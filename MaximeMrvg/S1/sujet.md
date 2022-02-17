---
author : Maxime Morvrange
title : Formule chimique brute
tag :
    - Dictionnaire
    - Chaine de caractères
---

# Écriture de formule chimique brute

En chimie, il existe 4 principaux atomes : le carbone, l'hydrogène, l'oxygène, et l'azote, respectivement représentés par les lettres C, H, O et N. A partir de ces 4 atomes, il est possible de construire diverses molécules. Nous pouvons les représenter par une chaine de caractères, de cette manière :

```python
eau = "HOH"
dioxygene = "HH"
methane = "HHCHH"
```

Pour l'eau, on aurait donc 2 atomes d'hydrogène, et un atome d'oxygène.

*Question 1 :*

Compléter une fonction `dicoAtome` qui prend en paramètre une chaîne de caractères `molecule`, et qui renvoie un dictionnaire comportant, pour chaque atome présent, le nombre de fois où il apparait dans la formule.

*Question 2 :*

On souhaite maintenant, à partir du dictionnaire créé à la question précédente, reconstruire la formule chimique brute d'une molécule, en factorisant cette fois-ci toutes les lettres. \
Compléter une fonction `factoriser` qui prend en paramètre `dicoMolecule`, un dictionnaire. Cette fonction doit retourner une chaine de caractères comprenant les atomes et le nombre de fois où ils sont présents.

```python
>>> methane = {"C":1,"H":4,"O":0,"N":0}
>>> factoriser(methane)
"CH4"
>>> eau = dicoAtome("HOH")
>>> factoriser(eau) == "H20"
True
```
