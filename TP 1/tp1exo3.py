jour=0
heure=0
minute=0
T=0

print ("saisir le jour :" )
jour = int(input())

print ("saisir l'heure :" )
heure = int(input())

print ("saisir la minute :" )
minute = int(input())

T=(jour*24*60)+(heure*60)+minute

print (T)
