#*SOLUCIONES 40 KATAS PYTHON*#


#1. Escribe una función que reciba una cadena de texto como parámetro y devuelva un diccionario con las frecuencias de cada letra en la cadena. Los espacios no deben ser considerados.

def frecuencias_letras(cadena_texto):
    frecuencia = {}

    for letra in cadena_texto:
        if letra == " ":
            continue

        letra = letra.lower()
        frecuencia[letra] = frecuencia.get(letra, 0) + 1
            
    return frecuencia



#2. Dada una lista de números, obtén una nueva lista con el doble de cada valor. Usa la función map()

def doble_valor(lista):

    doble = list(map(lambda x: x*2, lista))
    
    return doble



#3. Escribe una función que tome una lista de palabras y una palabra objetivo como parámetros. La función debe devolver una lista con todas las palabras de la lista original que contengan la palabra objetivo.

def lista_objetivo(lista, palabra_objetivo):

    lista_final = []

    for palabra in lista:
        if palabra.count(palabra_objetivo) > 0:
            lista_final.append(palabra)
    
    return lista_final



#4. Genera una función que calcule la diferencia entre los valores de dos listas. Usa la función map()

def diferencia_listas(lista1, lista2):

    if len(lista1) != len(lista2):

        raise ValueError('Las listas deben tener la misma longitud')    # he usado raise porque lo aprendimos con el profesor Edu cuando hicimos algunos ejercicios
    
    diferencias = list(map(lambda x, y: x-y, lista1, lista2))
    
    return diferencias



#5. Escribe una función que tome una lista de números como parámetro y un valor opcional nota_aprobado, que por defecto es 5. La función debe calcular la media de los números en la lista y determinar si la media es mayor o igual que nota aprobado. Si es así, el estado será "aprobado", de lo contrario, será "suspenso". La función debe devolver una tupla que contenga la media y el estado.

from functools import reduce

def media_num(lista, nota_aprobado = 5):
        
    total = reduce(lambda x, y: x+y, lista)
    media = total/len(lista)

    if media >= nota_aprobado:
        estado = "aprobado"

    else:
        estado = "suspenso"

    return (media, estado)



#6. Escribe una función que calcule el factorial de un número de manera recursiva.

def factorial_num(numero):
    
    if numero == 0 or numero == 1:
        return 1
    
    else:
        return numero * factorial_num(numero - 1)



#7. Genera una función que convierta una lista de tuplas a una lista de strings. Usa la función map()

def tuplas_string(lista):

    return list(map(str, lista))



#8. Escribe un programa que pida al usuario dos números e intente dividirlos. Si el usuario ingresa un valor no numérico o intenta dividir por cero, maneja esas excepciones de manera adecuada. Asegúrate de mostrar un mensaje indicando si la división fue exitosa o no.

print('Escribe el primer número')
numero_1 = input()
print('Escribe tu segundo número')
numero_2 = input()

try:

    numero_1 = float(numero_1)
    numero_2 = float(numero_2)

    total = numero_1/numero_2

except ValueError:

    print('ERROR, asegurate de introducir valores numéricos')

except ZeroDivisionError:

    print('ERROR, no se puede dividir por 0, asegúrate de que el segundo número que introduzcas no sea un 0')

else:
    print(f'GENIAL, la solución de dividir {numero_1} entre {numero_2} es {total:.2f}')  #he restringido el total para que solo me de dos decimales



#9. Escribe una función que tome una lista de nombres de mascotas como parámetro y devuelva una nueva lista excluyendo ciertas mascotas prohibidas en España. La lista de mascotas a excluir es ["Mapache", "Tigre", "Serpiente Pitón", "Cocodrilo", "Oso"].Usa la función filter()

def excluir_mascotas(lista_mascotas):

    mascotas_prohibidas = ["Mapache", "Tigre", "Serpiente Pitón", "Cocodrilo", "Oso"]

    return list(filter(lambda mascota: mascotas_prohibidas.count(mascota) == 0, lista_mascotas))



