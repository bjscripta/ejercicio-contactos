import time
from funciones import *

while True:
    limpiar()
    print("""
          1. Agregar contactos
          2. Mostrar contactos
          3. Imprimir planilla
          4. Salir del programa""")
    opc = int(input("Ingrese opcion: "))
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