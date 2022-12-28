def multiple(n,nMax):
    """
    Cette fonction permet de trouver tous les multiples de n et qui sont inférieurs à nMax
    Argument:
    n= le nombre choisit, type:entier
    nMax= le nombre maximum a ne pas dépasser, type:entier
    Return:
    listeFinalMultiple: la liste de tous les multiples de n inférieur à nMax, type:liste
    """
    listeInitial=[]
    m=0
    e=2
    listeFinalMultiple=[]
    while m<nMax:
            m=n*e
            e += 1
            if m<=nMax and m>n:
                listeFinalMultiple.append(m)
    return listeFinalMultiple

def diviseur(n,nMax):
    """
    Cette fonction permet de trouver tous les diviseurs de n
    Argument:
    n= le nombre choisit, type:entier
    nMax= type:entier
    Return:
    listeFinalDiviseu: la liste de tous les diviseurs de n, type:liste
    """
    e=1
    d=1
    listeInitial=[]
    listeFinalDiviseur=[]
    while e<n:
        d= n%e
        if d==0:
            listeFinalDiviseur.append(e)
        e +=1
    return listeFinalDiviseur

def union(liste1,liste2):
    """
    Cette fonction permet de fusionner deux listes.
    Argument:
    liste1: la première liste, type: liste
    liste2: la seconde liste, type:liste
    Return:
    listeInitial: la liste de la fusion de liste 1 et 2, type:liste
    """
    listeInitial=liste2+liste1
    return listeInitial

def filtreNumero1(M,R):
    """
    Cette fonction permet de récupérer les élements communs dans M et dans R
    Argument:
    M: la première liste, type:liste
    R: la seconde liste, type:liste
    Return:
    liste_filtree: la liste des éléments communs de M et de R ,type:liste
    """
    liste_filtree = []
    for i in range(len(M)):
        if M[i] in R:
            liste_filtree.append(M[i])
    return liste_filtree

def filtreNumero2(M,R):
    """
    Cette fonction permet de récupérer les élements de M qui ne sont pas dans R
    Argument:
    M: la première liste, type:liste
    R: la seconde liste, type:liste
    Return:
    liste_filtree: la liste des éléments présent dans M mais pas dans R ,type:liste
    """
    liste_filtree = []
    for i in range(len(M)):
        if M[i] not in R:
            liste_filtree.append(M[i])
    return liste_filtree

#Jeu
def jeuclement():
    trypassed = False
    while not trypassed:
        try:
            nMax= int(input("Choisir le nombre de valeur présent dans le jeu:"))  #On demande la taille maximale de la liste du jeu                                      
            trypassed = True
        except:
            print("Veuillez saisir un entier.") 
    FinDuJeu = False                                                      #On définit la variable FinDuJeu qui nous permettra d'arreter le jeu
    listeN=[]                                                             #On créé la liste des nombres déjà utilisés
    listeInitial=[]                                                       #On créé la liste initial qui contiendra les valeurs allant de 1 à nMax
    j=1                                                                   #On défini J
    listeModifie=[]                                                       #On créé la liste modifié qui contiendra la liste initial mais après le passage des fonctions
    NumeroJoueur=2                                                        #On établie la variable joueur qui nous permettra de savoir quuel joueur joue
    while j != nMax+1:                                                    #Ce While permet de remplir la liste initial de 1 à nMax
        listeInitial.append(j)
        j +=1
    print("Nombre valide: ",listeInitial)
    trypassed = False
    while not trypassed:
        try:
            n=int(input("Joueur 1 choisit un nombre pair:"))                                                                     #On fait jouer le 1er joueur une fois avant de lancer la boucle, pour avoir le premier élément
            trypassed = True
        except:
            print("Veuillez saisir un entier.")          
    if n%2==0:
        listeN.append(n)
    else:
        while n>nMax or n%2==1:                                           #Si le joueur ne choisit pas un nombre pair pour commencer ou que son nombre est supérieur à nMax, on lui demande en boucle de recommencer jusqu'à ce qu'il rentre un nombre pair inférieur à nMAx
            print("Le nombre choisit n'est pas pair ou il n'est pas compris dans la liste")
            trypassed = False
            while not trypassed:
                try:
                    n=int(input("Joueur 1 choisit un nombre pair: "))
                    trypassed = True
                except:
                    print("Veuillez saisir un entier.")
        listeN.append(n)



    while FinDuJeu == False:                                            #Le jeu débute
        if NumeroJoueur%2==0:                                               #Si le compteur est pair le joueur 2 joue
            listeModifie=filtreNumero2(filtreNumero1(listeInitial,(union(multiple(n,nMax),diviseur(n,nMax)))),listeN)   #On applique les fonctions
            print("Nombre valide:",listeModifie)
            trypassed = False
            while not trypassed:
                try:
                    n=int(input("Joueur 2 choisit : "))                                                                     #Le joueur chosit son nombre présent dans la liste modifié
                    trypassed = True
                except:
                    print("Veuillez saisir un entier.")
            listeN.append(n)                                                                                            #On ajoute le nombre choisit à la liste des nombres déjà utilisés
            NumeroJoueur+=1                                                                                             #on ajoute 1 au compteur car le joueur vient de joueur
        if filtreNumero2(filtreNumero1(listeInitial,(union(multiple(n,nMax),diviseur(n,nMax)))),listeN)==[]:            #On vérifie ,qu'après avoir sélectionné son nombre, qu'il y est encore des nombres présent dans la liste, s'il y en a encore le jeu continue, à l'inverse le jeu s'arrete
                FinDuJeu = True
        elif NumeroJoueur%2==1:                                             #Compteur impair, le joueur 1 joue
            listeModifie=filtreNumero2(filtreNumero1(listeInitial,(union(multiple(n,nMax),diviseur(n,nMax)))),listeN)   #On applique les fonctions
            print("Nombre valide:",listeModifie)
            trypassed = False
            while not trypassed:
                try:
                    n=int(input("Joueur 1 choisit : "))                                                                     #Le joueur chosit son nombre présent dans la liste modifié
                    trypassed = True
                except:
                    print("Veuillez saisir un entier.")
            listeN.append(n)                                                                                            #On ajoute le nombre choisit à la liste des nombres déjà utilisés
            NumeroJoueur+=1                                                                                             #on ajoute 1 au compteur car le joueur vient de joueur
        if filtreNumero2(filtreNumero1(listeInitial,(union(multiple(n,nMax),diviseur(n,nMax)))),listeN)==[]:            #On vérifie ,qu'après avoir sélectionné son nombre, qu'il y est encore des nombres présent dans la liste, s'il y en a encore le jeu continue, à l'inverse le jeu s'arrete
            FinDuJeu = True
    if NumeroJoueur%2==0:                       #Quand le jeu est fini, si le compteur est pair, le joueur 1 a gagné
        print("Victoire du joueur 1")
    if NumeroJoueur%2==1:                       #Si le compteur est impair, le joueur 2 a gagné
        print("Victoire du joueur 2")


