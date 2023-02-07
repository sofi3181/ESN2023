import random
'''Obtenir la proposition du joueur
Params: entier correspondant à la proposition
Return:"ciseaux", "feuille" ou "pierre"
'''
def propositionJoueur(i):
    print(i)
    tab=["ciseaux", "feuille", "pierre"]
    if i >=0 and i <len(tab) :
        return tab[i]
    else :
        return None

'''Obtenir la proposition de la machine
Params: -
Return:"ciseaux", "feuille" ou "pierre"
'''
def propositionMachine():
    tab=["ciseaux", "feuille", "pierre"]
    nb=random.randint(0,2)
    return(tab[nb])

'''Connaître le gagnant
Params: chaîne correspondant à la proposition du jouer
        chaîne correspondant à la proposition de la machine
Return:-1 en cas d'égalité, 0 si le joueur gagne, 1 si la machine gagne
'''
def shifumi(p1, p2):
    rep=1
    if p1 not in ["ciseaux", "feuille", "pierre"]:
        rep=None
    elif p2 not in ["ciseaux", "feuille", "pierre"]:
        rep=None
    elif p1==p2: 
        rep=-1
    elif p1=="pierre" and p2=="ciseaux" or p1=="feuille" and p2=="pierre" or p1=="ciseaux" and p2=="feuille":
        rep=0
    return rep

    
