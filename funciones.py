import csv
import msvcrt
import os

contactos = []

def presione():
    print("Presione tecla para continuar: ")
    msvcrt.getch()

def limpiar():
    os.system("cls")

def opcion1():
    print("REGISTRAR CONTACTO")
    nombre = input("Ingrese nombre del contacto: ")
    fono = input("Ingrese numero de telefono: ")
    correo = input("Ingrese correo electronico: ")
    contacto = [nombre,fono,correo]
    contactos.append(contacto)
    print("CONTACTO REGISTRADO CON EXITO!")

def opcion2():
    if len(contactos)==0:
        print("No existen contactos")
    else:
        print("Nombre\tNumero de telefono\tCorreo Electronico")
        for i in contactos:
            print(f"Nombre:{i[0]} Numero de telefono:{i[1]} Correo electronico:{i[2]}")


def opcion3():
    print("Guardar contactos en un archivo CSV")
    archivo = input("Ingrese nombre de archivo.csv, siga este formato (nombre.csv)")
    with open(f"{archivo}", "w",newline="") as archivo:
        escritor = csv.writer(archivo)
        escritor.writerows(contactos)
        print("Archivo CSV creado con exito!")

def opcion4():
    print("Gracias por usar el programa, adios!")
    exit()


