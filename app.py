from flask import Flask, render_template, jsonify, request
import sqlite3
import os
import urllib.request
import urllib.parse
import json

app = Flask(__name__)
DB_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "catecismo.db")

# Crear la base de datos al iniciar si no existe
if not os.path.exists(DB_PATH):
    from crear_db import crear_base_de_datos
    crear_base_de_datos()

def get_db():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/api/preguntas")
def listar_preguntas():
    lang = request.args.get("lang", "es")
    conn = get_db()
    if lang == "en":
        preguntas = conn.execute(
            "SELECT id, domingo, pregunta_en as pregunta FROM catecismo ORDER BY id"
        ).fetchall()
    else:
        preguntas = conn.execute(
            "SELECT id, domingo, pregunta FROM catecismo ORDER BY id"
        ).fetchall()
    conn.close()
    return jsonify([dict(p) for p in preguntas])

@app.route("/api/pregunta/<int:pregunta_id>")
def obtener_pregunta(pregunta_id):
    lang = request.args.get("lang", "es")
    conn = get_db()
    if lang == "en":
        pregunta = conn.execute(
            "SELECT id, domingo, pregunta_en as pregunta, respuesta_en as respuesta, meditacion_en as meditacion, referencias FROM catecismo WHERE id = ?",
            (pregunta_id,)
        ).fetchone()
    else:
        pregunta = conn.execute(
            "SELECT id, domingo, pregunta, respuesta, meditacion, referencias FROM catecismo WHERE id = ?",
            (pregunta_id,)
        ).fetchone()
    conn.close()
    if pregunta:
        return jsonify(dict(pregunta))
    return jsonify({"error": "Pregunta no encontrada"}), 404

@app.route("/api/domingo/<int:domingo_num>")
def obtener_por_domingo(domingo_num):
    lang = request.args.get("lang", "es")
    conn = get_db()
    if lang == "en":
        preguntas = conn.execute(
            "SELECT id, domingo, pregunta_en as pregunta, respuesta_en as respuesta, meditacion_en as meditacion, referencias FROM catecismo WHERE domingo = ? ORDER BY id",
            (domingo_num,)
        ).fetchall()
    else:
        preguntas = conn.execute(
            "SELECT * FROM catecismo WHERE domingo = ? ORDER BY id", (domingo_num,)
        ).fetchall()
    conn.close()
    return jsonify([dict(p) for p in preguntas])

@app.route("/api/buscar")
def buscar():
    termino = request.args.get("q", "")
    lang = request.args.get("lang", "es")
    if not termino:
        return jsonify([])
    conn = get_db()
    if lang == "en":
        preguntas = conn.execute(
            "SELECT id, domingo, pregunta_en as pregunta FROM catecismo WHERE pregunta_en LIKE ? OR respuesta_en LIKE ? ORDER BY id",
            (f"%{termino}%", f"%{termino}%")
        ).fetchall()
    else:
        preguntas = conn.execute(
            "SELECT id, domingo, pregunta FROM catecismo WHERE pregunta LIKE ? OR respuesta LIKE ? ORDER BY id",
            (f"%{termino}%", f"%{termino}%")
        ).fetchall()
    conn.close()
    return jsonify([dict(p) for p in preguntas])

@app.route("/api/biblia")
def obtener_texto_biblico():
    ref = request.args.get("ref", "")
    lang = request.args.get("lang", "es")
    if not ref:
        return jsonify({"error": "Referencia no proporcionada"}), 400

    # Para espanol, usar base de datos local
    if lang == "es":
        conn = get_db()
        resultado = conn.execute("SELECT texto FROM biblia WHERE referencia = ?", (ref,)).fetchone()
        conn.close()
        if resultado:
            return jsonify({"texto": resultado["texto"], "referencia": ref})
        return jsonify({"error": f"No se encontro el texto de {ref}"}), 404

    # Para ingles, intentar base de datos local primero, luego API externa
    conn = get_db()
    resultado = conn.execute("SELECT texto_en FROM biblia WHERE referencia = ? AND texto_en IS NOT NULL AND texto_en != ''", (ref,)).fetchone()
    conn.close()
    if resultado:
        return jsonify({"texto": resultado["texto_en"], "referencia": ref})

    # Fallback: bible-api.com (funciona bien en ingles)
    try:
        url = f"https://bible-api.com/{urllib.parse.quote(ref)}"
        req = urllib.request.Request(url, headers={"User-Agent": "CatecismoHeidelberg/1.0"})
        with urllib.request.urlopen(req, timeout=10) as response:
            data = json.loads(response.read().decode("utf-8"))
            if "text" in data and data["text"]:
                return jsonify({"texto": data["text"].strip(), "referencia": data.get("reference", ref)})
            elif "verses" in data and data["verses"]:
                texto = " ".join(v["text"] for v in data["verses"]).strip()
                return jsonify({"texto": texto, "referencia": data.get("reference", ref)})
    except Exception:
        pass

    return jsonify({"error": f"Could not find text for {ref}"}), 404

if __name__ == "__main__":
    if not os.path.exists(DB_PATH):
        from crear_db import crear_base_de_datos
        crear_base_de_datos()

    print("=" * 50)
    print("  CATECISMO DE HEIDELBERG")
    print("  Abre tu navegador en: http://localhost:5000")
    print("=" * 50)
    app.run(debug=True, port=5000)
