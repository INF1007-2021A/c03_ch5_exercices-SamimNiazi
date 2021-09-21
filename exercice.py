#!/usr/bin/env python
# -*- coding: utf-8 -*-


from typing import List


def convert_to_absolute(number: float) -> float:
    if number < 0:
        number = -1 * number
    return number

    

def use_prefixes() -> List[str]:
    prefixes, suffixe = 'JKLMNOPQ', 'ack'
    nombre_combines = []
    for lettre in prefixes:
        nombre_combines.append (lettre + suffixe)
    return nombre_combines

def prime_integer_summation() -> int:
    n = 2
    d = 2
    liste = [2]
    for i in range (540):
        n += 1
        d = 2
        while n % d != 0:
            d += 1
            if d == n:
                liste.append(n)
    return sum(liste)

def factorial(number: int) -> int:
    factoriel = 1
    for chiffre in range(1,(number+1)):
        factoriel *= chiffre
    return factoriel


def use_continue() -> None:
    liste2=[]
    for chiffres in range(1,11):
        if chiffres != 5:
            liste2.append(chiffres)   
    return liste2


def verify_ages(groups: List[List[int]]) -> List[bool]:
    liste3 = []
    for list in groups:
        if len(list) < 3:
            liste3.append (False)
            continue
        elif len (list) > 10:
            liste3.append (False)
            continue
        else:
            for x in list:
                if x == 25:
                    liste3.append (True)
                    break
                elif x < 18:
                    liste3.append (False)
                    break
                elif x > 70 and 50 in list:
                    liste3.append (False)
                    break
                else: 
                    liste3.append (True)
                    break

    return liste3


def main() -> None:
    number = -4.325
    print(f"La valeur absolue du nombre {number} est {convert_to_absolute(number)}")

    print(f"La liste des noms générés avec les préfixes est: {use_prefixes()}")

    print(f"La somme des 100 premiers nombre premier est : {prime_integer_summation()}")

    number = 10
    print(f"La factiorelle du nombre {number} est: {factorial(number)}")
    
    print(f"L'affichage de la boucle est:")
    use_continue()

    groups = [
        [15, 28, 65, 70, 72], [18, 24, 22, 50, 70], [25, 2],
              [20, 22, 23, 24, 18, 75, 51, 49, 100, 18, 20, 20], [70, 50, 26, 28], [75, 50, 18, 25],
              [13, 25, 80, 15], [20, 30, 40, 50, 60], [75, 50, 100, 28]
    ]
    print(f"Les différents groupes sont: {groups}")
    print(f"L'acceptance des groupes est: {verify_ages(groups)}")


if __name__ == '__main__':
    main()
