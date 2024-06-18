# METODOS DE LOS STRINGS

# upper
palabra = "hola mundo"
# pabrabraM = palabra.upper()
print(palabra.upper())

# lower
palabraMi = "DAVID"
print(palabraMi.lower())

# capitalize
cap = "carlos"
print(cap.capitalize())

# title
titulo = "david silva"
print(titulo.title())

# strip
espacios = "   python  "
print(espacios)
print(espacios.strip())

# split
nombre = "Laura Lopez"
print(nombre.split())

numeros = "uno-dos-tres"
print(numeros.split("-"))

# replace
saludo = "hola mundo"
print(saludo.replace("mundo", "Python"))

# find
oracion = "Python es dinamico"
print(oracion.find("es"))

# join *Metodo propio de las listas []
lista = ["hola", "David"]
print("&".join(lista))

# indices, empiezan desde 0
cadena = "Computador"
print(cadena[5])


