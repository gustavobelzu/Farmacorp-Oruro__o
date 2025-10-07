# reiniciar_proyecto.py
import os
import shutil

# 1. Borrar base de datos SQLite si existe
db_path = "db.sqlite3"
if os.path.exists(db_path):
    os.remove(db_path)
    print(f"Base de datos '{db_path}' borrada")
else:
    print(f"No existe base de datos '{db_path}'")

# 2. Limpiar migraciones de todas las apps
for root, dirs, files in os.walk(".", topdown=True):
    if "migrations" in dirs:
        migrations_path = os.path.join(root, "migrations")
        for f in os.listdir(migrations_path):
            if f != "__init__.py" and f.endswith(".py"):
                os.remove(os.path.join(migrations_path, f))
        print(f"Migraciones borradas en: {migrations_path}")

# 3. Limpiar archivos compilados de Python (__pycache__ y .pyc)
for root, dirs, files in os.walk(".", topdown=True):
    for dir_name in dirs:
        if dir_name == "__pycache__":
            shutil.rmtree(os.path.join(root, dir_name))
            print(f"__pycache__ borrado en: {os.path.join(root, dir_name)}")
    for file_name in files:
        if file_name.endswith(".pyc"):
            os.remove(os.path.join(root, file_name))
            print(f"{file_name} borrado")
