#importation des modules
from tkinter import *
import random

#déclaration des variables et du tableau de verbes
v = 0
score = 0
valeurs = []
tableau_vi= [["be","was/were","been","etre"],
            ["become","became","become","devenir"],
            ["begin","began","begun","commencer"],
            ["break","broke","broken","casser"],
            ["bring","brought","brought","apporter"],
            ["build","built","built","construire"],
            ["burn","burnt","burnt","bruler"],
            ["buy","bought","bought","acheter"],
            ["catch","caught","caught","attraper"],
            ["choose","chose","chosen","choisir"],
            ["come","came","come","venir"],
            ["cost","cost","cost","couter"],
            ["cut","cut","cut","couper"],
            ["do","did","done","faire"],
            ["draw","drew","drawn","dessiner"],
            ["dream","dreamt","dreamt","rever"],
            ["drink","drank","drunk","boire"],
            ["drive","drove","driven","conduire"],
            ["eat","ate","eaten","manger"],
            ["fall","fell","fallen","tomber"],
            ["feel","felt","felt","ressentir"],
            ["fight","fought","fougth","se battre"],
            ["find","found","found","trouver"],
            ["fly","flew","flown","voler"],
            ["forget","forgot","forgotten","oublier"],
            ["forgive","forgave","forgiven","pardonner"],
            ["get","got","got","obtenir"],
            ["give","gave","given","donner"],
            ["go","went","gone","aller"],
            ["have","had","had","avoir"],
            ["hear","heard","heard","entendre"],
            ["hit","hit","hit","frapper"],
            ["hold","held","helt","tenir"],
            ["hurt","hurt","hurt","blesser"],
            ["keep","kept","kept","garder"],
            ["know","knew","known","savoir"],
            ["lead","led","led","mener"],
            ["learn","learnt","learnt","apprendre"],
            ["leave","left","left","partir"],
            ["lose","lost","lost","perdre"],
            ["make","made","made","fabriquer"],
            ["mean","meant","meant","signifier"],
            ["meet","met","met","rencontrer"],
            ["pay","paid","paid","payer"],
            ["put","put","put","mettre"],
            ["read","read","read","lire"],
            ["ride","rode","ridden","faire"],
            ["ring","rang","rung","sonner"],
            ["run","ran","run","courir"],
            ["say","said","said","dire"],
            ["see","saw","seen","voir"],
            ["sell","sold","sold","vendre"],
            ["send","sent","sent","envoyer"],
            ["shoot","shot","shot","tirer"],
            ["show","showed","shown","montrer"],
            ["shut","shut","shut","fermer"],
            ["sing","sang","sung","chanter"],
            ["sit","sat","sat","asseoir"],
            ["sleep","slept","slept","dormir"],
            ["smell","smelt","smelt","sentir"],
            ["speak","spoke","spoken","spoken"],
            ["spell","spelt","spelt","epeler"],
            ["spend","spent","spent","depenser"],
            ["stand","stood","stood","etre debout"],
            ["steal","stole","stolen","derober"],
            ["swim","swam","swum","nager"],
            ["take","took","taken","prendre"],
            ["teach","taught","taught","enseigner"],
            ["tell","told","told","raconter"],
            ["think","thought","thought","penser"],
            ["throw","threw","thrown","lancer"],
            ["understand","understood","understood","comprendre"],
            ["wake","woke","woken","se reveiller"],
            ["wear","wore","worn","porter"],
            ["win","won","won","gagner"],
            ["write","wrote","written","ecrire"]]

#cette définition permet de choisir aléatoirement x et y
def initxy():
    global x, y, valeurs
    x = random.randint(0, 75) #tirer x entre 0 et 75
    y = random.randint(0,3) #tirer y entre 0 et 3
    while x in valeurs != True : #tant que la ligne tirée a déja été tiré
        x = random.randint(1, 75) #retirer x
    valeurs.append(x) #ajouter x aux valeurs

