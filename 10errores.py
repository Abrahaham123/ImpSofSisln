# Errores básicos en Python y cómo solucionarlos

# 1. SyntaxError: EOL while scanning string literal
# ERROR:
# mensaje = "Hola mundo
# SOLUCIÓN:
mensaje = "Hola mundo"

# 2. NameError: name 'variable' is not defined
# ERROR:
# print(variable)
# SOLUCIÓN:
variable = 5
print(variable)

# 3. IndentationError: unexpected indent
# ERROR:
# def saludar():
#       print("Hola")  # Indentación incorrecta
# SOLUCIÓN:
def saludar():
    print("Hola")

# 4. TypeError: can only concatenate str (not "int") to str
# ERROR:
# edad = 20
# print("Tienes " + edad + " años")
# SOLUCIÓN:
edad = 20
print("Tienes " + str(edad) + " años")

# 5. ZeroDivisionError: division by zero
# ERROR:
# resultado = 10 / 0
# SOLUCIÓN:
divisor = 0
if divisor != 0:
    resultado = 10 / divisor
else:
    print("No se puede dividir entre cero")

# 6. IndexError: list index out of range
# ERROR:
# lista = [1, 2, 3]
# print(lista[5])
# SOLUCIÓN:
lista = [1, 2, 3]
if 5 < len(lista):
    print(lista[5])
else:
    print("Índice fuera de rango")

# 7. KeyError en diccionarios
# ERROR:
# persona = {"nombre": "Cami"}
# print(persona["edad"])
# SOLUCIÓN:
persona = {"nombre": "Cami"}
print(persona.get("edad", "Edad no registrada"))

# 8. AttributeError: 'int' object has no attribute 'append'
# ERROR:
# numero = 5
# numero.append(2)
# SOLUCIÓN:
lista = []
lista.append(2)

# 9. ModuleNotFoundError
# ERROR:
# import mathh  # mal escrito
# SOLUCIÓN:
import math
print(math.sqrt(16))

# 10. ValueError: invalid literal for int() with base 10
# ERROR:
# numero = int("diez")
# SOLUCIÓN:
entrada = "10"
if entrada.isdigit():
    numero = int(entrada)
    print("Número convertido:", numero)
else:
    print("Entrada no válida para conversión a entero")
