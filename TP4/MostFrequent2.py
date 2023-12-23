L1 = [2, 55, 7, 55, 36, 7, 21, 56, 55, 3, 2, 6,2, 55, 7, 55, 36, 7, 21, 56, 55, 3, 7, 6,2, 55, 7, 55, 36, 7, 21, 56, 55, 3, 7, 6,2, 55, 7, 55, 36, 7, 21, 56, 55, 3, 7, 6,2, 55, 7, 55, 36, 7, 21, 56, 55, 3, 7]


occurence = [0] * len(L1)
print (occurence)
for i in  L1:
    occurence[i] = L1.count(i)
print(occurence)


maximal = max(occurence)



nombre = occurence.index(maximal)

print(f"Le nombre le plus frequent dans la liste est le : {nombre} ({maximal} x)")







""" ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** *
* Ne rien modifier apres cette ligne.
** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** * /
"""
