from tortoise.queryset import QuerySet
from tortoise.models import Model
from tortoise import Tortoise

class GenericController:
    def __init__(self, model: Model):
        self.model = model
    
    #CREAR
    async def create(self, **kwargs):
        try:
            return await self.model.create(**kwargs)
        except Exception as e:
            return e

    #OBTENER 1
    async def get(self, **kwargs):
        try:
            return await self.model.get_or_none(**kwargs)
        except Exception as e:
            return e

    #LISTAR
    async def index(self):
        try:
            res = await self.model.all()
            return res
        except Exception as e:
            return e

    #OBTENER SEGUN FILTRO
    async def filter(self, **kwargs) -> QuerySet:
        try:
            return await self.model.filter(**kwargs).all()
        except Exception as e:
            return e

    #ACTUALIZAR
    async def update(self, instance: Model, **kwargs):
        try:
            for key, value in kwargs.items():
                setattr(instance, key, value)
            return await instance.save()
        except Exception as e:
            return e

    #ELIMINAR
    async def delete(self, instance: Model):
        try:
            await instance.delete()
            return "Eliminado"
        except Exception as e:
            return e
    
    @classmethod
    async def connDB(cls):
        try:
            await Tortoise.init(
                db_url='postgres://kvgmkfdy:llJ3r-JXPgZML2GlRjklF8utNyianxEL@peanut.db.elephantsql.com/kvgmkfdy',
                modules={'models': ['modelos']}
            )
            await Tortoise.generate_schemas()
            return True
        except Exception as e:
            return False
        
