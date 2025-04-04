import random 

#cadena de signos 
character = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"

l1 = int(input("de cuantos dijitos quieres tu contraseña"))
contra = ""

#codigo para almacenar
for n in range (l1):
    contra += random.choice(character)


print("Tu contraseña generada es:", contra)
