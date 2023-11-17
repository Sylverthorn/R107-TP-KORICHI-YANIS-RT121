N = int(input("ENTREZ LA FACTORIELLE A DETERMINER : "))
choix = int(input("Choisissez le type de boucle (1 = while / 2 = for)"))
while choix != 1 and choix != 2:
    choix = int(input("Choisissez le type de boucle (1 = while / 2 = for)"))

FACTO=1

if choix == 2:
   
    for i in range (1, N+1):
        FACTO = FACTO * (i)
        print(i, "x", FACTO/i, "=", FACTO)
    print(FACTO)

if choix == 1:

    while N > 1:
        N = N-1
        FACTO = N * (N-1)
        
    print(FACTO)



