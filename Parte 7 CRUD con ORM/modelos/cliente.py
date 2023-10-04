import uuid
from tortoise import fields, models

class Clientes(models.Model):
    id = fields.UUIDField(pk=True, default=uuid.uuid4)
    nombre = fields.CharField(max_length=50, null=False)
    telefono = fields.CharField(max_length=20, null=False)

    def __str__(self) -> str:
        return f"Cliente(Nombre: {self.nombre}, telefono: {self.telefono})"