## Écrivez votre code ici !
def square(x):
    if isinstance(x, int) or isinstance(x, float):
        return x*x
    else:
        print("Le paramètre doit etre un nombre !")
        return None



