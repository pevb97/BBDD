import os
import re
from tortoise.models import Model
from tortoise.fields import IntField, CharField, DecimalField,DatetimeField

class Interfaz:
    datePtron = r"^(0[1-9]|[1-2][0-9]|3[0-1])-(0[1-9]|1[0-2])-\d{4}$"
    def clearView():
        os.system('cls' if os.name=='nt' else 'clear')

    def captureOptionView(options: dict) -> int:
        Interfaz.clearView()
        for index, option in options.items():
            print(f"{index}-{option}")
        option = int(input("Escoge una opcion valida: "))
        return option if option in list(options.keys()) else Interfaz.captureOptionView(options)
    
    def captureOptionObjects(options: list[Model]) -> int:
        Interfaz.clearView()
        object_indexs = []
        for index, object in enumerate(options):
            object_indexs.append(index)
            print(index, object)
        option = int(input(f"Escoge el id a relacionar:"))
        return (option-1) if option in object_indexs else Interfaz.captureOptionObjects(options)
    
    def viewObject(objects:list):
        for object in objects:
            print(object)


    def getText(atributo: str)->str:
        response = input(f"Ingresa {atributo}: ")
        if response:
            return response
        else:
            return Interfaz.getText(atributo)
    
    def getNum(atributo: str)->float:
        response = float(input(f"Ingresa {atributo}: "))
        if response:
            return response
        else:
            return Interfaz.getNum(atributo)

    def getDate(atributo:str)->str:
        fecha = input(f"Ingresa {atributo}(dd-mm-aaaa): ")
        if re.match(Interfaz.datePtron, fecha):
            return fecha
        else:
            return Interfaz.getDate(atributo)

    def getInfo(atributos: dict):
        info = {}
        for atributo, tipo in atributos.items():
            if tipo == CharField:
                info[atributo] = Interfaz.getText(atributo)
            elif tipo in [IntField, DecimalField]:
                info[atributo] = Interfaz.getNum(atributo)
            elif tipo == DatetimeField:
                info[atributo] = Interfaz.getDate(atributo)
        return info
    
    

