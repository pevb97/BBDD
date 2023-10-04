from tortoise import fields, models
import uuid

class Categorias(models.Model):
    id = fields.UUIDField(pk=True, default=uuid.uuid4)
    nombre = fields.CharField(max_length=50, null=False)

    def __str__(self) -> str:
        return f"Categoria(Nombre: {self.nombre})"