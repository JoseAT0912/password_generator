import random

elementos = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"

size = int( input("Ingresa la longitud de la contraseña:") )

password = ""

for i in range( size ):
    password += random.choice(elementos)

print(password)