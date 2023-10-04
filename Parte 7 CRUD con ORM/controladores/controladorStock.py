from controladores.controladorProducto import ControladorProducto
from controladores.controladorSucursal import ControladorSucursal
from controladores.genericController import GenericController
from tortoise.fields.relational import BackwardFKRelation
from modelos import Stocks
from vista import Interfaz

class ControladorStock(GenericController):
    def __init__(self):
        self.atributos = {nombre:type(campo) for nombre, campo in Stocks._meta.fields_map.items() if (not isinstance(campo, BackwardFKRelation) and nombre != 'id')}
        GenericController.__init__(self, Stocks)

    async def create(self):
        productos = await ControladorProducto().index()
        sucursales = await ControladorSucursal().index()
        if len(productos) and len(sucursales):
            print("Ingrese la siguiente informacion del Stock")
            info = Interfaz.getInfo(self.atributos)
            producto_id = Interfaz.captureOptionObjects(productos)
            sucursal_id = Interfaz.captureOptionObjects(sucursales)
            info['sucursal'] = sucursales[sucursal_id]
            info['producto'] = productos[producto_id]
            return await GenericController.create(self, **info)
        else:
            return "Necesita crear un Producto o Sucursal antes de crear un Stock"

    
    async def filter(self):
        indexOptions = {index: option for index, option in enumerate(self.atributos.keys())}
        atributo = Interfaz.captureOptionView(indexOptions)
        print("Ingrese la siguiente informacion del Stock")
        info =  Interfaz.getInfo({indexOptions[atributo]: self.atributos[indexOptions[atributo]]})
        return await GenericController.filter(self, **info)
    
    async def delete(self):
        stocks = await self.index()
        indexOptions = {index: categoria for index, categoria in enumerate(stocks)}
        atributo = Interfaz.captureOptionView(indexOptions)
        return await GenericController.delete(self, stocks[atributo])