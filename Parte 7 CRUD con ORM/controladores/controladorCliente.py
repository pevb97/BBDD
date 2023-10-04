from controladores.genericController import GenericController
from tortoise.fields.relational import BackwardFKRelation
from modelos import Clientes
from vista import Interfaz

class ControladorCliente(GenericController):
    def __init__(self):
        self.atributos = {nombre:type(campo) for nombre, campo in Clientes._meta.fields_map.items() if (not isinstance(campo, BackwardFKRelation) and nombre != 'id')}
        GenericController.__init__(self, Clientes)

    async def create(self):
        print("Ingrese la siguiente informacion del Cliente")
        info = Interfaz.getInfo(self.atributos)
        return await GenericController.create(self, **info)
    
    async def filter(self):
        indexOptions = {index: option for index, option in enumerate(self.atributos.keys())}
        atributo = Interfaz.captureOptionView(indexOptions)
        print("Ingrese la siguiente informacion del Cliente")
        info =  Interfaz.getInfo({indexOptions[atributo]: self.atributos[indexOptions[atributo]]})
        return await GenericController.filter(self, **info)
    
    async def delete(self):
        clientes = await self.index()
        indexOptions = {index: categoria for index, categoria in enumerate(clientes)}
        atributo = Interfaz.captureOptionView(indexOptions)
        return await GenericController.delete(self, clientes[atributo])
        