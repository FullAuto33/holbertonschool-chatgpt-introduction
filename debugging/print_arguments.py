#!/usr/bin/python3
import sys

def main():
    """
    Point d'entrée du script.

    Vérifie les arguments de ligne de commande et les affiche.
    """
    if len(sys.argv) > 1:
        print("Arguments :")
        for i in range(1, len(sys.argv)):
            print(sys.argv[i])
    else:
        print("Aucun argument fourni.")

if __name__ == "__main__":
    main()