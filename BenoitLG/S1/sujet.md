---
author: Benoît LE GOUIS
title: Somme des chiffres d'un nombre
---

# Somme des chiffres pour un nombre en écriture décimale

On veut calculer la somme des chiffres d'un nombre en écriture décimale. Ce genre d'opération est effectué de manière naturelle en primaire pour déterminer si un nombre
est un multiple de 3 ou de 9 : on fait la somme de ses chiffres, et on regarde si cette somme est elle-même un multiple de 3 ou de 9. 

En revanche, là où il est très facile pour un humain de savoir quels chiffres composent un nombre, cette décomposition ne va pas de soi pour un ordinateur.
Cet exercice demande donc dans un premier temps d'effectuer la somme des chiffres dans un tableau, et ensuite de compter de combien de chaque chiffre un nombre est composé.

*Question 1 :*
Compléter la fonction `somme_chiffres` qui prend en argument un tableau d'occurrences de chiffres `tableau_chiffres` de taille 10, contenant pour `0 <= i <= 9` le nombre de fois qu'on a chaque chiffre 'i' et qui renvoie la somme des chiffres ainsi comptés.

!!! example "Exemples"

    ```pycon
    >>> somme_chiffres([0, 3, 2, 1, 0, 0, 0, 0, 0, 0])
    10
	>>> somme_chiffres([1, 1, 1, 1, 1, 1, 1, 1, 1, 1])
	45
    ```


*Question 2 :*
Compléter la fonction `decomposition` qui prend en argument un nombre entier positif `nombre` et qui renvoie le tableau `tab` tel que pour `0 <= i <= 9`, 
`tab[i]` contient le nombre d'occurrences de `i` dans `nombre`.
On rappelle que l'opérateur % en python correspond au modulo.


!!! example "Exemples"

    ```pycon
    >>> decomposition(111223)
    [0, 3, 2, 1, 0, 0, 0, 0, 0, 0]
	>>> decomposition(1234567890)
	[1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
    ```

{{ IDE('exo') }}