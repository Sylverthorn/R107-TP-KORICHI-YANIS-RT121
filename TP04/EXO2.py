nombreEtudiants = int(input("Donnez le nombre d'etudiants : "))
T = []
S =0


for i in range (0 , nombreEtudiants):
    note = float(input("ENTREZ LA NOTE DE L'ETUDIANT {} : " .format(i+1)))
    while note > 20 or note <0 :
        note = float(input("VALEURS NON PRIS EN CHARGE ENTREZ LA NOTE : "))
    T.append(note)
    

M = sum(T)/nombreEtudiants
print ("Moyenne : ", M)

print ("NUMERO DE L'ETUDIANT | NOTE | ECART A LA MOYENNE"  )
for i in range (0 , nombreEtudiants):
    print( i+1 , " | ", T[i], "|" , T[i] - M)



    