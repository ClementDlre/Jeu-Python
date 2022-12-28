#Exercice 2 :

def jeu_des_allumettes():
    """
    Ce programme est le jeu des allumettes où deux joueurs rivalisent, le dernier à piocher une allumettes sera le perdant.
    
    Pas de return car ce n'est que de l'affichage, le programme ne renvoie rien. 
    """
    allumettesrestantes = 21      # On définit le nombre d'allumettes restantes à 21.
    TourJoueur1 = True            # On définit cette variable permettant de savoir si c'est le tour du joueur 1 ou du joueur 2.
    while allumettesrestantes > 0:  # Tant qu'il reste des allumettes, le jeu continue de se jouer. 
        print("Il reste",allumettesrestantes,"allumettes :")       # Affiche le nombre d'allumettes restantes
        allumettesgraphique = '.'*allumettesrestantes + '\n' + '|'*allumettesrestantes  # Cette variable correspond à l'affichage des allumettes
        print(allumettesgraphique)
        if TourJoueur1 == True:   # Si c'est le tour du joueur 1, alors on lui demande de jouer
            print("C'est le tour du joueur 1 : ")
            trypassed = False
            while not trypassed: # Tant qu'il n'entre pas un chiffre entre 1, 2, ou 3 alors on lui demande d'entrer un chiffre entre 1, 2, ou 3
                try:
                    choix = int(input("Souhaitez vous enlever 1, 2, ou 3 allumettes ?"))
                    while choix != 1 and choix != 2 and choix != 3:
                        print("Veuillez sélectionner 1, 2, ou 3 allumettes.")
                        choix = int(input("Souhaitez vous enlever 1, 2, ou 3 allumettes ?"))
                    trypassed = True
                except:
                    print("Veuillez saisir un chiffre entre 1 et 3.")
            allumettesrestantes -= choix # On enlève des allumettes restantes les allumettes qui ont été enlevé par le joueur 1. 
            TourJoueur1 = False
        else:                    # Si c'est le tour du joueur 2, alors on lui demande de jouer
            print("C'est le tour du joueur 2 : ")
            trypassed = False
            while not trypassed: # Tant qu'il n'entre pas un chiffre entre 1, 2, ou 3 alors on lui demande d'entrer un chiffre entre 1, 2, ou 3
                try:
                    choix = int(input("Souhaitez vous enlever 1, 2, ou 3 allumettes ?"))
                    while choix != 1 and choix != 2 and choix != 3:
                        print("Veuillez sélectionner 1,2, ou 3 allumettes.")
                        choix = int(input("Souhaitez vous enlever 1, 2, ou 3 allumettes ?"))
                    trypassed = True
                except:
                    print("Veuillez saisir un chiffre entre 1 et 3.")
            allumettesrestantes -= choix # On enlève des allumettes restantes les allumettes qui ont été enlevé par le joueur 1. 
            TourJoueur1 = True
    print("Il n'y a plus d'allumettes !") # Dès que l'on sort du while, alors il n'y a plus d'allumettes, on renvoie donc ceci
    if TourJoueur1 == True:    # Si c'est le dernier joueur était le joueur 2, alors on renvoie le joueur 1 a gagné
        print("Le joueur 1 a gagné !")
    else:                      # Si c'est le dernier joueur était le joueur 1, alors on renvoie le joueur 2 a gagné
        print("Le joueur 2 a gagné !")

def jeu_des_allumettes_ordinateur():
    """
    Ce programme permet de jouer contre un ordinateur au jeu des allumettes.
    
    Pas de return non plus car il n'y a que de l'affichage.
    """
    allumettesrestantes = 21      # On définit le nombre d'allumettes restantes à 21.
    TourJoueur = True             # On définit cette variable permettant de savoir si c'est le tour du joueur ou de l'ordinateur
    while allumettesrestantes > 0:  # Tant qu'il reste des allumettes, le jeu continue de se jouer. 
        allumettesgraphique = '.'*allumettesrestantes + '\n' + '|'*allumettesrestantes  # Cette variable correspond à l'affichage des allumettes
        print(allumettesgraphique)
        if TourJoueur == True:   # Si c'est le tour du joueur, alors on lui demande de jouer
            print("C'est le tour du joueur 1 : ")
            trypassed = False
            while not trypassed: # Tant qu'il n'entre pas un chiffre entre 1, 2, ou 3 alors on lui demande d'entrer un chiffre entre 1, 2, ou 3
                try:
                    choix = int(input("Souhaitez vous enlever 1, 2, ou 3 allumettes ?"))
                    while choix != 1 and choix != 2 and choix != 3:
                        print("Veuillez sélectionner 1,2, ou 3 allumettes.")
                        choix = int(input("Souhaitez vous enlever 1, 2, ou 3 allumettes ?"))
                    trypassed = True
                except:
                    print("Veuillez saisir un chiffre entre 1 et 3.")
            TourJoueur = False
            allumettesrestantes -= choix # On enlève des allumettes restantes les allumettes qui ont été enlevé par le joueur. 
        else:                    # Si c'est le tour de l'ordinateur, alors on lui demande de jouer
            print("C'est le tour de l'ordinateur : ")
            choix = (allumettesrestantes%3)-1  # Cet ligne permet à l'ordinateur de ne prendre la/les dernière(s) allumette(s) que lorsqu'il n'a pas le choix
            if choix <= 0:
                choix += 3
            if choix >= allumettesrestantes:
                choix = allumettesrestantes
            allumettesrestantes -= choix        # On enlève des allumettes restantes les allumettes qui ont été enlevé par l'ordinateur. 
            print("L'ordinateur a enlevé",choix,"allumette(s).")
            TourJoueur = True
    print("Il n'y a plus d'allumette !")  # Dès que l'on sort du while, alors il n'y a plus d'allumettes, on renvoie donc ceci
    if TourJoueur == True:   # Si c'est le dernier joueur était l'ordinateur, alors on renvoie le joueur a gagné
        print("Le joueur a gagné !")
    else:                    # Si c'est le dernier joueur était le joueur, alors on renvoie l'ordinateur a gagné
        print("L'ordinateur a gagné !")

