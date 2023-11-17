
inferieur10 = 0
supérieur10 = 0
supérieur15 = 0


for i in range (0, 11):
    N = int(input("ENTREZ UN NOMBRE: "))
    while N < 0 or N > 20:
        N = int(input("VALEUR NON PRISE EN CHARGE, ENTREZ UN NOMBRE: "))
    if N < 10 :
        inferieur10 += 1
    elif N >= 10 and N < 15:
        supérieur10 +=1
    else:
        supérieur15 += 1

print ("il y a,", inferieur10, "valeurs inférieur à 10")
print ("il y a,", supérieur10, "valeurs supérieur à 10")
print ("il y a,", supérieur15, "valeurs supérieur à 15")

