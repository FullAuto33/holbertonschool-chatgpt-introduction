#!/usr/bin/python3
import sys

def factorial(n):
    """
    Calcule la factorielle d'un entier non négatif.

    Args:
        n (int): L'entier pour lequel calculer la factorielle.

    Returns:
        int: La factorielle de n.

    Raises:
        TypeError: Si n n'est pas un entier.
        ValueError: Si n est un entier négatif.
    """
    if not isinstance(n, int):
        raise TypeError("L'argument doit être un entier")
    if n < 0:
        raise ValueError("L'argument doit être un entier non négatif")
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n-1)

def main():
    """
    Point d'entrée du script.

    Vérifie les arguments de ligne de commande et calcule la factorielle de l'entier passé en argument.
    """
    if len(sys.argv) != 2:
        print("Usage: python script.py <entier>")
    else:
        try:
            n = int(sys.argv[1])
            f = factorial(n)
            print(f"La factorielle de {n} est {f}")
        except (TypeError, ValueError) as e:
            print(e)

if __name__ == "__main__":
    main()