#cette définition permet de générer une nouvelle ligne
def generate():
    hide = "******"
    global x
    global y

    initxy() #appel de la def aléatoire de x et y

    if y ==0: #si premiere colonne tirée
        baser = Label(frame, text=hide, font=("Courrier", 10), bg='#FFFFFF', fg='black') #cacher la premiere colonne
        baser.place(x=-230, y=-50, width=110, height=25) #donne la position du label
        preteritr = Label(frame, text=tableau_vi[x][1], font=("Courrier", 10), bg='#FFFFFF', fg='black') #montrer la deuxieme colonne
        preteritr.place(x=-110, y=-50, width=110, height=25) #donne la position du label
        participer = Label(frame, text=tableau_vi[x][2], font=("Courrier", 10), bg='#FFFFFF', fg='black') #montrer la troisieme colonne
        participer.place(x=10, y=-50, width=110, height=25) #donne la position du label
        traductionr = Label(frame, text=tableau_vi[x][3], font=("Courrier", 10), bg='#FFFFFF', fg='black') #montrer la dernier colonne
        traductionr.place(x=130, y=-50, width=110, height=25) #donne la position du label

    if y ==1: #si deuxieme colonne tirée
        baser = Label(frame, text=tableau_vi[x][0], font=("Courrier", 10), bg='#FFFFFF', fg='black')
        baser.place(x=-230, y=-50, width=110, height=25)
        preteritr = Label(frame, text=hide, font=("Courrier", 10), bg='#FFFFFF', fg='black') #cacher la deuxieme colonne
        preteritr.place(x=-110, y=-50, width=110, height=25)
        participer = Label(frame, text=tableau_vi[x][2], font=("Courrier", 10), bg='#FFFFFF', fg='black')
        participer.place(x=10, y=-50, width=110, height=25)
        traductionr = Label(frame, text=tableau_vi[x][3], font=("Courrier", 10), bg='#FFFFFF', fg='black')
        traductionr.place(x=130, y=-50, width=110, height=25)

    if y ==2: #si troisieme colonne tiree
        baser = Label(frame, text=tableau_vi[x][0], font=("Courrier", 10), bg='#FFFFFF', fg='black')
        baser.place(x=-230, y=-50, width=110, height=25)
        preteritr = Label(frame, text=tableau_vi[x][1], font=("Courrier", 10), bg='#FFFFFF', fg='black')
        preteritr.place(x=-110, y=-50, width=110, height=25)
        participer = Label(frame, text=hide, font=("Courrier", 10), bg='#FFFFFF', fg='black') #cacher la troisieme colonne
        participer.place(x=10, y=-50, width=110, height=25)
        traductionr = Label(frame, text=tableau_vi[x][3], font=("Courrier", 10), bg='#FFFFFF', fg='black')
        traductionr.place(x=130, y=-50, width=110, height=25)

    if y ==3: #si quatrieme colonne tiree
        baser = Label(frame, text=tableau_vi[x][0], font=("Courrier", 10), bg='#FFFFFF', fg='black')
        baser.place(x=-230, y=-50, width=110, height=25)
        preteritr = Label(frame, text=tableau_vi[x][1], font=("Courrier", 10), bg='#FFFFFF', fg='black')
        preteritr.place(x=-110, y=-50, width=110, height=25)
        participer = Label(frame, text=tableau_vi[x][2], font=("Courrier", 10), bg='#FFFFFF', fg='black')
        participer.place(x=10, y=-50, width=110, height=25)
        traductionr = Label(frame, text=hide, font=("Courrier", 10), bg='#FFFFFF', fg='black') #cacher la derniere colonne
        traductionr.place(x=130, y=-50, width=110, height=25)



#cette définition détermine les bonnes ou mauvaises réponses et ajoute le score et les couleurs pour chaque réponses
def validate():
    global tirage1, tirage2, tirage3,tirage4, tirage5, tirage6, tirage7, tirage8, tirage9, tirage10, score, v, x, y, reponse1, reponse2, reponse3, reponse4, reponse5, reponse6, reponse7, reponse8, reponse9, reponse10, color1, color2, color3, color4, color5, color6, color7, color8, color9, color10

    if v < 10: #si il y a eu moins de 10 tirages
        if reponse.get() == tableau_vi[x][y]: #si il s'agit de la bonne réponse
            score = score + 1 #ajouter 1 au score
            if v == 0: #si il s'agit du premier tirage
                color1 = "green" #mettre la couleur 1 à vert
            if v == 1: #si il s'agit du deuxieme tirage
                color2 = "green" #mettre la couleur 2 à vert
            if v == 2: #si il s'agit du troisieme tirage
                color3 = "green"
            if v == 3:
                color4 = "green"
            if v == 4:
                color5 = "green"
            if v == 5:
                color6 = "green"
            if v == 6:
                color7 = "green"
            if v == 7:
                color8 = "green"
            if v == 8:
                color9 = "green"
            if v == 9:
                color10 = "green"

