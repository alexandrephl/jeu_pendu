## Jeu du pendu ##

import random

## FONCTIONS
#ouverture du fichier contenant les mots
def obtenir_list_mots() :
    global mots
    with open("mots_pendu.txt", 'r') as f: 
        contenu = f.read()
    # mots est une liste globale qui contient tous les mots possibles
    mots = contenu.split()

#choix du mot parmis la liste des mots
def choisir_mot():
    global mot_choisi
    # on choisit un entier au hasard qui sert d'index pour choisir notre mot
    index_mot = random.randint(0, len(mots)-1)
    mot_choisi = mots[index_mot]

# correspond à un essai de lettre de l'utilisateur
def Essai():
    global lettres_trouvees
    trouve = False
    index_lettre_choisi = 0

    lettre_choisie = (input('entrez la lettre choisie : '))

    #on vérifie si la lettre choisie appartient à notre mot
    for caractere in mot_choisi :
        if caractere == lettre_choisie :
            trouve = True
            #si on a trouvé la lettre choisie, on cherche son ou ses index
            if index_lettre_choisi != 0 :
                index_lettre_choisi = mot_choisi.index(lettre_choisie,index_lettre_choisi+1)
            else :
                index_lettre_choisi = mot_choisi.index(lettre_choisie)
            #on met à jour la chaine des lettres trouvées
            lettres_trouvees = lettres_trouvees[:(index_lettre_choisi)] + lettre_choisie + lettres_trouvees[(index_lettre_choisi+1):]
    #retourne un booleen qui averti si l'essai est réussi ou non
    return trouve

#fonction globale qui contient la boucle du jeu
def Jouer():
    obtenir_list_mots()
    choisir_mot()

    global lettres_trouvees
    global mot_choisi
    lettres_trouvees = '_'*len(mot_choisi)
    Essais_restants = 6

    #Le jeu tourne tant que le nombre maximal d'essai n'est pas atteint et que le mot n'est pas trouvé
    while (Essais_restants > 0 and lettres_trouvees != mot_choisi):
        print(lettres_trouvees)
        print(f'Il te reste {Essais_restants} essais \n')
        if Essai():
           print('La lettre est dans le mot !')
        else :
            print('La lettre n\'est pas dans le mot')
            Essais_restants -= 1

    if lettres_trouvees == mot_choisi :
        print('BRAVO ! Tu as trouvé le mot')
    else : print(f'Tu as perdu.. Le mot était {mot_choisi}')

## MAIN CODE
print('VOICI LE JEU DU PENDU \nessaye de deviner le mot, tu as le droit à 6 mauvaises réponses :\n')
Jouer()
