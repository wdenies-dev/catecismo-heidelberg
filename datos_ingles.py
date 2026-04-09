import sqlite3
import os

DB_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "catecismo.db")

def actualizar_ingles():
    from datos_ingles_1 import obtener_parte1
    from datos_ingles_2 import obtener_parte2
    from datos_ingles_3 import obtener_parte3

    datos = obtener_parte1() + obtener_parte2() + obtener_parte3()

    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    for item in datos:
        cursor.execute("""
            UPDATE catecismo
            SET pregunta_en = ?, respuesta_en = ?, meditacion_en = ?
            WHERE id = ?
        """, (item[1], item[2], item[3], item[0]))

    conn.commit()
    conn.close()
    print(f"Datos en ingles actualizados para {len(datos)} preguntas")

if __name__ == "__main__":
    actualizar_ingles()
