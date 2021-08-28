import random

essai = input("Pile ou face ? ")
n = random.randint(1, 2)

if n == 1:
    choix = "face"
else:
    choix = "pile"

print(choix)

if essai == choix:
    print("C'est gagné !!")
else: 
    print("Vous avez perdu !!")