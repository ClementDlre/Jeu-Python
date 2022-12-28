from random import *
from time import sleep

def position_tresor():
    """
    Ce programme nous permet de créer la position du trésor.
    Return : La position du trésor en x et la position du trésor en y.
    
    Cette fonction n'est pas testable car elle renvoie une valeur aléatoire.
    """
    tresor_x = randint(1,100)       # On prend un e valeur aléatoire entre 1 et 100 pour x et y, ce sera la position du coffre. 
    tresor_y = randint(1,100)
    return tresor_x,tresor_y

def creationtableau():
    """
    Ce programme permet de créer un tableau qui servira pour le graphisme de la carte.
    Return : Tableau ne contenant que des espaces dans chacune des cases.
    
    Cette fonction n'est pas testable car le tableau fait trop de mal à l'IDE.
    """
    tab = []
    for i in range (102):
        tab.append([])
        for _ in range(102):
            tab[i].append("  ")
    return tab

def rendugraphique(tab):
    """
    Ce programme permet d'afficher le tableau créer dans "creation tableau" sur une carte.
    
    Cette fonction n'est pas testable car elle ne fait qu'afficher la carte, elle ne renvoie rien. 
    """
    print(206*"-")                     
    for i in range(len(tab)): # On traverse le tableau ligne par ligne pour renvoyer à chaque fois les valeurs comprisent dans celui-ci. 
        texte = "|"
        for j in tab[-i-1]:   # On renvoie chaque caractère du tableau sur une chaîne de caractère "texte" qui est reinitialisée à chaque passage de ligne. 
            texte+=j
        print(texte+"|")
    print(206*"-") 

def changement(tab,x,y,x1,y1):
    """
    Ce tableau permet de mettre une croix dans le tableau pour chaque essais effectués par le joueur, et il permet aussi de créer un chemin entre chaque croix.
    Return : Tableau modifié avec les nouvelles valeurs.
    
    Cette fonction n'est pas testable car elle ne fait que de l'affichage aussi, et renvoyer le tableau entier ferait encore une fois trop de mal à l'IDE. 
    """
    xchange = False
    tab[y-1][x] = "--" #Ces variables permettent de créer une croix sur la carte.
    tab[y][x] = "><"
    tab[y+1][x] = "--"
    tab[y-1][x-1] = "*-"
    tab[y+1][x+1] = "-*"
    tab[y-1][x+1] = "-*"
    tab[y+1][x-1] = "*-"
    tab[y][x-1] = "| "
    tab[y][x+1] = " |"
    if x1 != 0:        #Ces variables permettent de créer un tracé sur la carte entre chaque point. 
        if x1 != x:
            if x1 > x:
                x,x1=x1,x
                xchange = True
            for routex in range(x1+1,x):
                tab[y1][routex] = "--"
    if y1 != 0:
        if y1 != y:
            if y1 > y:
                y,y1=y1,y
            if xchange:
                for routey in range(y1+1,y):
                    tab[routey][x1] = "| "
            else:
                for routey in range(y1+1,y):
                    tab[routey][x] = "| "
    return tab

def chasse_au_tresor():
    """
    Ce programme est le jeu de chasse au trésor joué par un joueur.
    """
    tab = creationtableau()       # On crée le tableau vide
    p_tresor = position_tresor()  # On crée les coordonnées du trésor
    coffre_x = False              # La variable coffre_x nous permettra de définir si la position x du trésor a été trouvé ou non, nous la définissons donc a False, car le coffre n'a pas été trouvé. 
    coffre_y = False              # La variable coffre_y nous permettra de définir si la position y du trésor a été trouvé ou non, nous la définissons donc a False, car le coffre n'a pas été trouvé. 
    x1,y1 = 0,0                   # Ces variable nous permet de contenir la précédente réponse de l'utilisateur, cela nous servira pour construire les chemins sur la carte.
    while coffre_x == False or coffre_y == False:   # Tant que les coffres n'ont pas été trouvé, l'utilisateur continue de jouer.
        choix_x = 101
        choix_y = 101
        trypassedx = False
        while not trypassedx:                       # Ce while nous permet de nous protéger d'éventuelles erreurs, par exemple, si l'utilisateur entre une lettre en réponse.
            try:
                while choix_x < 1 or choix_x > 100: # Ce while nous permet de forcer à l'utilisateur d'entrer une valeur entre 1 et 100. 
                    if coffre_x == False:
                        if coffre_y == True:
                            choix_y = p_tresor[1]
                        print("Veuillez choisir une valeur entre 1 et 100 pour x")
                        print("Quel valeur choissez vous pour x ?")
                        choix_x = int(input(""))
                trypassedx = True
            except:
                print("Veuillez entrer un nombre.")
        trypassedy = False
        while not trypassedy:                       # Ce while nous permet de nous protéger d'éventuelles erreurs, par exemple, si l'utilisateur entre une lettre en réponse.
            try:
                while choix_y < 1 or choix_y > 100: # Ce while nous permet de forcer à l'utilisateur d'entrer une valeur entre 1 et 100. 
                    if coffre_y == False:
                        if coffre_x == True:      
                            choix_x = p_tresor[0]
                        print("Veuillez choisir une valeur entre 1 et 100 pour y")
                        print("Quel valeur choissez vous pour y ?")
                        choix_y = int(input(""))
                trypassedy = True
            except:
                print("Veuillez entre un nombre.")
        tab = changement(tab,choix_x,choix_y,x1,y1)  # Nous actualisons la carte.
        rendugraphique(tab)                          # Nous affichons la carte.
        if p_tresor[0] > choix_x:        # Si le coffre est à gauche, alors nous indiquerons à l'utilisateur qu'il est à l'Est, ainsi de suite avec chacune des possibilités.
            repx = "Est"
        elif p_tresor[0] < choix_x:
            repx = "Ouest"
        else:                       # Si la coordonnée x d'un coffre a été trouvé, alors nous arrêtons de lui demander la valeur, et la valeur coffre_x est donc mise à True.
            repx = ""
            coffre_x = True
        if p_tresor[1] > choix_y:
            repy = "Nord"
        elif p_tresor[1] < choix_y:
            repy = "Sud"
        else:                       # Si la coordonnée y d'un coffre a été trouvé, alors nous arrêtons de lui demander la valeur, et la valeur coffre_y est donc mise à True.
            repx = ""
            coffre_y = True
        if not coffre_x or not coffre_y:  # Tant que la coordonnée x ou la coordonnée y n'a pas été trouvé, nous indiquons dans quelle direction se situe le coffre.
            print("Le coffre se situe vers le",repy,repx,"!")
        x1 = choix_x
        y1 = choix_y
        if coffre_x and coffre_y:         # Si le coffre a été trouvé, nous affichons un dessin de coffre ainsi qu'un message de félicitations. 
            print("                             _.--.","\n","                        _.-'_:-'||","\n","                    _.-'_.-::::'||","\n","               _.-:'_.-::::::'  ||","\n","             .'`-.-:::::::'     ||","\n","            /.'`;|:::::::'      ||_","\n","           ||   ||::::::'     _.;._'-._","\n","           ||   ||:::::'  _.-!oo @.!-._'-.","\n","            \'.  ||:::::.-!()oo @!()@.-'_.|","\n",r"            '.'-;|:.-'.&$@.& ()$%-'o.'\U||","\n","              `>'-.!@%()@'@_%-'_.-o _.|'||","\n","               ||-._'-.@.-'_.-' _.-o  |'||","\n",r"               ||=[ '-._.-\U/.-'    o |'||","\n","               || '-.]=|| |'|      o  |'||","\n","               ||      || |'|        _| ';","\n","               ||      || |'|    _.-'_.-'","\n","               |'-._   || |'|_.-'_.-'","\n","                '-._'-.|| |' `_.-'","\n","                    '-.||_/.-'","\n\n\n")
            print("Félicitations, vous avez trouvé le coffre !")



