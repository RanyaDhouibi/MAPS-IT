import unittest
import sys
import os

# Ajouter le répertoire 'src' au sys.path pour permettre les bons imports
from src.validateur_sequence import ValidateurSequence
from src.generateur_reseau import GenerateurReseau

class TestValidateurSequence(unittest.TestCase):
    """Test de la classe ValidateurSequence."""
    
    def test_est_graphique_valide(self):
        """Test des séquences de degrés graphiques valides."""
        self.assertTrue(ValidateurSequence.est_graphique([3, 3, 2, 3, 3, 2]))
        self.assertTrue(ValidateurSequence.est_graphique([2, 2, 2, 2]))
        self.assertTrue(ValidateurSequence.est_graphique([4, 3, 3, 2, 2, 2]))

    def test_est_graphique_invalide(self):
        """Test des séquences de degrés graphiques invalides."""
        self.assertFalse(ValidateurSequence.est_graphique([5, 3, 2, 2]))  # Séquence de degrés invalide
        self.assertFalse(ValidateurSequence.est_graphique([1, 1, 1, 1, 1]))  # Séquence de degrés invalide

    def test_est_graphique_sequence_vide(self):
        """Test pour une séquence vide (devrait être invalide)."""
        self.assertFalse(ValidateurSequence.est_graphique([]))  # Séquence vide devrait être invalide

class TestGenerateurReseau(unittest.TestCase):
    """Test de la classe GenerateurReseau."""

    def test_generation_reseaux(self):
        """Test de la génération de réseaux avec une séquence de degrés valide."""
        sequence = [3, 3, 2, 3, 3, 2]
        generateur = GenerateurReseau(sequence)
        reseaux = generateur.generer_reseaux()
        
        self.assertEqual(len(reseaux), 54)  # Supposons que 54 réseaux soient générés pour cette séquence
        self.assertIsInstance(reseaux, list)  # Vérifier que l'objet généré est une liste
        self.assertGreater(len(reseaux), 0)  # S'assurer qu'au moins un réseau est généré

    def test_generation_aucun_reseau(self):
        """Test qu'une erreur est levée pour une séquence de degrés invalide."""
        with self.assertRaises(ValueError):
            generateur = GenerateurReseau([5, 3, 2, 2])  # Séquence de degrés invalide
            generateur.generer_reseaux()

    def test_connectivite(self):
        """Test de la connectivité des réseaux générés."""
        sequence = [2, 2, 2, 2]
        generateur = GenerateurReseau(sequence)
        reseaux = generateur.generer_reseaux()

        for reseau in reseaux:
            visited = [False] * len(reseau)  # Suivi des nœuds visités
            stack = [0]  # Démarrer le DFS depuis le nœud 0
            while stack:
                node = stack.pop()
                if not visited[node]:
                    visited[node] = True
                    stack.extend(reseau[node])  # Ajouter les nœuds adjacents à la pile
            
            self.assertTrue(all(visited))  # S'assurer que tous les nœuds sont visités, ce qui signifie que le graphe est connecté

    def test_generation_graphe_vide(self):
        """Test de la génération d'un graphe vide (devrait renvoyer une liste vide)."""
        sequence = [0, 0, 0, 0]  # Séquence représentant un graphe vide
        generateur = GenerateurReseau(sequence)
        reseaux = generateur.generer_reseaux()
        self.assertEqual(len(reseaux), 0)  # Aucun réseau ne devrait être généré

    def test_generation_reseau_avec_degres_max(self):
        """Test de la génération de réseaux avec une séquence de degrés maximale."""
        sequence = [3, 3, 3, 3, 3, 3, 3, 3]  # Exemple de séquence où tous les nœuds ont un degré maximal
        generateur = GenerateurReseau(sequence)
        reseaux = generateur.generer_reseaux()
        self.assertGreater(len(reseaux), 0)  # Des réseaux devraient être générés

if __name__ == "__main__":
    unittest.main()
