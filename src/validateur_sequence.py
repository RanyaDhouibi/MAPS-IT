import heapq

class ValidateurSequence:
    """
    Utilitaire de validation pour les séquences de degrés.
    """
    @staticmethod
    def est_graphique(sequence_degres):
        """
        Vérifie si une séquence de degrés est graphique en utilisant le critère de Havel-Hakimi.
        
        Optimisation avec une structure de pile (priority queue) pour éviter un tri à chaque itération.
        :param sequence_degres: Liste des degrés des sommets
        :return: True si la séquence est graphique, False sinon
        """
        if not sequence_degres:
            return False

        # Trier la séquence initiale
        sequence_degres = [-deg for deg in sequence_degres]  # Utiliser des valeurs négatives pour simuler un max-heap
        heapq.heapify(sequence_degres)

        while sequence_degres and sequence_degres[0] < 0:
            # Extraire le plus grand élément (notez que nous avons utilisé des valeurs négatives)
            first = -heapq.heappop(sequence_degres)
            if first > len(sequence_degres):
                return False

            # Réduire les degrés des `first` premiers éléments
            temp = []
            for i in range(first):
                if not sequence_degres:
                    return False
                degree = -heapq.heappop(sequence_degres)
                degree -= 1
                if degree < 0:
                    return False
                temp.append(degree)

            # Réinsérer les éléments réduits dans la pile
            for degree in temp:
                heapq.heappush(sequence_degres, -degree)

        return True
