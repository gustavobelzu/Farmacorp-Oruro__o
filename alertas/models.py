# alertas/models.py
from django.db import models
from inventarios.models import Inventario
from datetime import date

class Alerta(models.Model):
    tipo = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True, null=True)
    fecha_alerta = models.DateField(blank=True, null=True)
    estado = models.CharField(max_length=50, blank=True, null=True)
    inventario = models.ForeignKey(
        Inventario,
        on_delete=models.CASCADE,
        related_name='alertas',
        null=True,  # permite que la alerta exista aunque no haya inventario
        blank=True
    )

    # ======================
    # MÉTODO DE ALERTA
    # ======================
    def notificar_alerta(self):
        """Notifica sobre la alerta según su tipo o estado."""
        hoy = date.today()
        fecha = self.fecha_alerta.strftime("%Y-%m-%d") if self.fecha_alerta else "no definida"
        mensaje = f"Alerta tipo: {self.tipo} | Fecha: {fecha} | Estado: {self.estado or 'pendiente'}"
        
        # Ejemplo de notificación automática
        if self.tipo.lower() == "stock bajo" and self.inventario:
            mensaje += f" | Inventario: {self.inventario.id} - Cantidad: {self.inventario.cantidad}"
            if self.inventario.cantidad <= self.inventario.stock_minimo:
                mensaje += " ⚠️ Stock crítico, se recomienda reabastecer."
        
        if self.tipo.lower() == "producto vencido" and self.inventario:
            productos_vencidos = [
                p.nombre for p in self.inventario.productos.all() 
                if p.fecha_vencimiento and p.fecha_vencimiento <= hoy
            ]
            if productos_vencidos:
                mensaje += f" ⚠️ Productos vencidos: {', '.join(productos_vencidos)}"
        
        return mensaje

    def __str__(self):
        return f"Alerta {self.id} - Tipo: {self.tipo}"
