a = 0
b = 0
temp = 0
temp2 = 0
temp3 = 0

a = int(input("ENTREZ LA PREMIERE VALEUR POUR A : "))
b = int(input("ENTREZ LA DEUXIEME VALEUR POUR B : "))

temp2 = a
temp3 = b

temp = a
a = b 
b = temp

print("Avant permutation")
print("A : ",temp2)
print("B : ", temp3)

print("Après permutation")
print("A : ",a)
print("B : ", b)