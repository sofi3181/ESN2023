import random

def propositionJoueur(i):
    print(i)
    tab=["ciseaux", "feuille", "pierre"]
    if i >=0 and i <len(tab) :
        return tab[i]
    else :
        return None

def propositionMachine():
    tab=["ciseaux", "feuille", "pierre"]
    nb=random.randint(0,2)
    return(tab[nb])

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

    
