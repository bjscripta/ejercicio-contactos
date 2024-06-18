import time
from funcionescontacto import *

while True:
    limpiar()
    print("""
          1. Agregar contactos
          2. Mostrar contactos
          3. Imprimir planilla
          4. Salir del programa""")
    while True:
        try:
            opc = int(input("Ingrese opcion: "))
            if opc in (1,2,3,4):
                break
            else:
                print("ERROR, Opcion no disponible")
        except:
            print("ERROR, solo se permiten numeros enteros")
    limpiar()
    if opc==1:
        opcion1()
    elif opc==2:
        opcion2()
    elif opc==3:
        opcion3()
    else:
        opcion4()
    time.sleep(2)