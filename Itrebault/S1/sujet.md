author: Lena TREBAUL
title: Animal mystère

---

# Animal mystère

On dispose de caractéristiques sur des animaux : leur taille en cm et leur masse en kg, regroupées sous la forme d'une liste à laquelle on ajoute l'espèce de cet animal en première position. 

```python
donnee_animal = ['chat', 23, 3.5]
```

Les listes correspondant à différents animaux sont regroupées dans une même liste qui constitue un jeu de données `donnees_animaux`.

```python
donnees_animaux = [['chat', 23, 3.5], 
                   ['elephant', 660, 5225],
                   ['chat', 28, 4.2], 
                   ['singe', 60, 22],
                   ['elephant', 550, 4100],
                   ['poisson rouge', 10, 0.1]
                   ]
```

Si l'on dispose de ces caractéristiques pour un nouvel animal dont l'espèce n'est pas connue, on veut savoir quelles sont les espèces des animaux du jeu de données `donnees_animaux` ayant les caractéristiques les plus proches de cet animal.

Pour estimer si deux animaux $'a_{1}'$ et $a_{2}$ ayant les caractéristiques respectives $m_{1}$, $t_{1}$ et $m_{2}$, $t_{2}$ sont "proches", on utilise la formule suivante calculant leur distance $d$ : $d = \sqrt{ (t_{1}-t_{2})^2 + (m_{1}-m_{2})^2 }$

Chacun des animaux de la liste `donnees_animaux` correspond à une donnée dont on veut calculer la distance par rapport à une nouvelle donnée : notre animal mystère.

1. Compléter la fonction `calcule_distance` qui retourne la distance entre deux données `donnee1` et `donnee2` et vérifier son fonctionnement sur le test donné. On utilise la fonction `sqrt` de la bibliothèque `maths` pour calculer la racine carrée.
```python
from math import sqrt

def calcule_distance(donnee1, donnee2):
    d = sqrt((...-...)**2 + (...-...)**2)
    return d
```
```pycon
    >>> round(calcule_distance(['chat', 23, 3.5], ['elephant', 660, 5225])
    5260
```

Ces distances, ainsi que l'indice `i` de l'animal correspondant dans la liste `donnees_animaux`, sont rangées par ordre croissant avec la méthode `sort` dans la fonction principale `k_plus_proches` et on sélectionne les `k` (entier) animaux les plus proches de notre animal mystère.


2. La fonction principale `k_plus_proches` prend en paramètres un nouvel animal `donnee` dont on ne connait pas l'espèce, un ensemble d'animaux `jeu_donnees` et un entier `k`, et retourne la liste des espèces de ces `k` voisins. La compléter et tester son bon fonctionnement sur les exemples suivants :

```python
def k_plus_proches(donnee, jeu_donnees, k):
    
    distances = []
    for i in range(len(jeu_donnees)):
        distances.append([calcule_distance(donnee, ...), i])
    distances.sort()
    
    voisins = []
    for i in range(...):
        voisins.append(jeu_donnees[distances[i][1][...]])
        
    return ...
```

```pycon
    >>> k_plus_proches(['mystère', 25, 4], donnees_animaux, 3)
    ['chat', 'chat', 'poisson rouge']
    >>> k_plus_proches(['mystère', 500, 3800], donnees_animaux, 2)
    ['elephant', 'elephant']
```





