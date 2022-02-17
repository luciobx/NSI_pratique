author: Alexis Craipeau
title: Racine numérique

---

# Trouver la racine numérique

On calcule la racine numérique d'un entier en additionnant tous les chiffres qui le composent jusqu'à n'en avoir plus qu'un. <-- à retravailler

**Exemples de calculs racine numérique :** 

```
123 --> 1 + 2 + 3 = 6
La racine numérique de 123 est 6. 

123456789 --> 1 + 2 + 3 + 4 + 5 + 6 + 7 + 8 + 9 = 45 --> 4 + 5 = 9
La racine numérique de 123456789 est 9. 
```

*(Les nombres dont la racine numérique est 3, par exemple, sont tous divisibles par 3.* 
*Les nombres dont la racine numérique est 9 sont tous divisibles par 9.)* <-- A enlever

On cherche à coder la fonction racine_numerique(nombre) qui, pour tout nombre, renvoie sa racine numérique.

Une racine numérique n'étant composée que d'un unique chiffre, une racine numérique ne peut avoir que pour valeur 0, 1, 2, 3, 4, 5, 6, 7, 8 ou 9.

**Exemples d'appels de racine_numerique(nombre) :**

```python
>>> racine_numerique(19)
1
>>> racine_numerique(123)
6
>>> racine_numerique(123456789)
45
```

