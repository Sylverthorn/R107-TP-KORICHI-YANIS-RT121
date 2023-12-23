L1 = [2, 55, 7, 55, 36, 7, 21, 56, 55, 3, 7, 6,2, 55, 7, 55, 36, 7, 21, 56, 55, 3, 7, 6,2, 55, 7, 55, 36, 7, 21, 56, 55, 3, 7, 6,2, 55, 7, 55, 36, 7, 21, 56, 55, 3, 7, 6,2, 55, 7, 55, 36, 7, 21, 56, 55, 3, 7]


occurence = {}
print (occurence)
for i in  L1:
    print (i)
    if i in occurence:
        occurence[i] += 1
    else :
        occurence[i] = 1
print(occurence)
maximal = max(occurence.values())



nombre = [k for k, values in occurence.items() if values == maximal ]

print(f"Le nombre le plus frequent dans la liste est le : {nombre} ({maximal} x)")







""" ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** *
* Ne rien modifier apres cette ligne.
** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** * /
"""
