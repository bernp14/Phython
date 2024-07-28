# -*- coding:Latin-1 -*
# executer par commande python -m bissextile    
#           sans mettre l'extension ".py"

import os

annee = input("Saisissez une annee : ")
annee = int (annee)

if annee % 400 == 0 or ( annee % 4 == 0 and annee % 100 != 0):
    print("L'annee saisie est bissextile, appuyez sur une touche ...")
else:
    print("L'annee saisie n'est pas bissextile, appuyez sur une touche ...")

# programme en en pause pour eviter qu'il se referme sous windows 

os.system("read")
