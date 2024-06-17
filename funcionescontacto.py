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
    while True:
        nombre = input("Ingrese nombre del contacto: ")
        if len(nombre) >= 3:
            break
        else:
            print("Error, el nombre debe contener 3 caracteres o mas")
    while True:
        try:
            fono = int(input("Ingrese numero de telefono: "))
            if len(str(fono)) >= 9:
                break
            else:
                print("Error, el numero debe contener 9 numeros")
        except:
            print("Error, solo se permiten numeros enteros")
    while True:
        email = input("Ingrese correo electronico: ")
        if "@" in email:
            break
        else:
            print("Error, el correo electronico no es valido")
    contacto = ({
        "nombre": nombre,
        "fono": fono,
        "email": email
    })
    contactos.append(contacto)
    print("CONTACTO REGISTRADO CON EXITO!")

def opcion2():
    if len(contactos)==0:
        print("No existen contactos")
    else:
        for i in contactos:
            print(f"Nombre:{i["nombre"]} Telefono:{i["fono"]} Correo electronico:{i["email"]}")


def opcion3():
    if len(contactos)==0:
        print("No hay contactos guardados")
    else:
        print("Guardar contactos en un archivo CSV")
        archivo = input("Ingrese nombre de archivo.csv, siga este formato (nombre.csv)")
        with open(f"{archivo}", "w",newline="") as archivo:
            importar = ["nombre","fono","email"]
            write = csv.DictWriter(archivo,fieldnames=importar)
            write.writeheader()
            write.writerows(contactos)
            print("Archivo CSV creado con exito!")

def opcion4():
    print("Gracias por usar el programa, adios!")
    exit()


