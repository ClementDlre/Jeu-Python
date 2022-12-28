import Exercice_1
import Exercice_2
import Exercice_3
import Exercice_4

import tkinter as tk
from tkinter import ttk
from random import randint

fenetrejeu1 = False
fenetrejeu2 = False
fenetrejeu4 = False

class HoverButton(tk.Button):                 # On définit la classe HoverButton pour que le bouton change de couleur lorsque nous passons notre curseur par dessus. 
    def __init__(self, master, **kw):
        tk.Button.__init__(self,master=master,**kw)
        self.defaultBackground = self["background"]
        self.bind("<Enter>", self.on_enter)
        self.bind("<Leave>", self.on_leave)

    def on_enter(self, e):
        self['background'] = 'gray'

    def on_leave(self, e):
        self['background'] = self.defaultBackground
    
def Jeu1choix():   # Si le bouton "Juste Prix" est choisi alors on définit toutes les variables pour que le menu du juste prix s'affiche
    fenetre.destroy()
    global jeu1choix
    global jeu2choix
    global jeu4choix
    jeu1choix = True
    jeu2choix = False
    jeu4choix = False
    retour = False
    
def Jeu2choix():    # Si le bouton "Jeu des Allumettes" est choisi alors on définit toutes les variables pour que le menu du jeu des allumettes s'affiche
    fenetre.destroy()
    global jeu1choix
    global jeu2choix
    global jeu4choix
    global retour
    jeu2choix = True
    jeu1choix = False
    jeu4choix = False
    retour = False
    
def Jeu4choix():    # Si le bouton "Chasse au Trésor" est choisi alors on définit toutes les variables pour que le menu de la chasse au trésor s'affiche
    fenetre.destroy()
    global jeu1choix
    global jeu2choix
    global jeu4choix
    global retour
    jeu4choix = True
    jeu2choix = False
    jeu1choix = False
    retour = False
    
def fenetreretour():   # Si le bouton "Retour" est choisi alors on définit toutes les variables pour que le menu des différents jeux s'affiche
    global fenetrejeu1
    global fenetrejeu2
    global fenetrejeu4
    if fenetrejeu1:
        fenetre1.destroy()
        fenetrejeu1 = False
    elif fenetrejeu2:
        fenetre2.destroy()
        fenetrejeu2 = False
    elif fenetrejeu4:
        fenetre4.destroy()
        fenetrejeu4 = False
    global jeu1choix
    global jeu2choix
    global jeu4choix
    global retour
    retour = True
    jeu2choix = False
    jeu4choix = False
    jeu1choix = False
    
def quitter():    # Si le bouton "Quitter" est choisi alors on définit toutes les variables pour que le menu s'affiche
    global quitte
    fenetre.destroy()
    quitte = False

quitte = True
retour = True
jeu2choix = False
jeu4choix = False
jeu1choix = False

