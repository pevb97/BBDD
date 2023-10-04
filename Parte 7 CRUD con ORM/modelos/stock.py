import uuid
from tortoise import fields, models
from .producto import Productos
from .sucursal import Sucursales


class Stocks(models.Model):
    id = fields.UUIDField(pk=True, default=uuid.uuid4)
    cantidad = fields.IntField()
    producto = fields.ForeignKeyField(model_name='models.Productos', related_name='stocks')
    sucursal = fields.ForeignKeyField(model_name='models.Sucursales', related_name='stocks')

    def __str__(self) -> str:
        return f"Stock(Cantidad: {self.cantidad}, Producto_id: {self.producto_id}, Sucursal_id: {self.sucursal_id})"