from random import *
def nombre_mystere():
    x = randint(1,1000)  # On choisit une valeur aléatoire entre 1 et 1000 pour le juste prix
    nbre_reponses=0      # On définit le nombre de réponse du joueur à 0
    while nbre_reponses < 10:  # Tant que le joueur n'a pas répondu plus de 10 fois alors il continue de jouer
        trypassed = False
        while not trypassed:   # Tant que le joueur n'a pas rendu une réponse valable, on le fait réessayer
            rep = 1001
            try:
                while rep < 1 or rep > 1000:
                    rep=int(input("Veuillez saisir un entier entre 1 et 1000 : ")) 
                nbre_reponses +=1
                trypassed = True
            except:
                print("Veuillez saisir un nombre entre 1 et 1000.")
        if rep<x:  # Si le nombre répondu est trop petit, alors on lui renvoie que le nombre saisi est trop petit
            print ("le nombre saisi est trop petit.")
        elif rep>x:  # Si le nombre répondu est trop grand, alors on lui renvoie que le nombre saisi est trop petit
            print("Le nombre saisi est trop grand.")
        elif rep==x: # S'il a trouvé la réponse, alors on renvoie "Juste prix !!" , on lui donne son nombre de tentatives, et on arrête le programme. 
            print("Juste prix !!")
            print("Vous avez trouvé le juste prix en",nbre_reponses,"réponses.")
            break
    if rep!=x:   # Si le joueur n'a pas trouvé le juste prix au bout de 10 tentatives, alors on lui dis qu'il a échoué. 
        print("Vous avez échoué...")



def justeprix():
    n = 1000 # Prix maximum de l'article 
    justeprix = randint(1,n) # On choisit un prix entre 1€ et 1000€ 
    a, b = 1, n # a et b seront les bornes de notre ensemble 
    nbre_reponses = 0 # Compteur de reponses   
    while b-a > 1: #
        rep = (a+b)//2 #On  fait une dichotomie 
        nbre_reponses += 1 # On inremente le compteur
        if nbre_reponses > 10: # Le compteur depasse les 10 essais donc on arrete la boucle et on retourne vous ave echoué
            print("Vous avez echoué")
            break
        print (rep) # On extrait les reponses obtenu grace à la dichotomie 
        if  rep == justeprix: 
            print("Le juste prix est :", rep) # Si l'ordinateur trouve le bon prix on affiche le juste prix et le nombre de reponses 
            print("Le nombre de reponses est de :", nbre_reponses)
            break
        elif rep > justeprix: # on change les bornes, ici la borne inférieur
            b = rep
        else: # et ici la borne supérieur 
            a = rep
    if  b-a <= 1: #Ici on affiche les resultats, si la borne inferieur est le juste prix ou la borne superieur est le juste prix 
        if  justeprix == a:
            print("Le juste prix est :", a)
        else:
            print("Le juste prix est :", b)

