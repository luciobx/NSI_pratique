---
author: Enzo Frémeaux
title: Nombres parfaits
tag:
  - boucle
  - tableau
---

# Diviseurs d'un nombre :

Un diviseur est un nombre qui en divise un autre. Le reste de cette division est nul.

Soit `n` un nombre et `d` le diviseur => Il faut que le reste de la division (obtenu grâce à `%`) soit nul :
- n%d == 0

Exemple : 
- 12 % 6 => 0 (Le reste vaut 0)
- 13 % 6 => 1 (Le reste vaut 1)



*Question 1 :*

Compléter une fonction `liste_des_diviseurs` qui prend un paramètre un nombre `nb` et qui renvoie un tableau contenant :

- Tous les diviseurs de nb (sauf lui-même)

Ex : 
```python
nombre = 152
liste_des_diviseurs(nombre)==[1, 2, 4, 8, 19, 38, 76]
```

# Nombres parfaits :



Un nombre parfait est un nombre qui est égal à la somme de ses diviseurs. (Sauf lui-même)

Par exemple : 28 est un nombre parfait car il est égal à la somme de ses diviseurs :  1 + 2 + 4 + 7 + 14

*Question 2 :*

Ecrire une fonction `est_parfait` prenant en paramètre un nombre `nb` et qui renvoie :

- True si le nombre est parfait 
- False s'il ne l'est pas

Ex :
```python
>>> est_parfait(28)
True
>>> est_parfait(15)
False
```