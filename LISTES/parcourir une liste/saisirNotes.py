# ecrire un programme qui peut demander a l'utilisateur de 
# saisir les nores des etudiants (10) puis le programme affiche la 
# liste des notes des etudiants

notes = []
for i in range(9):
    print("la note de l'etudiant ", i+1, " = ", end="")
    notes.append(float(input()))
    
for i, note in enumerate(notes):
    print(" la note num ", i+1," = ", note)    