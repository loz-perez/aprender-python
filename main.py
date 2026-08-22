# main.py
# Tu primer programa en Python.
# Para correrlo: abrí este archivo en VS Code y apretá el botón "Run" (▶) arriba a la derecha,
# o desde la terminal integrada escribí: python3 main.py

# 1. Esto imprime texto en la pantalla.
print("¡Hola, Lorenzo!")
print("Este es tu primer programa en Python.")

# 2. Una variable guarda un valor para usarlo después.
nombre = "Lorenzo"
edad = 25  # <- cambiá este número por tu edad real

print("Te llamás " + nombre + " y tenés " + str(edad) + " años.")

# 3. Podés pedirle algo al usuario y guardarlo en una variable.
ciudad = input("¿En qué ciudad estás? ")
print("¡" + ciudad + " suena bien!")

# 4. Un condicional (if) permite que el programa decida qué hacer.
if edad >= 18:
    print("Sos mayor de edad.")
else:
    print("Sos menor de edad.")

# 5. Un loop (for) repite algo varias veces.
print("Contando del 1 al 5:")
for numero in range(1, 6):
    print(numero)

# 6. Una función agrupa código para reutilizarlo.
def saludar(persona):
    return "¡Hola, " + persona + "! Bienvenido/a a programar."

print(saludar(nombre))


# ---------------------------------------------------------
# EJERCICIOS PARA VOS (descomentá y completá cada uno)
# ---------------------------------------------------------

# Ejercicio 1: Creá una variable "color_favorito" con tu color favorito
# y hacé un print que diga "Mi color favorito es <color>".
color_favorito = "azul"
print("Mi color favorito es", color_favorito)

# Ejercicio 2: Pedile al usuario dos números con input() y sumalos.
# Ojo: input() siempre devuelve texto, hay que convertirlo con int().
numero1 = int(input("Ingresá un número: "))
numero2 = int(input("Ingresá otro número: "))
print("La suma es:", numero1 + numero2)

# Ejercicio 3: Escribí una función llamada "es_par" que reciba un número
# y devuelva True si es par y False si es impar (pista: usá el operador %).
def es_par(numero):
    return numero % 2 == 0

# Ejercicio 4: Usando un for, imprimí la tabla del 5 (5x1, 5x2, ... 5x10).
for i in range(1, 11):
    print(f"5 x {i} = {5 * i}")q
