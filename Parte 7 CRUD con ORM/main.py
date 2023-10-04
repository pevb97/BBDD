import asyncio
from controladores import *
import modelos
from vista import Interfaz
from readchar import readkey, key

optionsModelos = dict([(i,  dato) for i, dato in enumerate(modelos.__all__)])
OPTIONSCRUD = {0:'Crear', 1:'Listar', 2:'Obtener', 3: 'Eliminar'}
controladores = {
    0: ControladorCategoria(),
    1: ControladorCliente(),
    2: ControladorItem(),
    3: ControladorOrden(),
    4: ControladorProducto(),
    5: ControladorStock(),
    6: ControladorSucursal(),
}


async def main():
    print("Oprima cualquier tecla para iniciar")
    while True:
        exit = readkey()
        if not (exit in [key.ESC, key.ESC_2]):
            respModelo = Interfaz.captureOptionView(optionsModelos)
            respCRUD = Interfaz.captureOptionView(OPTIONSCRUD)
            if(await GenericController.connDB()):
                controlador = controladores[respModelo]
                if(respCRUD == 0):
                    print(await controlador.create())
                elif(respCRUD == 1):
                    Interfaz.viewObject(await controlador.index())
                elif(respCRUD == 2):
                    Interfaz.viewObject(await controlador.filter())
                elif(respCRUD == 3):
                    print(await controlador.delete())
            print("Oprima cualquier tecla para continuar o ESC para salir")
        else:
            break



asyncio.run(main())





