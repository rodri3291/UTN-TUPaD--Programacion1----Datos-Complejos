#1)Dado el diccionario precios_frutas.Añadir las siguientes frutas con sus respectivos precios:
Naranja = 1200
Manzana = 1500
Pera = 2300

precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva': 1450}
precios_frutas ['Naranja'] = 1200
precios_frutas ['Manzana'] = 1500
precios_frutas ['Pera'] = 2300

print("Diccionario actualizado:", precios_frutas)

#2)Siguiendo con el diccionario precios_frutas que resulta luego de ejecutar el código desarrollado en el punto anterior, actualizar los precios de las siguientes frutas:
Banana = 1330
Manzana = 1700
Melón = 2800

precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva': 1450, 'Naranja': 1200, 'Manzana': 1500, 'Pera': 2300}
precios_frutas.update({'Banana': 1330})
precios_frutas.update({'Manzana': 1700})
precios_frutas.update({'Melón': 2800})

print("Diccionario:",precios_frutas)

#3)Siguiendo con el diccionario precios_frutas que resulta luego de ejecutar el código desarrollado en el punto anterior, crear una lista que contenga únicamente las frutas sin los precios.
precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva': 1450, 'Naranja': 1200, 'Manzana': 1500, 'Pera': 2300}
precios_frutas: list = ["Banana","Ananá","Melón","Uva","Naranja","Manzana","Pera"]
for i in range(len(precios_frutas)):
    print(f"Lista de Frutas: {precios_frutas[i]}")

#4)Escribí un programa que permita almacenar y consultar números telefónicos.
contactos = {"Rodrigo": "123456", "Francisco": "464787", "Eugenia": "478347", "Chelita": "476546", "Graciela": "373647"}
nombre: int = input("Ingrese el nombre:").title()
numero: int = input("Ingrese el número:")

if nombre == "Rodrigo" and numero == "123456":
    print(f"El contacto:",nombre,numero,"existe")
elif nombre == "Francisco" and numero == "464787":
    print(f"El contacto:",nombre,numero, "existe")
elif nombre == "Eugenia" and numero == "478347":
    print(f"El contacto:",nombre,numero, "existe")
elif nombre == "Chelita" and numero == "476546":
    print(f"El contacto:",nombre,numero, "existe")
elif nombre == "Graciela" and numero == "373647":
    print(f"El contacto:",nombre,numero, "existe")
else:
    print(f"El contacto no existe")                              
        
            
#5)Solicita al usuario una frase e imprime:
frases = set()

while True:
    frase = input("Ingrese una frase (o ingrese salir para terminar):")
    if frase.lower() == "salir":
        break
    
    if frase in frases:
        print(f"Ya existe esa frase")
    else:
        frases.add(frase)
        print(f"Frase ingresada")
        
    print("Frases únicas guardadas:")
    for f in frases:
        print("",f)
            

#6)Permití ingresar los nombres de 3 alumnos, y para cada uno una tupla de 3 notas. Luego, mostrá el promedio de cada alumno.
alumnos = { "Rodrigo": (10,9,8), "Eugenia": (10,9,9),"Francisco": (10,10,9)}
print(alumnos)            

#7)Dado dos sets de números, representando dos listas de estudiantes que aprobaron Parcial 1 y Parcial 2:
estudiantes_parcial_1_aprobado = {"Rodrigo","Leandro","Gustavo","Agustina","Eugenia","Julieta","Lautaro","Facundo"}
estudiantes_parcial_2_aprobado = {"Rodrigo","Leandro","Gustavo","Eugenia"}

ambos = estudiantes_parcial_1_aprobado & estudiantes_parcial_2_aprobado
solo_uno = estudiantes_parcial_1_aprobado ^ estudiantes_parcial_2_aprobado
al_menos_uno = estudiantes_parcial_1_aprobado | estudiantes_parcial_2_aprobado

print("Alumnos que aprobaron ambos parciales",ambos)
print("Alumnos que aprobaron solo uno de los parciales",solo_uno)
print("Alumnos que aprobaron al menos un parcial",al_menos_uno)

#8)Armá un diccionario donde las claves sean nombres de productos y los valores su stock
frutas = {}

while True:
    print("Bienvenido a nuestro menú")
    print("1)Consultar el stock de un producto ingresado")
    print("2)Agregar unidades al stock si el producto ya existe")
    print("3)Agregar un nuevo producto si no existe")
    print("4)Salir del programa")
    
    opcion = input("Ingrese la opción que desee ejecutar:")
    
    if opcion == "1":
        frutas["Manzana"] = 10
        frutas["Banana"] = 15
        frutas["Pera"] = 8
        frutas["Naranja"] = 20
        frutas = {'Manzana':10,'Banana':15,'Pera':8,'Naranja':20}
        print("Productos disponibles:",frutas)
        for i in frutas:
            print(f"El stock de {i} es de {frutas[i]} unidades")
        
    elif opcion == "2":
        producto = input("Ingrese el nombre del producto:")
        if producto in frutas:
            frutas.update({producto: frutas[producto] + int(input("Ingrese la cantidad a agregar al stock:"))})
            print(f"El nuevo stock de {producto} es de {frutas[producto]} unidades")
        else:
            print(f"El producto no existe en el stock")
            
    elif opcion == "3":
        frutas = {'Manzana':10,'Banana':15,'Pera':8,'Naranja':20}
        producto = input("Ingrese el nombre del producto:")
        if producto in frutas:
            print(f"El producto ya existe en el stock")
        else:
            frutas[producto] = int(input("Ingrese la cantidad a agregar al stock:"))
            print(f"El producto {producto} ha sido agregado con un stock de {frutas[producto]} unidades")
            
    elif opcion == "4":
        print("Gracias por utilizar el programa")
        break
    else:
        print("Opción inválida, por favor intente nuevamente")
                
#9)Creá una agenda donde las claves sean tuplas de (día,hora) y los valores sean eventos.
agenda = {("Lunes", "10:00"): "Reunión", ("Martes", "15:00"): "Clase de inglés"}
dia = input("Ingrese el día del evento:")
hora = input("Ingrese la hora del evento:")
evento = input("Ingrese el nombre del evento:")
agenda[(dia, hora)] = evento
for clave, valor in agenda.items():
    print(f"El día {clave[0]} a las {clave[1]} tiene el evento: {valor}")

#10)Dado un diccionario que mapea nombres de países con sus capitales, construí un nuevo diccionario donde: .Las capitales sean las claves y los países sean los valores.
paises = ["Argentina", "Chile", "Brasil"]
capitales = ["Buenos Aires", "Santiago", "Brasilia"]

diccionario_paises_capitales = {"Argentina": "Buenos Aires", "Chile": "Santiago", "Brasil": "Brasilia"}
print("Diccionario original:", diccionario_paises_capitales)
diccionario_capitales_paises = {"Buenos Aires": "Argentina", "Santiago": "Chile", "Brasilia": "Brasil"}
print("Diccionario invertido:", diccionario_capitales_paises)                                                     