#10. Escribe una función que reciba una lista de números y calcule su promedio. Si la lista está vacía, lanza una excepción personalizada y maneja el error adecuadamente.

def calcular_promedio(lista_numeros):

    if len(lista_numeros) == 0:

        raise ValueError('La lista está vacía')  # también se podría haber usado el try except
    
    return sum(lista_numeros)/ len(lista_numeros)



#11. Escribe un programa que pida al usuario que introduzca su edad. Si el usuario ingresa un valor no numérico o un valor fuera del rango esperado (por ejemplo, menor que 0 o mayor que 120), maneja las excepciones adecuadamente.

try:
    print('Introduzca su edad por favor:')
    edad = input()
    edad = int(edad)

    if edad < 1 or edad > 119:
        raise ValueError('ERROR, la edad introducida no es válida, recuerda introducir una edad entre 1-119')

except ValueError:
    print('ERROR, no se ha introducido un valor númerico')

else:
    print(f'La edad del usuario es: {edad}')



#12. Genera una función que al recibir una frase devuelva una lista con la longitud de cada palabra. Usa la función map()

def longitud_palabras(frase):

    palabras = frase.split()

    longitudes = list(map(lambda x: len(x), palabras))

    return longitudes



#13. Genera una función la cual, para un conjunto de caracteres, devuelva una lista de tuplas con cada letra en mayúsculas y minúsculas. Las letras no pueden estar repetidas .Usa la función map()

def mayusculas_minusculas(caracteres):

    caracteres_unicos = list(set(caracteres.lower()))

    return list(map(lambda c: (c.upper(), c.lower()), caracteres_unicos))



#14. Crea una función que retorne las palabras de una lista de palabras que comience con una letra en especifico. Usa la función filter()

def coincide_letra(lista_palabras, letra):

    return list(filter(lambda palabra: len(palabra) > 0 and palabra[0] == letra, lista_palabras))



#15. Crea una función lambda que sume 3 a cada número de una lista dada.


def sum_tres(lista):

    return list(map(lambda x: x+3, lista))



#16. Escribe una función que tome una cadena de texto y un número entero n como parámetros y devuelva una lista de todas las palabras que sean más largas que n. Usa la función filter()

def palabras_mas_largas(cadena, n):

    palabras = cadena.split() #he usado .split como ya aprendimos con Edu en el enunciado 12

    return list(filter(lambda palabra: len(palabra) > n, palabras))



#17. Crea una función que tome una lista de dígitos y devuelva el número correspondiente. Por ejemplo, [5,7,2] corresponde al número quinientos setenta y dos (572). Usa la función reduce()

from functools import reduce

def numero_correspondiente(lista_digitos):

    return reduce(lambda x, y: x * 10 + y, lista_digitos)



#18. Escribe un programa en Python que cree una lista de diccionarios que contenga información de estudiantes (nombre, edad, calificación) y use la función filter para extraer a los estudiantes con una calificación mayor o igual a 90. Usa la función filter()

estudiantes = [
    {'nombre': 'Diana', 'edad': 8, 'calificación': 54},
    {'nombre': 'Mónica', 'edad': 54, 'calificación': 89},
    {'nombre': 'Jessy', 'edad': 16, 'calificación': 97},
    {'nombre': 'Laura', 'edad': 32, 'calificación': 99},
    {'nombre': 'Iryna', 'edad': 19, 'calificación': 90},
]

def calificacion_alta(estudiante):
    estudiante_destacados = list(filter(lambda estudiante: estudiante['calificación'] >= 90, estudiantes))
    return estudiante_destacados



#19. Crea una función lambda que filtre los números impares de una lista dada.

lista_numeros = [12, 43, 53, 67, 88, 94, 51, 21, 42, 99, 75, 68]

filtrar_impares = list(filter(lambda x: x % 2 != 0, lista_numeros))



#20. Para una lista con elementos tipo integer y string obtén una nueva lista sólo con los valores int. Usa la función filter()

def solo_num(lista):

    return list(filter(lambda x: type(x) == int, lista))



