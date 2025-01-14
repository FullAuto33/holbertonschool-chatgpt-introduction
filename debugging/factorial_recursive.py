#!/usr/bin/python3
import sys

def factorial(n):
    """
    **Description de la Fonction**
    -----------------------------
    Cette fonction calcule la factorielle d'un entier donné.

    **Paramètres**
    -------------
    * `n`: L'entier pour lequel la factorielle doit être calculée.

    **Retour**
    ----------
    * La factorielle de l'entier `n`.
    """
    if n == 0:
        # Cas de base : la factorielle de 0 est 1
        return 1
    else:
        # Cas récursif : n * factorielle de (n-1)
        return n * factorial(n-1)

# Calcule la factorielle de l'argument de ligne de commande
f = factorial(int(sys.argv[1]))
# Affiche le résultat
print(f)