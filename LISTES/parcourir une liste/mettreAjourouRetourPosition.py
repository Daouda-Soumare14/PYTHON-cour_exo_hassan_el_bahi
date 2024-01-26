# si on veut mettre a jour un element ou retourner sa position, cous devez utiliser son 
# index. une facon courante de le faire est de combiner les foncions range() et len() 
# avec la boucle for

n = [11, 2, 4, 2, 13, 20, 17, 19]
for index in range(len(n)):
    print(index) # affiche le nombre d'element de la liste de maniere successive 