#21. Crea una función que calcule el cubo de un número dado mediante una función lambda

calcular_cubo = lambda x: x**3



#22. Dada una lista numérica, obtén el producto total de los valores de dicha lista. Usa la función reduce() .

from functools import reduce  # necesitamos el módulo functools para importar la función reduce, ya que esta no viene de serie en Python

lista_numerica = [13, 15, 18, 26, 31, 37, 40]

producto_total = reduce(lambda x, y: x*y, lista_numerica)



#23. Concatena una lista de palabras. Usa la función reduce().

from functools import reduce  # de nuevo necesitamos el módulo functools para importar la función reduce

def concat_palabras(lista_palabras):

    return reduce(lambda x, y: x + y, lista_palabras)



#24. Calcula la diferencia total en los valores de una lista. Usa la función reduce() .

from functools import reduce  # otra vez

def dif_total(lista):

    if len(lista) == 0:
        raise ValueError('La lista está vacía')

    return reduce(lambda x, y: x - y, lista)



#25. Crea una función que cuente el número de caracteres en una cadena de texto dada.

def cont_num(cadena):
    
    return len(cadena)



#26. Crea una función lambda que calcule el resto de la división entre dos números dados.

def resto_num(numero_1, numero_2):

    return (lambda x, y: x % y) (numero_1, numero_2)



#27. Crea una función que calcule el promedio de una lista de números.

from functools import reduce

def promedio_num(lista):

    if len(lista) == 0:

        raise ValueError('La lista está vacía')
    
    total = reduce(lambda x, y: x + y, lista)

    promedio = total/len(lista)

    return promedio



#28. Crea una función que busque y devuelva el primer elemento duplicado en una lista dada.

def primer_duplicado(lista):

    vistos = []

    for elemento in lista:

        encontrado = False

        for v in vistos:

            if v == elemento:

                encontrado = True

                break

        if encontrado:

            return elemento
        
        vistos.append(elemento)
        
    return None  



#29. Crea una función que convierta una variable en una cadena de texto y enmascare todos los caracteres con el carácter '#', excepto los últimos cuatro.

def masc_num(variable):

    cadena_texto = str(variable)

    if len(cadena_texto) < 5:

        return cadena_texto  
    
    return "#" * (len(cadena_texto) - 4) + cadena_texto[-4:]



#30. Crea una función que determine si dos palabras son anagramas, es decir, si están formadas por las mismas letras pero en diferente orden.

def anagrama(palabra_1, palabra_2):

    return sorted(palabra_1.lower()) == sorted(palabra_2.lower())  # tuve que buscar la función incorporada sorted, que solo habíamos dado en el apartado de listas, pero no sabía que funcionaba con cualquier iterable 



#31. Crea una función que solicite al usuario ingresar una lista de nombres y luego solicite un nombre para buscar en esa lista. Si el nombre está en la lista, se imprime un mensaje indicando que fue encontrado, de lo contrario, se lanza una excepción.

nombres = []

while True:

    nombre = input("Ingrese un nombre o escriba fin para finalizar: ")

    if nombre.lower() == "fin":
        
        break
    
    nombres.append(nombre)

buscar = input("Ingresa el nombre que quieres buscar: ")

    
if buscar in nombres:
        
    print(f"¡El nombre '{buscar}' fue encontrado en la lista!")

else:
    
    raise ValueError(f"ERROR: El nombre '{buscar}' no se encuentra en la lista.")



#32. Crea una función que tome un nombre completo y una lista de empleados, busque el nombre completo en la lista y devuelve el puesto del empleado si está en la lista, de lo contrario, devuelve un mensaje indicando que la persona no trabaja aquí.

def buscar_empleado(nombre_completo, empleados):

    if nombre_completo in empleados:

        return f"{nombre_completo} trabaja como {empleados[nombre_completo]}"  # he usado un diccionario para que sea más fácil y directo acceder al puesto de trabajo de cada empleado
    
    else:
        
        return f"ERROR: La persona '{nombre_completo}' no trabaja aquí."



