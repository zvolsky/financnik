#!/bin/env/python3

"""
    Takto uspořádaný soubor se může 1) importovat, 2) spouštět jako script.

    1. import bude fungovat, když
        - mám soubor ve stejném adresáři jako odkud jsem spustil python
        - nebo když adresář, kde mám soubor, přidám do sys.path:
            import sys
            sys.path.append("cesta/k/tomuto/souboru")
    - import zkus_import, potom: zkus_import.DEFAULT_CINITEL, nebo: zkus_import.soucin(5, 4)
    nebo podobně:
    - from zkus_import import soucin, potom: soucin(5, 4)

    2. jako skript:
    python zkus_import.py
"""


DEFAULT_CINITEL = 3      # konstanty (jednou nastavené a jen výjimečně měněné údaje)


def soucin(a, b=DEFAULT_CINITEL):
    print("toto se provede jen když zavoláme funkci soucin()")
    return a * b


print("toto se provede vždy (při importu i volání jako skript) - ale takovýto společný kód se nepoužívá")
print("modul se zpracovává pod jménem {}".format(__name__))


if __name__ == '__main__':    # tato podmínka není splněná při importu
    # tady se může pomocí modulu argparse větvit podle případných argumentů příkazu

    print("toto se provede jen při volání jako skript: python -m zkus_import.py")
    print("Součin je {}".format(soucin(4)))
