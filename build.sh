#!/usr/bin/env bash
pip install -r requirements.txt
python crear_db.py
python actualizar_referencias.py