#33. Crea una función lambda que sume elementos correspondientes de dos listas dadas.

def sum_elem(lista_1, lista_2):

    if len(lista_1) != len(lista_2):

        raise ValueError("ERROR, las listas deben tener la misma longitud")
    
    return list(map(lambda x, y: x + y, lista_1, lista_2))



#34. Crea la clase Arbol , define un árbol genérico con un tronco y ramas como atributos. Los métodos disponibles son: crecer_tronco , nueva_rama , crecer_ramas , quitar_rama e info_arbol . El objetivo es implementar estos métodos para manipular la estructura del árbol. 

# Código a seguir:

    #1. Inicializar un árbol con un tronco de longitud 1 y una lista vacía de ramas.
    #2. Implementar el método crecer_tronco para aumentar la longitud del tronco en una unidad.
    #3. Implementar el método nueva_rama para agregar una nueva rama de longitud 1 a la lista de ramas.
    #4. Implementar el método crecer_ramas para aumentar en una unidad la longitud de todas las ramas existentes.
    #5. Implementar el método quitar_rama para eliminar una rama en una posición específica.
    #6. Implementar el método info_arbol para devolver información sobre la longitud del tronco, el número de ramas y las longitudes de las mismas. 

class Arbol:
    
    def __init__(self):  #<--- 1.
        self.tronco = 1
        self.ramas = []

    def crecer_tronco(self):  #<--- 2.
        self.tronco += 1

    def nueva_rama(self):  #<--- 3.
        self.ramas.append(1)

    def crecer_ramas(self):  #<--- 4.
        self.ramas = [longitud + 1 for longitud in self.ramas]

    def quitar_ramas(self, posicion):  #<--- 5.
        
        if 0 <= posicion < len(self.ramas):
            
            self.ramas.pop(posicion)

        else:
            print(f'ERROR, no se ha podido quitar la rama: la posición {posicion} no es válida')

    def info_arbol(self):  #<--- 6.
        
        return(f'Longitud del tronco: {self.tronco}\n'
               f'Número de ramas: {len(self.ramas)}\n'
               f'Longitud de las ramas: {self.ramas}')


# Caso de uso:

    #1. Crear un árbol.

    roble = Arbol()

    #2. Hacer crecer el tronco del árbol una unidad.

    roble.crecer_tronco()

    #3. Añadir una nueva rama al árbol.

    roble.nueva_rama()

    #4. Hacer crecer todas las ramas del árbol una unidad.

    roble.crecer_ramas()

    #5. Añadir dos nuevas ramas al árbol.

    roble.nueva_rama()
    roble.nueva_rama()

    #6. Retirar la rama situada en la posición 2.

    roble.quitar_ramas(2)

    #7. Obtener información sobre el árbol.

    print(roble.info_arbol())



#36. Crea la clase UsuarioBanco, representa a un usuario de un banco con su nombre, saldo y si tiene o no cuenta corriente. Proporciona métodos para realizar operaciones como retirar dinero, transferir dinero desde otro usuario y agregar dinero al saldo. 

# Código a seguir:

    #1. Inicializar un usuario con su nombre, saldo y si tiene o no cuenta corriente mediante True y False .
    #2. Implementar el método retirar_dinero para retirar dinero del saldo del usuario. Lanzará un error en caso de no poder hacerse.
    #3. Implementar el método transferir_dinero para realizar una transferencia desde otro usuario al usuario actual. Lanzará un error en caso de no poder hacerse.
    #4. Implementar el método agregar_dinero para agregar dinero al saldo del usuario. 
    
