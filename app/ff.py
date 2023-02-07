from tkinter import *
from f import *

#callback
'''fonction de callback
indiquant qui a gagné
'''
def ok():
    p1=propositionJoueur(l.curselection()[0])
    p2=propositionMachine()
    r=shifumi(p1,p2)
    print(p1, p2, r)
    resultat="tu as gagné"
    if r==-1:
        resultat="pas de gagnant"
    elif r==1:
        resultat="tu as perdu"
    print(resultat)        
    f1.destroy()



#création de l'IHM
f1 = Tk()
f1.title("Shifumi")
b1=Button(f1,text='Jouer',command=ok)
l=Listbox(f1)
l.insert(0,"ciseaux")
l.insert(1, "feuille")
l.insert(2, "pierre")
l.pack();
b1.pack(side=LEFT,padx=10, pady=10)
#boucle infinie d'attente
f1.mainloop()