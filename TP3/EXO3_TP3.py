import random

N = int(input("ENTREZ UN NOMBRE: "))
R = random.randint(1,100)
T=0

while N != R:
    if N < R:
        N = int(input("PLUS GRAND, ENTREZ UN NOMBRE: "))
        T +=1
    else:
        N = int(input("PLUS PETIT, ENTREZ UN NOMBRE: "))
        T +=1

print ("BRAVO ! Vous avez trouvé ", R, "en", T, "essais")
    