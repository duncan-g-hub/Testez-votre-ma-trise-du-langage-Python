## Écrivez votre code ici !

class BankAccount:
    def __init__(self, account_holder, balance):
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount):
        if  amount > 0:
            self.balance += amount
            print(f"{self.account_holder} dépose {amount}€ sur son compte bancaire.")
        else :
            print("Le montant à déposer doit etre supérieur à 0€.")

    def withdraw(self, amount):
        if amount > 0:
            if amount <= self.balance:
                self.balance -= amount
                print(f"{self.account_holder} retire {amount}€ de son compte bancaire.")
            else :
                print("Le montant à retirer doit etre inférieur ou égale au solde du compte.")
        else:
            print("Le montant à retirer doit etre supérieur à 0€.")

    def display_balance(self):
        print(f"{self.account_holder} possède {self.balance}€ sur son compte bancaire.")


tim = BankAccount("Tim", 100)
tim.deposit(2.5)
tim.withdraw(100)
tim.display_balance()