class UsuarioBanco:
    
    def __init__(self, nombre, saldo, cuenta_corriente=True):  #<--- 1.
        self.nombre = nombre
        self.saldo = float(saldo)
        self.cuenta_corriente = cuenta_corriente

    def retirar_dinero(self, cantidad):  #<--- 2.
        
        if cantidad <= 0:
            
            raise ValueError("La cantidad a retirar debe ser positiva")
        
        if cantidad > self.saldo:
            
            raise ValueError("ERROR, no se puede retirar dinero, saldo insuficiente")
        
        self.saldo -= cantidad
        
        return f"{self.nombre} ha retirado {cantidad}. Saldo actual: {self.saldo}"

    def transferir_dinero(self, otro_usuario, cantidad):  #<--- 3.
        
        if cantidad <= 0:
           
            raise ValueError("La cantidad a transferir debe ser positiva")
       
        if cantidad > self.saldo:
       
            raise ValueError("ERROR, no se puede transferir dinero, saldo insuficiente")
        
        self.saldo -= cantidad
        otro_usuario.saldo += cantidad
        
        return f"{self.nombre} transfirió {cantidad} a {otro_usuario.nombre}. Saldo actual: {self.saldo}"

    def agregar_dinero(self, cantidad):  #<--- 4.
        
        if cantidad <= 0:
           
            raise ValueError("La cantidad a agregar debe ser positiva")
        
        self.saldo += cantidad
        
        return f"{self.nombre} ha ingresado {cantidad}. Saldo actual: {self.saldo}"


    # Caso de uso:

    #1. Crear dos usuarios: "Alicia" con saldo inicial de 100 y "Bob" con saldo inicial de 50, ambos con cuenta corriente.
    
    Alicia = UsuarioBanco("Alicia", 100, True)
    Bob = UsuarioBanco("Bob", 50, True)

    
    #2. Agregar 20 unidades de saldo de "Bob".
    
    Bob.agregar_dinero(20)

    
    #3. Hacer una transferencia de 80 unidades desde "Bob" a "Alicia".
    
    Bob.transferir_dinero(Alicia, 80)  # Salta el error de saldo insuficiente porque Bob solo tiene 70 y quiere transferir 80
    

    #4. Retirar 50 unidades de saldo a "Alicia".

    Alicia.retirar_dinero(50)



#37. Crea una función llamada procesar_texto que procesa un texto según la opción especificada: contar_palabras , reemplazar_palabras , eliminar_palabra . Estas opciones son otras funciones que tenemos que definir primero y llamar dentro de la función procesar_texto . 

# Código a seguir:
    
    #1. Crear una función contar_palabras para contar el número de veces que aparece cada palabra en el texto. Tiene que devolver un diccionario.
    #2. Crear una función reemplazar_palabras para remplazar una palabra_original del texto por una palabra_nueva . Tiene que devolver el texto con el remplazo de palabras.
    #3. Crear una función eliminar_palabra para eliminar una palabra del texto. Tiene que devolver el texto con la palabra eliminada.
    #4. Crear la función procesar_texto que tome un texto, una opción(entre "contar", "reemplazar", "eliminar") y un número de argumentos variable según la opción indicada. Caso de uso: Comprueba el funcionamiento completo de la función procesar_texto

def contar_palabras(texto):  #<--- 1.

    palabras = texto.split()
    resultado = {}

    for palabra in palabras:

        palabra = palabra.lower()

        if palabra not in resultado:

            resultado[palabra] = 0

        resultado[palabra] += 1

    return resultado


def reemplazar_palabras(texto, palabra_vieja, palabra_nueva):  #<--- 2.
    
    lista = texto.split()

    lista_mod = [palabra_nueva if p == palabra_vieja else p for p in lista]
    
    return " ".join(lista_mod)


def eliminar_palabra(texto, palabra):  #<--- 3.

    lista = texto.split()

    lista_mod = [p for p in lista if p != palabra]

    return " ".join(lista_mod)


def procesar_texto(texto, opcion, *args):  #<--- 4.

    if opcion == "contar":

        return contar_palabras(texto)
    
    elif opcion == "reemplazar":

        if len(args) != 2:
            
            return "Error: necesitas dos palabras para reemplazar"
        
        return reemplazar_palabras(texto, args[0], args[1])
    
    elif opcion == "eliminar":
        
        if len(args) != 1:
            
            return "Error: necesitas una palabra para eliminar"
        
        return eliminar_palabra(texto, args[0])
    
    else:
        
        return "Opción no válida. Usa 'contar', 'reemplazar' o 'eliminar'"



