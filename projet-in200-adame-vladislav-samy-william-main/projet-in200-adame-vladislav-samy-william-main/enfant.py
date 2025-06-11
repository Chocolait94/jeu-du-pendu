import tkinter as tk
import random
import tkinter as tk

def afficher_fenetre_enfant(fenetre, relancer_jeu, etat_jeu, label_mot, label_fin_partie, entry_lettre, canvas, quitter, label_lettre_propo):
    # Création de la fenêtre enfant
    fenetre_enfant = tk.Toplevel(fenetre)
    fenetre_enfant.title("Menu fin de jeu")

    fenetre_enfant.configure(bg="#f0f0f0")
    label_titre = tk.Label(fenetre_enfant, text="Menu fin de jeu", font=("Helvetica", 16, "bold"), bg="#f0f0f0")
    label_titre.pack()  

    label_message = tk.Label(fenetre_enfant, text="", font=("Helvetica", 12), bg="#f0f0f0")
    label_message.pack()

    if  set(lettre for lettre in etat_jeu[2]) <= set(etat_jeu[1]):
        message = "Félicitations ! Vous avez gagné. Le mot était : " + etat_jeu[2]
        label_message.config(text=message)  
    else:
        message = "Dommage ! Vous avez perdu. Le mot était : " + etat_jeu[2]
        label_message.config(text=message)  

    bouton_recommencer = tk.Button(fenetre_enfant, text="Recommencer", command=lambda: relancer_jeu(label_mot, label_fin_partie, label_lettre_propo, entry_lettre, etat_jeu, canvas, fenetre, fenetre_enfant), font=("Helvetica", 14), bg="#4caf50", fg="white", width=20)
    bouton_recommencer.pack(pady=20)
    bouton_quitter = tk.Button(fenetre_enfant, text="Quitter", command=lambda: quitter(fenetre), font=("Helvetica", 14), bg="#f44336", fg="white", width=20)
    bouton_quitter.pack()
    
    x = fenetre.winfo_rootx() + fenetre.winfo_width() // 2 - fenetre_enfant.winfo_reqwidth() // 2
    y = fenetre.winfo_rooty() + fenetre.winfo_height() // 2 - fenetre_enfant.winfo_reqheight() // 2
    fenetre_enfant.geometry("+{}+{}".format(x, y))

    




    