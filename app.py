from flask import Flask, render_template, jsonify, request
import sqlite3
import os

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
    conn = get_db()
    preguntas = conn.execute(
        "SELECT id, domingo, pregunta FROM catecismo ORDER BY id"
    ).fetchall()
    conn.close()
    return jsonify([dict(p) for p in preguntas])

@app.route("/api/pregunta/<int:pregunta_id>")
def obtener_pregunta(pregunta_id):
    conn = get_db()
    pregunta = conn.execute(
        "SELECT * FROM catecismo WHERE id = ?", (pregunta_id,)
    ).fetchone()
    conn.close()
    if pregunta:
        return jsonify(dict(pregunta))
    return jsonify({"error": "Pregunta no encontrada"}), 404

@app.route("/api/domingo/<int:domingo_num>")
def obtener_por_domingo(domingo_num):
    conn = get_db()
    preguntas = conn.execute(
        "SELECT * FROM catecismo WHERE domingo = ? ORDER BY id", (domingo_num,)
    ).fetchall()
    conn.close()
    return jsonify([dict(p) for p in preguntas])

@app.route("/api/buscar")
def buscar():
    termino = request.args.get("q", "")
    if not termino:
        return jsonify([])
    conn = get_db()
    preguntas = conn.execute(
        "SELECT id, domingo, pregunta FROM catecismo WHERE pregunta LIKE ? OR respuesta LIKE ? ORDER BY id",
        (f"%{termino}%", f"%{termino}%")
    ).fetchall()
    conn.close()
    return jsonify([dict(p) for p in preguntas])

@app.route("/api/biblia")
def obtener_texto_biblico():
    ref = request.args.get("ref", "")
    if not ref:
        return jsonify({"error": "Referencia no proporcionada"}), 400

    conn = get_db()
    resultado = conn.execute("SELECT texto FROM biblia WHERE referencia = ?", (ref,)).fetchone()
    conn.close()

    if resultado:
        return jsonify({"texto": resultado["texto"], "referencia": ref})
    return jsonify({"error": f"No se encontró el texto de {ref}"}), 404

if __name__ == "__main__":
    # Crear la base de datos si no existe
    if not os.path.exists(DB_PATH):
        from crear_db import crear_base_de_datos
        crear_base_de_datos()

    print("=" * 50)
    print("  CATECISMO DE HEIDELBERG")
    print("  Abre tu navegador en: http://localhost:5000")
    print("=" * 50)
    app.run(debug=True, port=5000)
