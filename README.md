#Ranya Dhouibi
# Réseau de Communication - Générateur de Réseaux

Ce projet permet de générer des configurations uniques pour un réseau de communication entre des stations de travail dans un immeuble de bureaux. Chaque station a un nombre de connexions spécifique à d'autres stations, et le générateur respecte des contraintes de connectivité simple tout en garantissant que les réseaux générés ne soient pas isomorphes entre eux.

## Objectif

L'objectif de ce projet est de générer différentes configurations de réseaux basées sur une séquence de degrés fournie en entrée. Chaque degré définit le nombre de connexions d'une station avec d'autres stations.

## Fonctionnalités

- **Validation de la séquence de degrés** : Vérifie si la séquence de degrés donnée peut former un réseau valide.
- **Génération de réseaux uniques** : Génère plusieurs configurations de réseaux qui respectent la séquence de degrés et les contraintes de connectivité.
- **Éviter les graphes isomorphes** : Utilise une représentation canonique des réseaux pour s'assurer que les réseaux générés ne sont pas isomorphes.

## Entrées

- **Séquence de degrés** : La séquence de degrés définit le nombre de connexions pour chaque station de travail dans le réseau.
  
  Exemple d'entrée :
  ```python
  [3, 3, 2, 3, 3, 2]
