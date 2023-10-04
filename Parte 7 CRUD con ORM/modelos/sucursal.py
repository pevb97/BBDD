import uuid
from tortoise import fields, models

class Sucursales(models.Model):
    id = fields.UUIDField(pk=True, default=uuid.uuid4)
    nombre = fields.CharField(max_length=50, null=False)
    direccion = fields.CharField(max_length=50, null=False)

    def __str__(self) -> str:
        return f"Sucursal(Nombre: {self.nombre}, Direccion: {self.direccion})"