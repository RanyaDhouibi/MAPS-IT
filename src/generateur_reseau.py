from .ensemble_disjoint import EnsembleDisjoint
from .validateur_sequence import ValidateurSequence

class GenerateurReseau:
    """
    Générateur de réseaux de communication avec contraintes.
    """
    def __init__(self, sequence_degres):
        """
        Initialiser le générateur avec la séquence de degrés fournie.

        :param sequence_degres: Liste des degrés des sommets
        """
        self.sequence_degres = sorted(sequence_degres, reverse=True)
        self.n = len(sequence_degres)
        
        if not ValidateurSequence.est_graphique(sequence_degres):
            raise ValueError("Séquence de degrés invalide")
    
    def _etiquette_canonique(self, reseau):
        """
        Retourne une étiquette canonique pour un réseau donné. Cette étiquette est une version triée
        des connexions dans le réseau, afin d'éviter les duplications dues à l'ordre des connexions.

        :param reseau: Liste des connexions entre les sommets
        :return: Tuple représentant l'étiquette canonique
        """
        return tuple(
            tuple(sorted(connexions)) 
            for connexions in reseau
        )

    def generer_reseaux(self):
        """
        Génère tous les réseaux uniques possibles en fonction de la séquence de degrés donnée.

        :return: Liste des réseaux uniques
        """
        reseaux_uniques = set()

        def recherche_arriere(reseau, degres_restants):
            """
            Fonction récursive pour explorer toutes les possibilités de connexions dans le réseau.

            :param reseau: Liste représentant les connexions entre les sommets
            :param degres_restants: Liste des degrés restants pour chaque sommet
            """
            if all(d == 0 for d in degres_restants):
                ensemble_disjoint = EnsembleDisjoint(self.n)
                for u in range(self.n):
                    for v in reseau[u]:
                        ensemble_disjoint.fusionner(u, v)
                
                racine = ensemble_disjoint.trouver(0)
                if all(ensemble_disjoint.trouver(v) == racine for v in range(1, self.n)):
                    etiquette_canonique = self._etiquette_canonique(reseau)
                    reseaux_uniques.add(etiquette_canonique)
                return

            for u in range(self.n):
                if degres_restants[u] > 0:
                    for v in range(u + 1, self.n):
                        if (degres_restants[v] > 0 and 
                            v not in reseau[u] and 
                            u not in reseau[v]):
                            
                            reseau[u].append(v)
                            reseau[v].append(u)
                            degres_restants[u] -= 1
                            degres_restants[v] -= 1
                            
                            recherche_arriere(reseau, degres_restants)
                            
                            reseau[u].remove(v)
                            reseau[v].remove(u)
                            degres_restants[u] += 1
                            degres_restants[v] += 1

        reseau_initial = [[] for _ in range(self.n)]
        degres_initiaux = self.sequence_degres.copy()
        recherche_arriere(reseau_initial, degres_initiaux)

        return [
            [list(connexions) for connexions in reseau] 
            for reseau in reseaux_uniques
        ]