#les labels ci dessous pemettent d'afficher le score au fur et à mesure
        scorec = Label(frame, text="Score :", font=("Courrier", 10), bg='#FF7433', fg='white')
        scorec.place(x=80, y=90, width=90, height=25)
        scorec = Label(frame, text=score, font=("Courrier", 10), bg='#FF7433', fg='white') #affichage du score
        scorec.place(x=170, y=90, width=25, height=25)
        scorec = Label(frame, text="/", font=("Courrier", 10), bg='#FF7433', fg='white') #sur
        scorec.place(x=195, y=90, width=10, height=25)
        scorec = Label(frame, text=v+1, font=("Courrier", 10), bg='#FF7433', fg='white') #le nombre de tirage effectué
        scorec.place(x=205, y=90, width=25, height=25)

#la partie ci dessous permet d'enregistrer dans une variable le contenu de chaque ligne tirée ainsi que la réponse du joueur
        if y == 0:
            if v == 0: #si il s'agit du premier tirage
                tirage1 = tableau_vi[x][0].upper() + "    " + tableau_vi[x][1] + "    " + tableau_vi[x][2] + "    " + tableau_vi[x][3] #enregistre le contenu de la ligne
                reponse1 = reponse.get() #enregistre la reponse du joueur
            if v == 1:
                tirage2 = tableau_vi[x][0].upper() + "    " + tableau_vi[x][1] + "    " + tableau_vi[x][2] + "    " + tableau_vi[x][3]
                reponse2 = reponse.get()
            if v == 2:
                tirage3 = tableau_vi[x][0].upper() + "    " + tableau_vi[x][1] + "    " + tableau_vi[x][2] + "    " + tableau_vi[x][3]
                reponse3 = reponse.get()
            if v == 3:
                tirage4 = tableau_vi[x][0].upper() + "    " + tableau_vi[x][1] + "    " + tableau_vi[x][2] + "    " + tableau_vi[x][3]
                reponse4 = reponse.get()
            if v == 4:
                tirage5 = tableau_vi[x][0].upper() + "    " + tableau_vi[x][1] + "    " + tableau_vi[x][2] + "    " + tableau_vi[x][3]
                reponse5 = reponse.get()
            if v == 5:
                tirage6 = tableau_vi[x][0].upper() + "    " + tableau_vi[x][1] + "    " + tableau_vi[x][2] + "    " + tableau_vi[x][3]
                reponse6 = reponse.get()
            if v == 6:
                tirage7 = tableau_vi[x][0].upper() + "    " + tableau_vi[x][1] + "    " + tableau_vi[x][2] + "    " + tableau_vi[x][3]
                reponse7 = reponse.get()
            if v == 7:
                tirage8 = tableau_vi[x][0].upper() + "    " + tableau_vi[x][1] + "    " + tableau_vi[x][2] + "    " + tableau_vi[x][3]
                reponse8 = reponse.get()
            if v == 8:
                tirage9 = tableau_vi[x][0].upper() + "    " + tableau_vi[x][1] + "    " + tableau_vi[x][2] + "    " + tableau_vi[x][3]
                reponse9 = reponse.get()
            if v == 9:
                tirage10 = tableau_vi[x][0].upper() + "    " + tableau_vi[x][1] + "    " + tableau_vi[x][2] + "    " + tableau_vi[x][3]
                reponse10 = reponse.get()

        if y == 1:
            if v == 0: #si il s'agit du premier tirage
                tirage1 = tableau_vi[x][0] + "    " + tableau_vi[x][1].upper() + "    " + tableau_vi[x][2] + "    " + tableau_vi[x][3] #enregistre le contenu de la ligne
                reponse1 = reponse.get() #enregistre la reponse du joueur
            if v == 1:
                tirage2 = tableau_vi[x][0] + "    " + tableau_vi[x][1].upper() + "    " + tableau_vi[x][2] + "    " + tableau_vi[x][3]
                reponse2 = reponse.get()
            if v == 2:
                tirage3 = tableau_vi[x][0] + "    " + tableau_vi[x][1].upper() + "    " + tableau_vi[x][2] + "    " + tableau_vi[x][3]
                reponse3 = reponse.get()
            if v == 3:
                tirage4 = tableau_vi[x][0] + "    " + tableau_vi[x][1].upper() + "    " + tableau_vi[x][2] + "    " + tableau_vi[x][3]
                reponse4 = reponse.get()
            if v == 4:
                tirage5 = tableau_vi[x][0] + "    " + tableau_vi[x][1].upper() + "    " + tableau_vi[x][2] + "    " + tableau_vi[x][3]
                reponse5 = reponse.get()
            if v == 5:
                tirage6 = tableau_vi[x][0] + "    " + tableau_vi[x][1].upper() + "    " + tableau_vi[x][2] + "    " + tableau_vi[x][3]
                reponse6 = reponse.get()
            if v == 6:
                tirage7 = tableau_vi[x][0] + "    " + tableau_vi[x][1].upper() + "    " + tableau_vi[x][2] + "    " + tableau_vi[x][3]
                reponse7 = reponse.get()
            if v == 7:
                tirage8 = tableau_vi[x][0] + "    " + tableau_vi[x][1].upper() + "    " + tableau_vi[x][2] + "    " + tableau_vi[x][3]
                reponse8 = reponse.get()
            if v == 8:
                tirage9 = tableau_vi[x][0] + "    " + tableau_vi[x][1].upper() + "    " + tableau_vi[x][2] + "    " + tableau_vi[x][3]
                reponse9 = reponse.get()
            if v == 9:
                tirage10 = tableau_vi[x][0] + "    " + tableau_vi[x][1].upper() + "    " + tableau_vi[x][2] + "    " + tableau_vi[x][3]
                reponse10 = reponse.get()

        if y == 2:
            if v == 0: #si il s'agit du premier tirage
                tirage1 = tableau_vi[x][0] + "    " + tableau_vi[x][1] + "    " + tableau_vi[x][2].upper() + "    " + tableau_vi[x][3] #enregistre le contenu de la ligne
                reponse1 = reponse.get() #enregistre la reponse du joueur
            if v == 1:
                tirage2 = tableau_vi[x][0] + "    " + tableau_vi[x][1] + "    " + tableau_vi[x][2].upper() + "    " + tableau_vi[x][3]
                reponse2 = reponse.get()
            if v == 2:
                tirage3 = tableau_vi[x][0] + "    " + tableau_vi[x][1] + "    " + tableau_vi[x][2].upper() + "    " + tableau_vi[x][3]
                reponse3 = reponse.get()
            if v == 3:
                tirage4 = tableau_vi[x][0] + "    " + tableau_vi[x][1] + "    " + tableau_vi[x][2].upper() + "    " + tableau_vi[x][3]
                reponse4 = reponse.get()
            if v == 4:
                tirage5 = tableau_vi[x][0] + "    " + tableau_vi[x][1] + "    " + tableau_vi[x][2].upper() + "    " + tableau_vi[x][3]
                reponse5 = reponse.get()
            if v == 5:
                tirage6 = tableau_vi[x][0] + "    " + tableau_vi[x][1] + "    " + tableau_vi[x][2].upper() + "    " + tableau_vi[x][3]
                reponse6 = reponse.get()
            if v == 6:
                tirage7 = tableau_vi[x][0] + "    " + tableau_vi[x][1] + "    " + tableau_vi[x][2].upper() + "    " + tableau_vi[x][3]
                reponse7 = reponse.get()
            if v == 7:
                tirage8 = tableau_vi[x][0] + "    " + tableau_vi[x][1] + "    " + tableau_vi[x][2].upper() + "    " + tableau_vi[x][3]
                reponse8 = reponse.get()
            if v == 8:
                tirage9 = tableau_vi[x][0] + "    " + tableau_vi[x][1] + "    " + tableau_vi[x][2].upper() + "    " + tableau_vi[x][3]
                reponse9 = reponse.get()
            if v == 9:
                tirage10 = tableau_vi[x][0] + "    " + tableau_vi[x][1] + "    " + tableau_vi[x][2].upper() + "    " + tableau_vi[x][3]
                reponse10 = reponse.get()

        if y == 3:
            if v == 0: #si il s'agit du premier tirage
                tirage1 = tableau_vi[x][0] + "    " + tableau_vi[x][1] + "    " + tableau_vi[x][2] + "    " + tableau_vi[x][3].upper() #enregistre le contenu de la ligne
                reponse1 = reponse.get() #enregistre la reponse du joueur
            if v == 1:
                tirage2 = tableau_vi[x][0] + "    " + tableau_vi[x][1] + "    " + tableau_vi[x][2] + "    " + tableau_vi[x][3].upper()
                reponse2 = reponse.get()
            if v == 2:
                tirage3 = tableau_vi[x][0] + "    " + tableau_vi[x][1] + "    " + tableau_vi[x][2] + "    " + tableau_vi[x][3].upper()
                reponse3 = reponse.get()
            if v == 3:
                tirage4 = tableau_vi[x][0] + "    " + tableau_vi[x][1] + "    " + tableau_vi[x][2] + "    " + tableau_vi[x][3].upper()
                reponse4 = reponse.get()
            if v == 4:
                tirage5 = tableau_vi[x][0] + "    " + tableau_vi[x][1] + "    " + tableau_vi[x][2] + "    " + tableau_vi[x][3].upper()
                reponse5 = reponse.get()
            if v == 5:
                tirage6 = tableau_vi[x][0] + "    " + tableau_vi[x][1] + "    " + tableau_vi[x][2] + "    " + tableau_vi[x][3].upper()
                reponse6 = reponse.get()
            if v == 6:
                tirage7 = tableau_vi[x][0] + "    " + tableau_vi[x][1] + "    " + tableau_vi[x][2] + "    " + tableau_vi[x][3].upper()
                reponse7 = reponse.get()
            if v == 7:
                tirage8 = tableau_vi[x][0] + "    " + tableau_vi[x][1] + "    " + tableau_vi[x][2] + "    " + tableau_vi[x][3].upper()
                reponse8 = reponse.get()
            if v == 8:
                tirage9 = tableau_vi[x][0] + "    " + tableau_vi[x][1] + "    " + tableau_vi[x][2] + "    " + tableau_vi[x][3].upper()
                reponse9 = reponse.get()
            if v == 9:
                tirage10 = tableau_vi[x][0] + "    " + tableau_vi[x][1] + "    " + tableau_vi[x][2] + "    " + tableau_vi[x][3].upper()
                reponse10 = reponse.get()

        reponse.delete(first=0, last=100) #vider la zone d'entrée

        v = v + 1 #ajouter 1 au nombre de tirage

        generate() #générer la nouvelle ligne (appel de la définition generate)

    if v == 10: #si le nombre de tirage est egal à 10
        resultat() #afficher les resultats (appel de la definition resultat)

