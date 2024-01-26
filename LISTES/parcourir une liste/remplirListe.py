# creer un programme qui demande a un enseignant de remplir trois listes.
# la premiere contient la liste des noms d'eleves et les deux autres contiennent
# les notes obtenues par les eleves dans deux matieres (taille 5). ensuite le 
# programme affiche la liste des eleves avec leurs moyennes

noms = []
notes1 = []
notes2 = []
for i in range(3):
    print(" saisir le nom de l'etudiant num ", i+1, " = ", end="") 
    noms.append(input())
    print(" saisir la note1 de l'etudiant num ", i+1, " = ", end="")
    notes1.append(float(input()))
    print(" saisir la note2 de l'etudiant num ", i+1, " = ", end="")
    notes2.append(float(input()))
for nom, note1, note2, in zip(noms, notes1, notes2):
    print(" la moyenne de ", nom, " = ", (note1 + note2)/2)    