BASE = 4
fromage = 800.0
eau = 2
ail = 2
pain = 400

nbconvive = int(input("ENTREZ LE NOMBRES DE CONVIVES : "))

fromage = fromage * nbconvive / BASE
eau = eau * nbconvive / BASE
ail = ail * nbconvive / BASE
pain = pain * nbconvive / BASE

print ("Pour faire une fondue fribourgeoise pour 3 personnes, il vous faut :")
print ("- ", fromage, "gr de fromage")
print ("- ", eau, "dl d'eau")
print ("- ", ail, "gousse(s) d'ail")
print ("- ", pain, "gr de pain")