#cette définition permet d'afficher les résultats
def resultat():
    global tirage1, tirage2, tirage3,tirage4, tirage5, tirage6, tirage7, tirage8, tirage9, tirage10, reponse1, reponse2, reponse3, reponse4, reponse5, reponse6, reponse7, reponse8, reponse9, reponse10, color1, color2, color3, color4, color5, color6, color7, color8, color9, color10

    labelr = Label(frame, text="", font=("Courrier", 10), bg='#DEF6FF', fg='black') #label vide qui se supperpose au dessus de tous les labels, boutons et entréé précédement définis
    labelr.place(x=-300, y=-200, width=600, height=600) #placement du label

#la partie ci dessous permet d'afficher le score final
    scorea = Label(frame, text="Votre score :", font=("Arial", 10), bg='purple', fg='white')
    scorea.place(x=50, y=-110, width=100, height=25)
    scoreb = Label(frame, text=score, font=("Arial", 10), bg='purple', fg='white') #score
    scoreb.place(x=145, y=-110, width=25, height=25)
    scorey = Label(frame, text="/ 10", font=("Arial", 10), bg='purple', fg='white') #sur 10
    scorey.place(x=165, y=-110, width=40, height=25)

#entete du tableau
    repc = Label(frame, text="Vos réponses", font=("Courrier", 10), bg='grey', fg='white')
    repc.place(x=-200, y=-78, width=140, height=23)
    scorec = Label(frame, text="Bonnes réponses", font=("Courrier", 10), bg='grey', fg='white')
    scorec.place(x=-55, y=-78, width=300, height=23)

