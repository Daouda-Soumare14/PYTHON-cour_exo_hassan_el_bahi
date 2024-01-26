def rectangle():
    c = int(input("saisir le nombre de colonnes "))
    l = int(input("saisir le nombre de lignes"))

    for i in range(l):
        for j in range(c):
            print(" * ", end= " ")
        print()

rectangle()            