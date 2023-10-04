from controladores.controladorCategoria import ControladorCategoria
from controladores.genericController import GenericController
from tortoise.fields.relational import BackwardFKRelation
from modelos import Productos
from vista import Interfaz

class ControladorProducto(GenericController):
    def __init__(self):
        self.atributos = {nombre:type(campo) for nombre, campo in Productos._meta.fields_map.items() if (not isinstance(campo, BackwardFKRelation) and nombre != 'id')}
        GenericController.__init__(self, Productos)

    async def create(self):
        categorias = await ControladorCategoria().index()
        if len(categorias):
            print("Ingrese la siguiente informacion del Producto")
            info = Interfaz.getInfo(self.atributos)
            categoria_id = Interfaz.captureOptionObjects(categorias)
            info['categoria'] = categorias[categoria_id]
            return await GenericController.create(self, **info)
        else:
            return "Necesita crear una Categoria antes de crear un Producto"
        
    
    async def filter(self):
        indexOptions = {index: option for index, option in enumerate(self.atributos.keys())}
        atributo = Interfaz.captureOptionView(indexOptions)
        print("Ingrese la siguiente informacion del Producto")
        info =  Interfaz.getInfo({indexOptions[atributo]: self.atributos[indexOptions[atributo]]})
        return await GenericController.filter(self, **info)
    
    async def delete(self):
        productos = await self.index()
        indexOptions = {index: categoria for index, categoria in enumerate(productos)}
        atributo = Interfaz.captureOptionView(indexOptions)
        return await GenericController.delete(self, productos[atributo])