# ecrire un programme qui permet de:
#     1) demander a l'utilisateur d'entrer un nombre positif
#     2) afficher la serie de nombre de 1 à N 
#     3) afficher la serie de nombres pairs entre 1 à N
#     4) afficher la serie de nombres impairs entre 1 à N
#     5) afficher les 4 premiers elements de la liste
#     6) afficher a partir du 6ème elements jusqu'a la fin
#     7) afficher les 2 dernieres elements de la liste
#     8) afficher les elements 1 3 5 7 9 de la liste avec uniquement le decoupage
#     9) afficher la liste en exluant le premier element de la liste et les 3 derniers elements de la liste

# question1
N = int(input(' saisir la valeur de n '))
while N < 1:
    N = int(input(' saisir la valeur de n '))
# question2
L1 = list(range(1, N + 1))
print(L1)
# question3
L2 = list(range(0, N + 1, 2))
print(L2)
# question4
L3 = list(range(1, N + 1, 2))
print(L3)
# question5
L4 = [1, 2, 3, 4, 5, 6, 7, 8]
print(L4[0], L4[1], L4[2], L4[3]) # methode 1
print(L4 [0 : 4]) # methode 2 affiche sous forma de liste
# question6
L5 = [1, 2, 3, 4, 5, 6, 7, 8]
print(L5[6], L5[7]) # methode 1
print(L5 [6 : 8]) # methode 2 affiche sous forma de liste
# question7
L6 = [1, 2, 3, 4, 5, 6, 7, 8]
print(L6[-2], L6[-1]) # methode 1
print(L6 [6 : 8]) # methode 2 affiche sous forma de liste
# question8
L7 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(L7 [0 :: 2]) 
# question9
L8 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(L8 [1 : -3]) 



# note a retenir : pour acceder au element de la liste on peut utiliser l'indexation positif comme negatif
