class EnsembleDisjoint:
    """
    Implémentation de l'algorithme Union-Find (Ensemble Disjoint)
    pour vérifier la connectivité dans un réseau.
    """
    def __init__(self, n):
        """
        Initialiser l'ensemble disjoint avec n éléments.
        
        :param n: Nombre de sommets dans le réseau
        """
        self.parent = list(range(n))
        self.rang = [0] * n
    
    def trouver(self, x):
        """
        Trouver la racine de l'élément x en utilisant la méthode de compression de chemin.
        :param x: L'élément dont on veut trouver la racine
        :return: La racine de x
        """
        if self.parent[x] != x:
            self.parent[x] = self.trouver(self.parent[x])
        return self.parent[x]
    
    def fusionner(self, x, y):
        """
        Fusionner les ensembles contenant les éléments x et y.
        
        :param x: Premier élément
        :param y: Deuxième élément
        :return: True si la fusion a eu lieu, False si les éléments étaient déjà dans le même ensemble
        """
        racine_x, racine_y = self.trouver(x), self.trouver(y)
        if racine_x == racine_y:
            return False
        
        if self.rang[racine_x] < self.rang[racine_y]:
            racine_x, racine_y = racine_y, racine_x
        
        self.parent[racine_y] = racine_x
        if self.rang[racine_x] == self.rang[racine_y]:
            self.rang[racine_x] += 1
        
        return True
