# borrar_bd.py
import os

if os.path.exists("db.sqlite3"):
    os.remove("db.sqlite3")
    print("Base de datos borrada")
else:
    print("No existe db.sqlite3")