while quitte == True: # Cette boucle permet de garder une interface tant que l'on a pas pressé le bouton "Quitter"
    if jeu1choix:
        fenetrejeu1 = True
        fenetre1=tk.Tk()  # On définit  la variable fenetre1 en une fenêtre tkinter
        label1 = tk.Label(fenetre1, text="Jouer seul ou laisser l'ordinateur jouer ?")   # On définit l'entête
        label1.pack()
        fenetre1['bg'] = 'black'      # On définit la couleur du fond
        fenetre1.geometry("350x150")  # On définit la taille de la fenêtre
        bouton1jeu1 = HoverButton(fenetre1, command=Exercice_1.nombre_mystere,text="Jouer seul")               # Si le bouton "Jouer seul" est pressé nous lançons le programme Exercice1.nombre_mystere()
        bouton2jeu1 = HoverButton(fenetre1, command=Exercice_1.justeprix,text="Laisser l'ordinateur jouer")    # Si le bouton "Laisser l'ordinateur jouer" est pressé nous lançons le programme Exercice_1.justeprix()
        boutonretourjeu1 = HoverButton(fenetre1, command=fenetreretour,text="Retour")                          # Si le bouton "Retour" est pressé nous affichons le menu des jeux.
        bouton1jeu1.place(x=50,y=50)  # On définit les placements et les couleurs des boutons
        bouton2jeu1.place(x=160,y=50)
        boutonretourjeu1.place(x=130,y=100)
        boutonretourjeu1["fg"] = "red"   
        fenetre1.mainloop()  # On affiche la fenêtre tkinter

    elif jeu2choix:
        fenetrejeu2 = True
        fenetre2=tk.Tk() # On définit  la variable fenetre2 en une fenêtre tkinter
        label2 = tk.Label(fenetre2, text="Jouer seul ou laisser l'ordinateur jouer ?")  # On définit l'entête
        label2.pack()
        fenetre2['bg'] = 'black'      # On définit la couleur du fond
        fenetre2.geometry("350x150")  # On définit la taille de la fenêtre
        bouton1jeu2 = HoverButton(fenetre2, command=Exercice_2.jeu_des_allumettes,text="Jouer en 1c1")                          # Si le bouton "Jouer en 1c1" est pressé nous lançons le programme Exercice_2.jeu_des_allumettes
        bouton2jeu2 = HoverButton(fenetre2, command=Exercice_2.jeu_des_allumettes_ordinateur,text="Jouer contre l'ordinateur")  # Si le bouton "Jouer contre l'ordinateur" est pressé nous lançons le programme Exercice_2.jeu_des_allumettes_ordinateur
        boutonretourjeu2 = HoverButton(fenetre2, command=fenetreretour,text="Retour")                                           # Si le bouton "Retour" est pressé nous affichons le menu des jeux.
        bouton1jeu2.place(x=50,y=50)   # On définit les placements et les couleurs des boutons
        bouton2jeu2.place(x=160,y=50)
        boutonretourjeu2.place(x=150,y=100)
        boutonretourjeu2["fg"] = "red"
        fenetre2.mainloop()  # On affiche la fenêtre tkinter
        
    elif jeu4choix:
        fenetrejeu4 = True
        fenetre4=tk.Tk() # On définit  la variable fenetre2 en une fenêtre tkinter
        label4 = ttk.Label(fenetre4, text="Jouer seul ou laisser l'ordinateur jouer ?") # On définit l'entête
        label4.pack()
        fenetre4['bg'] = 'black'      # On définit la couleur du fond    
        fenetre4.geometry("350x150")  # On définit la taille de la fenêtre
        bouton1jeu4 = HoverButton(fenetre4, command=Exercice_4.chasse_au_tresor,text="Jouer seul")                              # Si le bouton "Jouer seul" est pressé nous lançons le programme Exercice_4.chasse_au_tresor
        bouton2jeu4 = HoverButton(fenetre4, command=Exercice_4.chasse_au_tresor_ordinateur,text="Laisser l'ordinateur jouer")   # Si le bouton "Laisser l'ordinateur jouer" est pressé nous lançons le programme Exercice_4.chasse_au_tresor_ordinateur
        boutonretourjeu4 = HoverButton(fenetre4, command=fenetreretour,text="Retour")                                           # Si le bouton "Retour" est pressé nous affichons le menu des jeux.
        bouton1jeu4.place(x=50,y=50)   # On définit les placements et les couleurs des boutons
        bouton2jeu4.place(x=160,y=50)
        boutonretourjeu4.place(x=130,y=100)
        boutonretourjeu4["fg"] = "red"
        fenetre4.mainloop()  # On affiche la fenêtre tkinter
        
    elif retour:
        retour = True
        fenetre = tk.Tk()  # On définit  la variable fenetre2 en une fenêtre tkinter
        fenetre['bg'] = 'black'      # On définit la couleur du fond  
        fenetre.geometry("350x200")  # On définit la taille de la fenêtre
        label = ttk.Label(fenetre, text="Liste des jeux jouables :")   # On définit l'entête
        label.pack()
        bouton1 = HoverButton(fenetre, command=Jeu1choix, text="Le Juste Prix")                   # Si le bouton "Le Juste Prix" est pressé nous lançons le programme Jeu1choix
        bouton2 = HoverButton(fenetre, command=Jeu2choix,text="Jeu des Allumettes")               # Si le bouton "Jeu des Allumettes" est pressé nous lançons le programme Jeu2choix
        bouton3 = HoverButton(fenetre, command=Exercice_3.jeuclement,text="Le Jeu des Multiples") # Si le bouton "Le Jeu des Multiples" est pressé nous lançons le programme Exercice_3.jeuclement
        bouton4 = HoverButton(fenetre, command=Jeu4choix,text="Chasse au Trésor")                 # Si le bouton "Chasse au Trésor" est pressé nous lançons le programme Jeu4choix
        bouton5 = HoverButton(fenetre, command=quitter,text ="Quitter")                           # Si le bouton "Quitter" est pressé nous lançons le programme quitter
        bouton1.place(x=50,y=50)   # On définit les placements et les couleurs des boutons
        bouton2.place(x=195,y=50)
        bouton3.place(x=35,y=100)
        bouton4.place(x=200,y=100)
        bouton5.place(x=145,y=150)
        bouton5["fg"] = "red"
        fenetre.mainloop()  # On affiche la fenêtre tkinter

