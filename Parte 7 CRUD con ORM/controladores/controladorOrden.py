from controladores.controladorCliente import ControladorCliente
from controladores.controladorSucursal import ControladorSucursal
from controladores.genericController import GenericController
from tortoise.fields.relational import BackwardFKRelation
from modelos import Ordenes
from vista import Interfaz

class ControladorOrden(GenericController):
    def __init__(self):
        self.atributos = {nombre:type(campo) for nombre, campo in Ordenes._meta.fields_map.items() if (not isinstance(campo, BackwardFKRelation) and nombre != 'id')}
        GenericController.__init__(self, Ordenes)

    async def create(self):
        clientes = await ControladorCliente().index()
        sucursales = await ControladorSucursal().index()
        if len(clientes) and len(sucursales):
            print("Ingrese la siguiente informacion de la Orden")
            info = Interfaz.getInfo(self.atributos)
            cliente_id = Interfaz.captureOptionObjects(clientes)
            sucursal_id = Interfaz.captureOptionObjects(sucursales)
            info['cliente'] = clientes[cliente_id]
            info['sucursal'] = sucursales[sucursal_id]
            return await GenericController.create(self, **info)
        else:
            return "Necesita crear un Cliente u Sucursal antes de crear una Orden"
        
    
    async def filter(self):
        indexOptions = {index: option for index, option in enumerate(self.atributos.keys())}
        atributo = Interfaz.captureOptionView(indexOptions)
        print("Ingrese la siguiente informacion de la Orden")
        info =  Interfaz.getInfo({indexOptions[atributo]: self.atributos[indexOptions[atributo]]})
        return await GenericController.filter(self, **info)
    
    async def delete(self):
        ordenes = await self.index()
        indexOptions = {index: categoria for index, categoria in enumerate(ordenes)}
        atributo = Interfaz.captureOptionView(indexOptions)
        return await GenericController.delete(self, ordenes[atributo])