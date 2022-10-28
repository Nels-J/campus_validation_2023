"""
Créer un programme qui manipule une classe ListCalculate qui reçoit une liste d'entiers dans le constructeur.

Créer les classes qui héritent de ListCalculate et qui définissent la méthode calculer
- ListCalculateSum
- ListCalculateProduct

Créer une liste contenant des ListCalculateSum et des ListCalculateProduct
et afficher le résultat de chacune des listes
 """


class ListCalculate():
    def __init__(self, arg):
        self.args = arg
        print(arg)


class ListCalculateSum(ListCalculate):
    pass


class ListCalculateProduct(ListCalculate):
    pass


def main():
    nbr = [1, 2, 3, 6]
    ListCalculate(nbr)


if __name__ == "__main__":
    main()
