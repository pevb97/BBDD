from controladores.genericController import GenericController
from controladores.controladorOrden import ControladorOrden
from controladores.controladorProducto import ControladorProducto
from tortoise.fields.relational import BackwardFKRelation
from modelos import Items
from vista import Interfaz

class ControladorItem(GenericController):
    def __init__(self):
        self.atributos = {nombre:type(campo) for nombre, campo in Items._meta.fields_map.items() if (not isinstance(campo, BackwardFKRelation) and nombre != 'id')}
        GenericController.__init__(self, Items)
    
    async def create(self):
        ordenes = await ControladorOrden().index()
        productos = await ControladorProducto().index()
        if len(ordenes) and len(productos):
            print("Ingrese la siguiente informacion del Item")
            info = Interfaz.getInfo(self.atributos)
            orden_id = Interfaz.captureOptionObjects(ordenes)
            producto_id = Interfaz.captureOptionObjects(productos)
            info['orden'] = ordenes[orden_id]
            info['producto'] = productos[producto_id]
            return await GenericController.create(self, **info)
        else:
            return "Necesita crear un producto u orden antes de crear un item"
        
    
    async def filter(self):
        indexOptions = {index: option for index, option in enumerate(self.atributos.keys())}
        atributo = Interfaz.captureOptionView(indexOptions)
        print("Ingrese la siguiente informacion del Item")
        info =  Interfaz.getInfo({indexOptions[atributo]: self.atributos[indexOptions[atributo]]})
        return await GenericController.filter(self, **info)
    
    async def delete(self):
        items = await self.index()
        indexOptions = {index: categoria for index, categoria in enumerate(items)}
        atributo = Interfaz.captureOptionView(indexOptions)
        return await GenericController.delete(self, items[atributo])
        
    