#premiere ligne
    numc = Label(frame, text="1", font=("Courrier", 10), bg='grey', fg='white') #numero de la ligne
    numc.place(x=-230, y=-50, width=25, height=23)
    repc = Label(frame, text=reponse1, font=("Courrier", 10), bg=color1, fg='white') #reponse du joueur
    repc.place(x=-200, y=-50, width=140, height=23)
    scorec = Label(frame, text=tirage1, font=("Courrier", 10), bg='#FF7433', fg='white') #bonne réponse de la ligne tirée
    scorec.place(x=-55, y=-50, width=300, height=23)

#deuxieme ligne
    numd = Label(frame, text="2", font=("Courrier", 10), bg='grey', fg='white') #numero de la ligne
    numd.place(x=-230, y=-25, width=25, height=23)
    repd = Label(frame, text=reponse2, font=("Courrier", 10), bg=color2, fg='white') #reponse du joueur
    repd.place(x=-200, y=-25, width=140, height=23)
    scored = Label(frame, text=tirage2, font=("Courrier", 10), bg='#FF7433', fg='white') #bonne réponse de la ligne tirée
    scored.place(x=-55, y=-25, width=300, height=23)

#troisieme ligne
    nume = Label(frame, text="3", font=("Courrier", 10), bg='grey', fg='white')
    nume.place(x=-230, y=0, width=25, height=23)
    repe = Label(frame, text=reponse3, font=("Courrier", 10), bg=color3, fg='white')
    repe.place(x=-200, y=0, width=140, height=23)
    scoree = Label(frame, text=tirage3, font=("Courrier", 10), bg='#FF7433', fg='white')
    scoree.place(x=-55, y=0, width=300, height=23)

    numf = Label(frame, text="4", font=("Courrier", 10), bg='grey', fg='white')
    numf.place(x=-230, y=25, width=25, height=23)
    repf = Label(frame, text=reponse4, font=("Courrier", 10), bg=color4, fg='white')
    repf.place(x=-200, y=25, width=140, height=23)
    scoref = Label(frame, text=tirage4, font=("Courrier", 10), bg='#FF7433', fg='white')
    scoref.place(x=-55, y=25, width=300, height=23)

    numg = Label(frame, text="5", font=("Courrier", 10), bg='grey', fg='white')
    numg.place(x=-230, y=50, width=25, height=23)
    repg = Label(frame, text=reponse5, font=("Courrier", 10), bg=color5, fg='white')
    repg.place(x=-200, y=50, width=140, height=23)
    scoreg = Label(frame, text=tirage5, font=("Courrier", 10), bg='#FF7433', fg='white')
    scoreg.place(x=-55, y=50, width=300, height=23)

    numh = Label(frame, text="6", font=("Courrier", 10), bg='grey', fg='white')
    numh.place(x=-230, y=75, width=25, height=23)
    reph = Label(frame, text=reponse6, font=("Courrier", 10), bg=color6, fg='white')
    reph.place(x=-200, y=75, width=140, height=23)
    scoreh = Label(frame, text=tirage6, font=("Courrier", 10), bg='#FF7433', fg='white')
    scoreh.place(x=-55, y=75, width=300, height=23)

    numi = Label(frame, text="7", font=("Courrier", 10), bg='grey', fg='white')
    numi.place(x=-230, y=100, width=25, height=23)
    repi = Label(frame, text=reponse7, font=("Courrier", 10), bg=color7, fg='white')
    repi.place(x=-200, y=100, width=140, height=23)
    scorei = Label(frame, text=tirage7, font=("Courrier", 10), bg='#FF7433', fg='white')
    scorei.place(x=-55, y=100, width=300, height=23)

    numj = Label(frame, text="8", font=("Courrier", 10), bg='grey', fg='white')
    numj.place(x=-230, y=125, width=25, height=23)
    repj = Label(frame, text=reponse8, font=("Courrier", 10), bg=color8, fg='white')
    repj.place(x=-200, y=125, width=140, height=23)
    scorej = Label(frame, text=tirage8, font=("Courrier", 10), bg='#FF7433', fg='white')
    scorej.place(x=-55, y=125, width=300, height=23)

    numk = Label(frame, text="9", font=("Courrier", 10), bg='grey', fg='white')
    numk.place(x=-230, y=150, width=25, height=23)
    repck = Label(frame, text=reponse9, font=("Courrier", 10), bg=color9, fg='white')
    repck.place(x=-200, y=150, width=140, height=23)
    scorek = Label(frame, text=tirage9, font=("Courrier", 10), bg='#FF7433', fg='white')
    scorek.place(x=-55, y=150, width=300, height=23)

    numl = Label(frame, text="10", font=("Courrier", 10), bg='grey', fg='white')
    numl.place(x=-230, y=175, width=25, height=23)
    repcl = Label(frame, text=reponse10, font=("Courrier", 10), bg=color10, fg='white')
    repcl.place(x=-200, y=175, width=140, height=23)
    scorel = Label(frame, text=tirage10, font=("Courrier", 10), bg='#FF7433', fg='white')
    scorel.place(x=-55, y=175, width=300, height=23)

