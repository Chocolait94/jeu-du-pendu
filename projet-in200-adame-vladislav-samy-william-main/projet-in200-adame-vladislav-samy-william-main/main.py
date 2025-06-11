import tkinter as tk
import fonction_game as fg
import enfant as enf
from enfant import afficher_fenetre_enfant
import random
from PIL import Image, ImageTk  



# Initialisation de la fenêtre
fenetre = tk.Tk()
fenetre.title("Le Pendu")
fenetre.geometry("800x800")


# etats jeu
etat_jeu = [[], [], random.choice(fg.mots_possibles).lower(), 0]
longueur_mot=""
# Cheat button function
def boutton_cheat(label_mot_cheat):
    mot = etat_jeu[2]
    label_mot_cheat.config(text=mot)

# Main frame
main_frame = tk.Frame(fenetre)
main_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)

# Left frame
left_frame = tk.Frame(fenetre, width=200, bg="#F5F5F5", bd=2, relief="raised")
left_frame.pack(side=tk.LEFT, fill=tk.Y, padx=10, pady=10)

# Charger l'image
image_path = "mem.jpeg"  
image = Image.open(image_path)
image = image.resize((300, 300))  
photo = ImageTk.PhotoImage(image)


label_image = tk.Label(left_frame, image=photo)
label_image.image = photo 





# Labels dans Left frame
label_score = tk.Label(left_frame, text="", font=("Helvetica", 12), bg="#F5F5F5")
label_lettre_propo = tk.Label(left_frame, text ="", font=("Helvetica", 12), bg="#F5F5F5")
label_mot_cheat = tk.Label(left_frame, text="", font=("Helvetica", 12), bg="#F5F5F5")

# Main frame
main_frame = tk.Frame(fenetre)
main_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)

# Canvas
canvas = tk.Canvas(fenetre, width=500, height=400, bg="white", bd=2, relief="raised")
canvas.pack(side=tk.TOP, fill=tk.BOTH, expand=True, padx=20, pady=20)

# entry et labels
entry_lettre = tk.Entry(main_frame, font=("Helvetica", 16), validate="key", validatecommand=(main_frame.register(fg.une_saisie), '%P'))
label_mot = tk.Label(main_frame, font=("Helvetica", 16))
label_fin_partie = tk.Label(main_frame, text="", font=("Helvetica", 16))
label_milieu_partie = tk.Label(main_frame, text="", font=("Helvetica", 16))

# Bouttons
button_valider = tk.Button(main_frame, text="Valider", command=lambda: fg.lettre_proposee(entry_lettre.get(), etat_jeu, label_mot, label_fin_partie, label_milieu_partie, entry_lettre, canvas, fenetre, label_lettre_propo), font=("Helvetica", 16), bg="#4caf50", fg="white")
bouton_quitter = tk.Button(main_frame, text="Quitter", command=fenetre.quit, font=("Helvetica", 16), bg="#f44336", fg="white")
boutton_regle = tk.Button(left_frame, text="Règle du jeu", command=fg.regle_jeu, font=("Helvetica", 16), bg="#2196f3", fg="white")
boutton_score = tk.Button(left_frame, text="Score", command=lambda: fg.score(label_score), font=("Helvetica", 16), bg="#ff9800", fg="white")
bouton_afficher_lettrepropo = tk.Button(left_frame, text="Afficher les lettres déjà proposées", command=lambda: fg.afficher_lettre(label_lettre_propo), font=("Helvetica", 16), bg="#607d8b", fg="white")
boutton_cheatt = tk.Button(left_frame, text="Voir le mot", command=lambda: boutton_cheat(label_mot_cheat), font=("Helvetica", 16), bg="#ff9800", fg="white")


def lier_entrée(event):
    button_valider.invoke()  

fenetre.bind('<Return>', lier_entrée)


# widget
label_mot.grid(row=0, column=0, columnspan=2, padx=10, pady=10)
label_fin_partie.grid(row=4, column=0, columnspan=2, padx=10, pady=10)
label_milieu_partie.grid(row=3, column=0, columnspan=2, padx=10, pady=10)
entry_lettre.grid(row=1, column=0, padx=10, pady=10, sticky="ew")
button_valider.grid(row=1, column=1, padx=10, pady=10, sticky="ew")
bouton_quitter.grid(row=2, column=0, columnspan=2, padx=10, pady=10, sticky="ew")

label_score.pack(fill=tk.X, padx=10, pady=5)
label_lettre_propo.pack(fill=tk.X, padx=10, pady=5)
label_mot_cheat.pack(fill=tk.X, padx=10, pady=5)
boutton_regle.pack(fill=tk.X, padx=10, pady=5)
boutton_score.pack(fill=tk.X, padx=10, pady=5)
bouton_afficher_lettrepropo.pack(fill=tk.X, padx=10, pady=5)
boutton_cheatt.pack(fill=tk.X, padx=10, pady=5)
label_image.pack(side=tk.BOTTOM, padx=10, pady=10)
# appel
fg.afficher_mot(label_mot, etat_jeu)
fg.creation_pendu(canvas, etat_jeu, fenetre)


# lancement
fenetre.mainloop()
