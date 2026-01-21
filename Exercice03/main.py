words = ["python", "programmation", "langage", "ordinateur", "apprentissage"]

voyelles = ["a", "e", "i", "o", "u", "y"]

liste_tuple = [(word , sum(1 for letter in word if letter in voyelles)) for word in words]
print(liste_tuple)

