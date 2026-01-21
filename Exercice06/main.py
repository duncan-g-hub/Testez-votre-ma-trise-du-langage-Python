# Fonction calculate_average
def calculate_average(list_numbers: list[int]) -> float:
    return sum(list_numbers) / len(list_numbers)
 
# Exemple d'utilisation de la fonction
numbers = [10, 20, 30, 40, 50]
average = calculate_average(numbers)
print("La moyenne est :", average)
