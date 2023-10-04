from tortoise.fields.relational import BackwardFKRelation
from controladores.genericController import GenericController
from modelos import Categorias
from vista import Interfaz


class ControladorCategoria(GenericController):
    def __init__(self):
        self.atributos = {nombre:type(campo) for nombre, campo in Categorias._meta.fields_map.items() if (not isinstance(campo, BackwardFKRelation) and nombre != 'id')}
        GenericController.__init__(self, Categorias)
        
    async def create(self):
        print("Ingrese la siguiente informacion de la Categoria")
        info = Interfaz.getInfo(self.atributos)
        return await GenericController.create(self, **info)
    

    async def filter(self):
        indexOptions = {index: option for index, option in enumerate(self.atributos.keys())}
        atributo = Interfaz.captureOptionView(indexOptions)
        print("Ingrese la siguiente informacion de la Categoria")
        info =  Interfaz.getInfo({indexOptions[atributo]: self.atributos[indexOptions[atributo]]})
        return await GenericController.filter(self, **info)
        
        
    async def delete(self):
        categorias = await self.index()
        indexOptions = {index: categoria for index, categoria in enumerate(categorias)}
        atributo = Interfaz.captureOptionView(indexOptions)
        return await GenericController.delete(self, categorias[atributo])
