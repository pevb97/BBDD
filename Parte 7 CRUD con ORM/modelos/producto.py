import uuid
from tortoise import fields, models
from .categoria import Categorias

class Productos(models.Model):
    id = fields.UUIDField(pk=True, default=uuid.uuid4)
    nombre = fields.CharField(max_length=50, null=False)
    marca = fields.CharField(max_length=50, null=False)
    precio_und = fields.DecimalField(max_digits=10, decimal_places=2, null=True)
    categoria = fields.ForeignKeyField(model_name='models.Categorias', related_name='productos')

    def __str__(self) -> str:
        return f"Producto(Nombre: {self.nombre}, Marca: {self.marca}, Precio U: {float(self.precio_und)}, Categoria_id: {self.categoria_id})"