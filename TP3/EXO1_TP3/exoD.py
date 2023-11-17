N = int(input("ENTREZ UN NOMBRE: "))
a = 0
c = 0
while N <= 1:
     N = int(input("VALEUR NON PRISE EN CHARGE, ENTREZ UN NOMBRE: "))

while c < N:
    a += 1
    c += a
    
print ( a)
