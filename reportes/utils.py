import os
from datetime import datetime
import matplotlib.pyplot as plt
import io
from reportlab.pdfgen import canvas
from openpyxl import Workbook

# Carpeta de destino de los reportes
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
REPORTS_DIR = os.path.join(BASE_DIR, "archivos")

# Asegurar que la carpeta exista
os.makedirs(REPORTS_DIR, exist_ok=True)


def generar_grafico(datos, nombre="grafico.png"):
    """Genera un gráfico de barras y lo guarda en la carpeta reportes/archivos."""
    fig, ax = plt.subplots()
    ax.bar(datos.keys(), datos.values())
    ax.set_title("Reporte Gráfico")

    filepath = os.path.join(REPORTS_DIR, nombre)
    plt.savefig(filepath)
    plt.close(fig)
    return filepath


def exportar_pdf(datos, nombre="reporte.pdf"):
    """Genera un PDF básico con ReportLab."""
    filepath = os.path.join(REPORTS_DIR, nombre)
    c = canvas.Canvas(filepath)
    c.drawString(100, 800, f"Reporte generado: {datetime.now().strftime('%Y-%m-%d %H:%M')}")
    for i, (k, v) in enumerate(datos.items(), start=1):
        c.drawString(100, 800 - i*20, f"{k}: {v}")
    c.save()
    return filepath


def exportar_excel(datos, nombre="reporte.xlsx"):
    """Genera un archivo Excel con OpenPyXL."""
    filepath = os.path.join(REPORTS_DIR, nombre)
    wb = Workbook()
    ws = wb.active
    ws.title = "Reporte"
    ws.append(["Campo", "Valor"])
    for k, v in datos.items():
        ws.append([k, v])
    wb.save(filepath)
    return filepath
