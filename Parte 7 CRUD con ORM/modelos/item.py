import uuid
from tortoise import fields, models
from .orden import Ordenes
from .producto import Productos

class Items(models.Model):
    id = fields.UUIDField(pk=True, default=uuid.uuid4)
    cantidad = fields.IntField(null=False)
    monto_venta = fields.DecimalField(max_digits=10, decimal_places=2, null=False)
    orden = fields.ForeignKeyField(model_name='models.Ordenes', related_name='items')
    producto = fields.ForeignKeyField(model_name='models.Productos', related_name='items')

    def __str__(self) -> str:
        return f"Item(Cantidad: {self.cantidad}, Monto Venta: {float(self.monto_venta)}, Orden_id: {self.orden_id}, Producto_id: {self.producto_id})"