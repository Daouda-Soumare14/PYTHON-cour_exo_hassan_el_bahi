def nombreCompris():
    N = int(input("saisir un nombre compris entre 10 et 20 "))
    while N < 10 or N > 20:
        if N < 10:
            print("plus petit")
        else:
            print("plus grand")
        N = int(input("saisir un nombre compris entre 10 et 20 "))
    print("bravo! vous avez saisi un nombre compris entre 10 et 20")        

nombreCompris() 

# exo2 sur la boucle while
# saisir un nombre striqutement > a 1 puis calcul la somme
# des nombre de 1 jusqa'a ce nombre

def nombreSaisi():
    M = int(input("saisir un nombre > a 1 "))
    while M <= 1:
        M = int(input("saisir un nombre > a 1 "))
    S = 0
    i = 1 #a chaque fois qu'on connais une valeur a l'avance on initialise i a cette valeur de notre cas c 1
    while i <= M:
        S += i 
        i += 1
    print("la somme des valeurs compris entre 1 et le nombre saisi = {}".format(S))
    

nombreSaisi()        