#paramettre de la fenetre
window = Tk() #fenetre tkinter
window.title("Irregular Verbs") #titre de la page
window.geometry("1600x900") #taille de base de la page
window.minsize(500, 325) #taille minimale de page
#window.iconbitmap("flag.ico") #logo de la page
window.config(bg='#DEF6FF') #couleur de fond de la page

color1 = color2 = color3 = color4 = color5 = color6 = color7 = color8 = color9 = color10 = "red"

#boite
frame= Frame(window, bg='#DEF6FF', bd=1, pady=125, padx=250) #boite contenant tous les éléments

#entete (label avec "Base verbale, preterit ...)
base = Label(frame, text="Base Verbale", font=("Courrier", 10), bg='#FF7433', fg='white') #label base verbale
base.place(x=-230, y=-90, width=110, height=25) #placement du label
preterit = Label(frame, text="Preterit", font=("Courrier", 10), bg='#FF7433', fg='white')
preterit.place(x=-110, y=-90, width=110, height=25)
participe = Label(frame, text="Participe Passé", font=("Courrier", 10), bg='#FF7433', fg='white')
participe.place(x=10, y=-90, width=110, height=25)
traduction = Label(frame, text="Traduction", font=("Courrier", 10), bg='#FF7433', fg='white')
traduction.place(x=130, y=-90, width=110, height=25)

