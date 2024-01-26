# ecrire un programme qui demande a l'utilisateur de saisir les valeurs
# de deux variables A et B, ensuite, il permet de definir et d'appeler 
# les fonctions suivantes.
# - une fonction qui retourne si les valeurs de A et B sont de meme signe
#     ou non.(une fonction sans valeur de retour et avec arguments)
# - une fonction qui renvoie le minimum de A et B. 
#     (une fonction avec une valeur de retour et avec arguments)
# - une fonction qui renvoie le maximum de A et B.
#     (une fonction avec une valeur de retour et avec arguments)


# definition des fonctions
def signe(A, B):
    if A * B > 0:
        print(" les valeurs A et B ont de meme signe ")
    else:
        print(" les valeurs de A et B ont des signes differents") 

def minimum(A, B):
    if A < B:
        return A
    else:
        return B  

def maximum(A, B):
    if A > B:
        return A
    else:
        return B              
    
# l'appel des fonctions
A = int(input(" saisir la valeur de A : "))
B = int(input(" saisir la valeur de B : "))
signe(A, B)
C = minimum(A, B)
print(" la valeur min = ", C)
print(" la valeur max = ", maximum(A, B))
