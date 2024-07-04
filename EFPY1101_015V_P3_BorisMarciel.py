###Boris Marciel


import os 
os.system("cls")
import random


nombre = ''
edad = ''
nif = ''
##CREO UNA VARIABLE CON EL MENU SOLICITADO
menu = """

    =======================================
            Menuusito lindo
    =======================================
        1° Grabar dato de una persona
        2° Buscar datos de una persona
        3° Imprimir certificados
        4° Salir
    ========================================
        """
##CREO UNA LISTA DONDE DESPUES GUARDARE EL DICCIONARIO CON LOS DATOS DE LA PERSONA GRABADA
datos_personas = []
##creo la funcion grabar
def grabar():    
    nombre =str(input('Ingresa tu nombre'))
    if nombre == '':
        print('Nombre invalido')
    

    edad= int(input('Ingresa tu edad'))
    if edad > 15:
        nif=input('Ingresa tu NIF')
        if nif == '':
            print('NIF invalido')
    else:
        if edad < 15:
            print('No es necesario tu NIF por ser menor de 15 anios')
            nif = ''

        
#creo el diccionario que guarda los datos de la persona grabada
    datos_persona= {
    
                'Nombre': nombre,
                'edad':edad,
                'nif':nif
            
                                            }
##ADJUNTO EL DICCIONARIO DENTRO DE LA LISTA DE LOS DATOS DE LAS PERSONAS
    datos_personas.append(datos_persona)
    
    
    
    
##CREO LA FUNCION DE BUSCAR LOS DATOS DE LA PERSONA POR SU NIF
def buscar():
    nif = input('Ingresa el nif de la persona a buscar')
    for datos_persona in datos_personas:
        if datos_persona['nif'] == nif:
            print('informacion de la persona')
            for key, value in datos_persona.items():
                print(f'{key}:{value}')
            return
        
##creo la funcion imprimir DE LOS CERTIFICADOS DE LA PERSONA
def imprimir():
    nif = input('Ingresa el NIF de la persona para imprrimir certificados')
    for datos_persona in datos_personas:
        if datos_persona['nif'] == nif:   
            certificado = {    
                        
                 "nacimiento": random.randint(1500,5000),
                 "estado conyugal": random.randint(1500,5000),
                 "pertenencia a la union europea": random.randint(1500,5000) 
                 
            
                        
        }
     ##Muestro los certificados solicitados mas los datos         
        print(f'Certificado nacimiento:{certificado['nacimiento']}')
        print(f'Certificado estado conyugal: {certificado['estado conyugal']}')
        print(f'Certificado pertenencia a la union europea:{certificado['pertenencia a la union europea']}')
        print(f'Nombre:{datos_persona['Nombre']}')
        print(f'Edad:{datos_persona['edad']}')
        print(f'NIF:{datos_persona['nif']}')
        return
    print('datos no encontrados')
    
    
    
    
    
    
    
##CREO LAS OPCIONES CORRESPONDIENTES AL MENU                  
while True:
    print(menu)
    opcion=input('Ingresa una opcion')

    if opcion == "1":
        grabar()
    elif opcion == "2":
        buscar()       
    elif opcion == "3":
        imprimir()
    elif opcion == "4":
        print('Salida exitosa')
        break
    
    
        
        
 
