from tkinter import *

from f import essai
#callback
def ok():
    essai()
    f1.destroy()
#création de l'IHM
f1 = Tk()
f1.title("Premier exemple")
b1=Button(f1,text='Cliquez',command=ok)
b1.pack(side=LEFT,padx=10, pady=10)
#boucle infinie d'attente
f1.mainloop()