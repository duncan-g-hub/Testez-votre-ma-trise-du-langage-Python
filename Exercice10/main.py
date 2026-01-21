## Écrivez votre code ici !

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_details(self):
        print(f"nom : {self.name}")
        print(f"age : {self.age}")


class Employee(Person):
    def __init__(self, name, age, salary):
        super().__init__(name, age)
        self.salary = salary

    def display_details(self):
        super().display_details()
        print(f"salaire : {self.salary}")


tim = Employee("Tim", 24, 1000)
tim.display_details()