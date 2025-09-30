# ===============================
# Script de limpieza Django
# ===============================

# 1️⃣ Borrar la base de datos
if (Test-Path "db.sqlite3") {
    Remove-Item "db.sqlite3" -Force
    Write-Output "Base de datos db.sqlite3 eliminada."
} else {
    Write-Output "No se encontró db.sqlite3."
}

# 2️⃣ Borrar migraciones antiguas
$apps = @("empleados","clientes","productos","inventarios","recetas","ventas","reportes","farmacia")

foreach ($app in $apps) {
    $migrationsPath = ".\$app\migrations"
    if (Test-Path $migrationsPath) {
        Get-ChildItem $migrationsPath -Filter "00*.py" | ForEach-Object { Remove-Item $_.FullName -Force }
        Write-Output "Migraciones de la app '$app' eliminadas."
    }
}

# 3️⃣ Borrar todas las carpetas __pycache__
Get-ChildItem -Recurse -Directory -Filter "__pycache__" | Remove-Item -Recurse -Force
Write-Output "Carpetas __pycache__ eliminadas."

Write-Output "✅ Limpieza completa. Ahora puedes crear nuevas migraciones."
