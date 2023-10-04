import uuid
from tortoise import fields, models
from .cliente import Clientes
from .sucursal import Sucursales

class Ordenes(models.Model):
    id = fields.UUIDField(pk=True, default=uuid.uuid4)
    fecha = fields.DatetimeField(null=False)
    total = fields.DecimalField(max_digits=10, decimal_places=2, null=False)
    cliente = fields.ForeignKeyField(model_name='models.Clientes', related_name='ordenes')
    sucursal = fields.ForeignKeyField(model_name='models.Sucursales', related_name='ordenes')
    
    def __str__(self) -> str:
        return f"Orden(Fecha: {self.fecha}, Total: {float(self.total)}, Cliente_id: {self.cliente_id}, Sucursal_id: {self.sucursal_id})"