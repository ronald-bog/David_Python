# Operadores Aritmeticos + - * / % // **
print(10 / 3)

# Operadores de comparacion: == != >= > < <=
print(1 > 2)
print(5 + 7 > 8 / 2)

# Operadores de Asignacion
# Asignacion =
# Suma y asignacion +=
# Resta y asignacion -=
# *=
# /=
valor = 10
# valor = valor + 20
valor += 20
print(valor)

# Operadores Logicos, devuelven bool
# and: True solo cuando todas las expresiones son True
# or: False solo cuando todas las expresiones son False
# not: cambiar el valor bool ej: False y le paso not me la coniverte en True

print("*****************")
print(5 < 10 and 20 == 20 and 1 == 1)
print(19 > 10 or 5 < 7)
print(not 2)

print("*****************")
# Operadores de pertenencia in, not in
palabra = "Hola"
print("i" not in palabra)

print("*****************")
# Truthy y Falsy
print(bool(0))
print(bool(""))
print(bool(False))
print(bool([]))
print(bool({}))
print(bool(None))
print(bool(()))
print(bool(set()))