def chasse_au_tresor_ordinateur():
    """
    Ce programme est le jeu de chasse au trésor joué par l'ordinateur.
    
    Le programme est réalisé de la même manière que le précédent, nous avons juste ajouté un système de dichotomie pour qu'il puisse résoudre le programme seul.
    """
    tab = creationtableau()
    p_tresor = position_tresor()
    coffre_x = False
    coffre_y = False
    x1 = 0
    y1 = 0
    ax,ay,bx,by = 1,1,100,100   # On définit nos variables de dichotomie, les variables aX seront les variables minimales et les variables bX seront les variables maximales.
    while coffre_x == False or coffre_y == False:
        if not coffre_x:
            choix_x = (ax+bx) // 2             # Tant que le coffre n'est pas trouvé alors l'ordinateur continue de modifier les variables et de chercher
        if not coffre_y:
            choix_y = (ay+by) // 2
        tab = changement(tab,choix_x,choix_y,x1,y1)
        rendugraphique(tab)
        if p_tresor[0] > choix_x:              # Si la position du coffre est à l'Est de celle devinée, alors la valeur minimale sur la coordonnée x est changée à la valeur choisie dernièrement pour x
            repx = "Est"
            ax = choix_x
        elif p_tresor[0] < choix_x:            # Si la position du coffre est à l'Ouest de celle devinée, alors la valeur minimale sur la coordonnée x est changée à la valeur choisie dernièrement pour x
            repx = "Ouest"
            bx = choix_x
        else:                                  # Si la position du coffre est trouvée alors on arrête de la demander
            repx = ""
            coffre_x = True
        if p_tresor[1] > choix_y:              # Si la position du coffre est au Nord de celle devinée, alors la valeur minimale sur la coordonnée y est changée à la valeur choisie dernièrement pour y
            repy = "Nord"
            ay = choix_y
        elif p_tresor[1] < choix_y:            # Si la position du coffre est au Sud de celle devinée, alors la valeur minimale sur la coordonnée y est changée à la valeur choisie dernièrement pour y
            repy = "Sud"
            by = choix_y
        else:                                  # Si la position du coffre est trouvée alors on arrête de la demander
            repx = ""
            coffre_y = True
        if not coffre_x or not coffre_y:
            print("Le coffre se situe vers le",repy,repx,"!")
        x1 = choix_x
        y1 = choix_y
        if coffre_x and coffre_y:
            print("                             _.--.","\n","                        _.-'_:-'||","\n","                    _.-'_.-::::'||","\n","               _.-:'_.-::::::'  ||","\n","             .'`-.-:::::::'     ||","\n","            /.'`;|:::::::'      ||_","\n","           ||   ||::::::'     _.;._'-._","\n","           ||   ||:::::'  _.-!oo @.!-._'-.","\n","            \'.  ||:::::.-!()oo @!()@.-'_.|","\n",r"            '.'-;|:.-'.&$@.& ()$%-'o.'\U||","\n","              `>'-.!@%()@'@_%-'_.-o _.|'||","\n","               ||-._'-.@.-'_.-' _.-o  |'||","\n",r"               ||=[ '-._.-\U/.-'    o |'||","\n","               || '-.]=|| |'|      o  |'||","\n","               ||      || |'|        _| ';","\n","               ||      || |'|    _.-'_.-'","\n","               |'-._   || |'|_.-'_.-'","\n","                '-._'-.|| |' `_.-'","\n","                    '-.||_/.-'","\n\n\n")
            print("L'ordinateur a trouvé le coffre !")
        sleep(3)


