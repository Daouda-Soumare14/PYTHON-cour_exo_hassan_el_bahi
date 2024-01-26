# methode 1: utilisation de la boucle for
# syntaxe:
liste = [[60, 50.55, 1 ], ['rachid', 'eljay'], ['Python', 'PHP', 'HTML', 'CSS']]
for i in liste: # une première boucle qui va parcourir tous les elements de la liste
    for j in i: # une deuxième boucle qui va parcourir chaque element de la liste 
        print(j, end='\t') # end='\t' permet de rester dans la meme lisgne pour chaque liste et ajouter de l'espace
    print()

# methode 2: utilisation de la boucle for et range
# syntaxe:
print()
l = [[60, 50.55, 1 ], ['rachid', 'eljay'], ['Python', 'PHP', 'HTML', 'CSS']]
for i in range(len(l)): # une première boucle qui permet de creer une sequence des elements de la liste
    for j in range(len(l[i])): # une deuxième boucle permet d'afficher chaque element de la liste 
        print(l[i][j], end='\t') # end='\t' permet de rester dans la meme lisgne pour chaque liste et ajouter de l'espace
    print()