#38. Genera un programa que nos diga si es de noche, de día o tarde según la hora proporcionada por el usuario.

def determinar_momento_del_dia(hora):
    if 0<= hora < 6 or 20 <= hora <=23:
        return 'Noche'
    elif 6 <= hora < 12:
        return 'Día'
    elif 12<= hora < 20:
        return 'Tarde'
    else:
        return 'Hora no válida, recuerda introducir un número entre 0 y 23'



#39. Escribe un programa que determine qué calificación en texto tiene un alumno en base a su calificación numérica. 

# Las reglas de calificación son:
    
    #- 0 - 69 insuficiente
    #- 70 - 79 bien
    #- 80 - 89 muy bien
    #- 90 - 100 excelente

calificación = int(input("Escribe la calificación del alumno a continuación (0-100): "))

if calificación < 0 or calificación > 100:

    raise ValueError("ERROR, la calificación introducida está fuera de los parámetros establecidos (0-100)")

elif calificación < 70:
    
    print("Insuficiente")

elif calificación < 80:
    
    print("Bien")

elif calificación < 90:
    
    print("Muy bien")

else:
    
    print("Excelente")



#40. Escribe una función que tome dos parámetros: figura (una cadena que puede ser "rectangulo" , "circulo" o "triangulo" ) y datos (una tupla con los datos necesarios para calcular el área de la figura).

import math  # para poder calcular el área de un círculo, he necesitado buscar que librería me facilitaba hacerlo, en este caso la librería math

def calc_area(figura, datos):

    figura = figura.lower()

    if figura == "rectangulo":

        if len(datos) != 2:
            
            raise ValueError("El rectángulo necesita base y altura (2 valores).")
        
        base, altura = datos
        
        return base * altura
    
    elif figura == "circulo":
        
        if len(datos) != 1:
            
            raise ValueError("El círculo necesita solo el radio (1 valor).")
        
        radio = datos[0]
        
        return math.pi * (radio ** 2)
    
    elif figura == "triangulo":
        
        if len(datos) != 2:
            
            raise ValueError("El triángulo necesita base y altura (2 valores).")
        
        base, altura = datos
        
        return (base * altura) / 2
    
    else:
        
        raise ValueError("Figura no válida. Usa: 'rectangulo', 'circulo' o 'triangulo'.")



#41. En este ejercicio, se te pedirá que escribas un programa en Python que utilice condicionales para determinar el monto final de una compra en una tienda en línea, después de aplicar un descuento. El programa debe hacer lo siguiente:
    
    #1. Solicita al usuario que ingrese el precio original de un artículo.
    #2. Pregunta al usuario si tiene un cupón de descuento (respuesta sí o no).
    #3. Si el usuario responde que sí, solicita que ingrese el valor del cupón de descuento.
    #4. Aplica el descuento al precio original del artículo, siempre y cuando el valor del cupón sea válido (es decir, mayor a cero). Por ejemplo, descuento de 15€.
    #5. Muestra el precio final de la compra, teniendo en cuenta el descuento aplicado o sin él.
    #6. Recuerda utilizar estructuras de control de flujo como if, elif y else para llevar a cabo estas acciones en tu programa de Python.

def calcular_compra():

    precio = float(input("Introduce el precio original del artículo (€): "))
    
    tiene_cupon = input("¿Tienes un cupón de descuento? (si/no): ").lower()

    if tiene_cupon == "si":

        descuento = float(input("Introduce el valor del cupón (€): "))
        
        if descuento > 0 and descuento < precio:
            
            precio_final = precio - descuento
            
            print(f"El precio final con descuento es: {precio_final:.2f} €")
       
        else:
           
            print("El cupón no es válido, se mantiene el precio original.")
           
            print(f"Precio final: {precio:.2f} €")
    
    else:
       
        print(f"No se aplica descuento. Precio final: {precio:.2f} €")