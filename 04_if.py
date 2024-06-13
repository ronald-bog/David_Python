# *****   if  ********

if 5 > 2:
    print("la condicion es verdadera - IF")

# *****   if - else  ********

if 1 > 2:
    print("la condicion es verdadera - if - else")
else:
    print("la condicion es falsa - if - else")

# Expresion ternaria

miVariable = "la condicion es verdadera ET" if 1 > 2 else "la condicion es falsa ET"
# JS 1 > 2 ? "la condicion es verdadera ET" : "la condicion es falsa ET"
print(miVariable)

# if - elif

color = "azul"

if color == "amarillo":
    print('La variable "color" tiene asignado: amarillo')
elif color == "rojo":
    print('La variable "color" tiene asignado: rojo')
else:
    print('La variable "color" tiene asignado un color diferente a rojo o amarillo')

# caso especial
color = "amarillo"
if color == "amarillo":
    print('La variable "color" tiene asignado: amarillo')
if color == "azul":
    print('La variable "color" tiene asignado: azul')
elif color == "rojo":
    print('La variable "color" tiene asignado: rojo')
else:
    print('La variable "color" tiene asignado un color diferente a rojo o amarillo')

# if anidado

miVariable = "framework"
variableAnidada = "Python"

if miVariable == "lenguaje":
    if variableAnidada == "Python":
        print(f"El lenguaje es {variableAnidada}")
    else:
        print(f"{variableAnidada} No es un lenguaje")
elif miVariable == "framework":
    if variableAnidada == "Django":
        print(f"El framework es {variableAnidada}")
    else:
        print(f"{variableAnidada} No es un framework")
