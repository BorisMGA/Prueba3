import os 
os.system("cls")

menu= """ 

        ====================================
            Bienvenido  sajshajkshak
        ====================================

            1° Grabar vehiculo
            2° Buscar vehiculo
            3° Imprimir Certificado
            4° Salir 
        =======================================

            """
vehiculos = []

def grabar():
    tipo = input('Ingresa el tipo de vehiculo(automovil, moto )')
    patente = input('Ingresa la patente')
    marca =  input('Ingresa la marca ')
    precio = int(input('Ingresa el precio'))
    fecha_ingreso = input('Ingresa la fecha de ingreso')
    multas = input('Ingresa las multas')
    run_dueno = int(input('Ingresa el run del dueño'))
    nombre_dueno = input('Ingrese el run del dueno')



    vehiculo ={  
                'tipo': tipo,
                'patente': patente,
                'marca': marca,
                'precio': precio,
                'fecha_ingreso': fecha_ingreso,
                'multas': multas,
                'run_dueno': run_dueno,
                'nombre_dueno': nombre_dueno

    }
    vehiculos.append(vehiculo)
    print('Vehiculo guardado con exito')


def buscar():
    patente = input('Ingresa la patente del vehiculo a buscar')
    for vehiculo in vehiculos:
        if vehiculo['patente'] == patente:
            print('Informacion del vehiculo')
            for key, value in vehiculo.items():
                print(f'{key.capitalize()}:{value}')
            return
def imprimir():
    patente = input('Ingresa la patente del vehiculo a imprimir certificados:')
    for vehiculo in vehiculos:
        if vehiculo['patente'] == patente:
            certificado = {





            }







print(menu)
opcion = input('Ingresa una opcion valida ')

if opcion == "1":
    grabar()






























      

      
      
      
      
      
      
      
      
 