---
author: Yannick Mulot
title: Inversion
tag:
  - tableau
  - boucle
---

# Message brouillé

L'un ou l'une de vos camarades a pris l'habitude de vous transmettre ses messages en inversant systématiquement les caractères afin de les protéger de toute lecture fortuite.

*Exemple :*
```python
"?idim ec enitnac al à elbmesne enuejéd nO !tulaS" # Version inversée
"Salut! On déjeune ensemble à la cantine ce midi?" # Version normale
```

Nous souhaitons disposer d'une fonction Python permettant d'inverser une chaîne de caractères et ainsi : 
- pouvoir lire les messages reçus en remettant les caractères dans le bon sens
- pouvoir à son tour inverser les caractères pour transmettre un message

*Exemple :*
```python
inverse_chaine("! ruojnoB")   # Bonjour !
inverse_chaine("Au revoir !") # ! riover uA
```

Afin de pouvoir travailler sur les chaînes de caractères, celles-ci devront être converties en **tableaux de caractères** et inversement.

*Conversion d'une chaine de caractères vers un tableau :*
```pycon
>>> list("chaine")
['c', 'h', 'a', 'i', 'n', 'e']
```

*Conversion d'un tableau de caractères vers une chaîne :*
```pycon
>>> "".join(['c', 'h', 'a', 'i', 'n', 'e'])
'chaine'
```
## Exercice 1

Compléter la procédure `echange` qui prend en paramètre un tableau `tab` ainsi que deux indices `i1` et `i2` et qui échange les valeurs de `tab[i1]` et `tab[i2]`. Les pré-conditions suivantes devront être respectées :

- `i1` supérieur ou égale à `0` et inférieur strictement à `len(tab)`
- `i2` supérieur ou égale à `0` et inférieur strictement à `len(tab)`

*Exemple :*
```pycon
>>> tab = list("tulas")
>>> tab
['t','u','l','a','s']
>>> echange(tab, 0, 4)
>>> tab
['s','u','l','a','t']
>>> echange(tab, 1, 3)
>>> tab
['s','a','l','u','t']
>>> "".join(tab)
'salut'
```

## Exercice 2

Compléter la procédure `inverse_tableau` qui prend en paramètre un tableau et en inverse toutes les valeurs.

*Exemple :*
```pycon
>>> tab = [2, 4, 6, 8]
>>> inverse_tableau(tab)
>>> tab
[8, 6, 4, 2]
```

Pour terminer, compléter la fonction `inverse_chaine` qui prend en paramètre une chaine de caractères et retourne la version inversée de celle-ci.

*Exemple :*
```pycon
>>> inverse_chaine("Salut tout le monde!")
'!ednom el tuot tulaS'
```