#reponse
reponset = Label(frame, text="La partie manquante est ", font=("Courrier", 10), bg='#DEF6FF', fg='black')
reponset.place(x=-140, y=0, width=160, height=25)
reponse = Entry(frame, bg='#DEF6FF', font=("Courrier", 10), fg='blue', relief='groove', borderwidth=0) #entrée de texte ou le joueur rentre sa réponse
reponse.place(x=10, y=0, width=110, height=25) #placement de l'entrée
bas = Label(frame, text="¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯", font=("Courrier", 10), bg='#DEF6FF', fg='black') #label __
bas.place(x=10, y=20, width=110, height=25) #placement du label
point = Label(frame, text=".", font=("Courrier", 15), bg='#DEF6FF', fg='black') #label .
point.place(x=120, y=0, width=5, height=25) #placement du label

#boutons
buttonv = Button(frame, text="VALIDER", font=("Courrier", 10), bg='#DEF6FF', fg='black', relief='groove', command = validate) #bouton valider qui appel la définition validate
buttonv.place(x=10, y=50, width=110, height=25) #placement du bouton
labelp = Label(frame, text=" ", font=("Courrier", 10), bg='#DEF6FF', fg='black')
labelp.pack(pady=25, fill=X) #label de hauteur 25 et de largeur ajustable

generate() #appel de la fonction generate

frame.pack(expand=YES) #affichage de la boite
window.mainloop() #met la fenetre en boucle principale
