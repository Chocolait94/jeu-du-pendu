import tkinter as tk
import random
import webbrowser
import enfant as enf
from tkinter import simpledialog



longueur_mot =""
scores = []
mots_propo = []

def regle_jeu():
    webbrowser.open_new("https://cruciverbiste.com/le-pendu-regles-astuces-sites-ou-jouer/")

    

def dictionnaire(dico):
    mots = []
    with open(dico, "r") as fichier:
        for ligne in fichier:
            mots.append(ligne.strip())  
    return mots

mots_possibles = dictionnaire("dico.txt")

etat_jeu = [[], [], random.choice(mots_possibles).lower(), 0]



# Fonction pour quitter le jeu
def quitter(fenetre):
    fenetre.destroy()


def afficher_mot(label_mot, etat_jeu):
    mot = ""
    mot_a_deviner = etat_jeu[2]  
    for lettre in mot_a_deviner:
        if lettre in etat_jeu[1]:
            mot += lettre + " "
        else:
            mot += "_ "
    label_mot.config(text=mot)


def une_saisie(lettre):
    if len(lettre)>1:
        return False
    return True



# # Fonction pour relancer le jeu
def relancer_jeu(label_mot, label_fin_partie, label_lettre_propo, entry_lettre, etat_jeu, canvas,  fenetre,fenetre_enfant ):
    global mots_propo  
    scores.append(etat_jeu[3])
    etat_jeu[1].clear()
    etat_jeu[3] = 0
    etat_jeu[2] = obtenir_longueur_mot(fenetre)
    
    
    mots_propo = []
    
    afficher_mot(label_mot, etat_jeu)
    afficher_lettre(label_lettre_propo)  
    obtenir_longueur_mot(fenetre)
    relancer_canvas(canvas)
    label_fin_partie.config(text="")
    entry_lettre.delete(0, tk.END)
    if fenetre_enfant:
        fenetre_enfant.destroy()
    


def relancer_canvas(canvas):
    canvas.delete("all")
    
    

# Fonction pour gérer la saisie d'une lettre

def lettre_proposee(lettre, etat_jeu, label_mot, label_fin_partie, label_milieu_partie, entry_lettre, canvas , fenetre , label_lettre_propo):
    global mots_propo
    if lettre in etat_jeu[1] and len(lettre)==1:
        mots_propo.append(lettre)
        
        label_milieu_partie.config(text="Vous avez déjà proposé cette lettre :" " "  + lettre)
        fenetre.after(4000, lambda: label_milieu_partie.config(text=""))      
    else:
        etat_jeu[1].append(lettre)

    
        if lettre.isdigit():
           label_milieu_partie.config(text="Vous avez chosie un chiifre.")
        elif lettre in etat_jeu[2] and len(lettre)==1 :
            mots_propo.append(lettre)
            
            print("Bonne lettre !")
        elif lettre not in etat_jeu[2] and len(lettre)==1 :
            mots_propo.append(lettre)
            
            print("Mauvaise lettre !")
            etat_jeu[3] += 1
            creation_pendu(canvas, etat_jeu, fenetre)
            label_milieu_partie.config(text="vous avez " + str(etat_jeu[3]) + " erreurs.")
            fenetre.after(1000, lambda: label_milieu_partie.config(text=""))
            

        

            
    afficher_lettre(label_lettre_propo)
    afficher_mot(label_mot, etat_jeu)

    if etat_jeu[3] >= 10:
        enf.afficher_fenetre_enfant(fenetre, relancer_jeu, etat_jeu, label_mot, label_fin_partie, entry_lettre, canvas, quitter, label_lettre_propo)
    elif set(lettre for lettre in etat_jeu[2]) <= set(etat_jeu[1]):
        print("Vous avez deviné le mot !")
        enf.afficher_fenetre_enfant(fenetre, relancer_jeu, etat_jeu, label_mot, label_fin_partie, entry_lettre, canvas, quitter, label_lettre_propo)


def creation_pendu(canvas, etat_jeu, fenetre):
    x = 150  
    y = 150  
    if etat_jeu[3] == 1 : 
        canvas.create_line(x-50, y+170, x+50, y+170, fill='black', width=5) 
    elif etat_jeu[3] == 2 :
        canvas.create_line(x, y+170, x, y-50, fill='black', width=5) 
    elif etat_jeu[3] == 3 :
        canvas.create_line(x-50, y-50, x+150, y-50, fill='black', width=5) 
    elif etat_jeu[3] == 4 :
        canvas.create_line(x, y, x+50, y-50, fill='black', width=5)  
    elif etat_jeu[3] == 5 :
        canvas.create_line(x+100, y-50, x+100, y, fill='black', width=5) 
    elif etat_jeu[3] == 6 :
        canvas.create_oval(x+70, y, x+130, y+50, fill='black', width=5) 
    elif etat_jeu[3] == 7 :
        canvas.create_line(x+100, y+50, x+100, y+200, fill='black', width=5) 
    elif etat_jeu[3] == 8 :
        canvas.create_line(x+50, y+100, x+150, y+100, fill='black', width=5) 
    elif etat_jeu[3] == 9 :
        canvas.create_line(x+100, y+200, x+50, y+250, fill='black', width=5) 
    elif etat_jeu[3] == 10 : 
        canvas.create_line(x+100, y+200, x+150, y+250, fill='black', width=5)
    canvas.update()  

def score(label_score):
    global scores
    label_score.config(text="Scores de toutes les parties : " + ', '.join(map(str, scores)))

def afficher_lettre(label_lettre_propo):
    global mots_propo
    lst = []
    for lettre in mots_propo:
        if lettre not in lst:
            lst.append(lettre)
    

            
    
    label_lettre_propo.config(text="Vos lettres proposées : " + ', '.join(map(str, lst)))


def obtenir_longueur_mot(fenetre):
    longueur_mot = simpledialog.askinteger("Longueur du mot", "Entrez la longueur du mot à deviner :", parent=fenetre)
    mots_possibles_filtres = [mot for mot in mots_possibles if len(mot) == longueur_mot]
    if mots_possibles_filtres:
        return random.choice(mots_possibles_filtres)
    else:
        return None







            




