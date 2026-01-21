students = {
    'Alice': {
         'Mathematiques': 90,
         'Francais': 80,
         'Histoire': 95
    },
    'Bob': {
         'Mathematiques': 75,
         'Francais': 85,
         'Histoire': 70
    },
     'Charlie': {
         'Mathematiques': 88,
         'Francais': 92,
         'Histoire': 78
     }
}

name = input("Entrez le nom de l'étudiant : ").title()

if students.get(name):
    print(f"Notes de {name} : ")
    notes = []
    for matiere, note in students[name].items():
        print(f"{matiere} : {note}")
        notes.append(note)
    moyenne = round(sum(notes) / len(notes), 2)
    print(f"Moyenne de {name} : {moyenne}")

else:
    print(f"L'étudiant {name} n'existe pas dans la liste.")

