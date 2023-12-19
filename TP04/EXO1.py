N = float(input("ENTREZ LA VALEURS A CALCULER : "))
T = [None] * 10


for i in range(0, 10):
    T[i] = N * i
    print(N ,"x", i,"=", round(T[i] , 10) )




