# -*- coding:Latin-1 -*

import os 
from random import randrange
from math import ceil

argent = 1000
continuer_partie = True 


#chiffretire = random.randrange(50)
#print("chiffre :  + chiffretire")

while continuer_partie:
    nombre_mise = -1
    while nombre_mise < 0 or nombre_mise > 49:
        nombre_mise = input("Encodez le nombre que vous voulez miser, entre 0 et 49 : ")
        try:
            nombre_mise = int(nombre_mise)
        except ValueError:
            print("vous n'avez pas saisi de nombre")
            nombre_mise = -1
            continue
        if nombre_mise < 0:
            print("ce nombre est inférieur à 0 !")
        if nombre_mise > 49:
            print("ce nombre est supérieur à 49 !")
            
    mise = 0
    while mise <= 0 or mise > argent:
        mise = input("Encodez votre mise : ")
        try:
            mise = int(mise)
        except ValueError:
            print("vous n'avez pas saisi de nombre")
            mise = -1
            continue
        if mise < 0:
            print("la mise est inférieure à 0 !")
        if mise > argent:
            print("La mise est superieure à l'argent disponible")
     
    
    numero_gagnant = randrange(50)
    print("La roulette tourne et s'arrete sur le numero .... ", numero_gagnant)
    if numero_gagnant == nombre_mise:
        print("Felicitations ! Vous avez gagne")    
        argent += mise*3
    elif numero_gagnant % 2 == nombre_mise % 2:
        mise = ceil(mise * 0.5)
        print("Bonne couleur ! Vous gagnez ",mise, "$" )    
        argent += mise
    else:
        print("Desole .... vous perdez votre mise ",mise, "$")
        argent -= mise
    
    if argent <= 0:
        print("Vous etes ruine ... fin de la partie")
        continuer_partie = False
    else:
        print("Vous avez a present ",argent,"$")
        quitter = input("Souhaitez-vous quitter le casino (o/n) ?")
        if quitter == 'o' or quitter == 'O':
            print("Vous quitter le casino avec ", argent,"$")
            continuer_partie = False
            
os.system("pause")
            

