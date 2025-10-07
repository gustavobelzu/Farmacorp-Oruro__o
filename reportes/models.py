from django.db import models
from empleados.models import Empleado
from reportes import utils  # Importar funciones auxiliares


class Reporte(models.Model):
    id_reporte = models.AutoField(primary_key=True)
    fecha_reporte = models.DateField(auto_now_add=True)
    tipo = models.CharField(max_length=100)
    ci_empleado = models.ForeignKey(
        Empleado,
        on_delete=models.CASCADE,
        blank=True,
        null=True
    )
    #METODOS REPORTES
    def generar_graficos(self, datos):
        """Genera gráfico y lo guarda en /reportes/archivos/"""
        filename = f"grafico_reporte_{self.id_reporte}.png"
        return utils.generar_grafico(datos, filename)

    def exportar_reporte_pdf(self, datos):
        """Genera un PDF en /reportes/archivos/"""
        filename = f"reporte_{self.id_reporte}.pdf"
        return utils.exportar_pdf(datos, filename)

    def exportar_reporte_excel(self, datos):
        """Genera un Excel en /reportes/archivos/"""
        filename = f"reporte_{self.id_reporte}.xlsx"
        return utils.exportar_excel(datos, filename)

    def __str__(self):
        return f"Reporte {self.id_reporte} - {self.tipo}"
