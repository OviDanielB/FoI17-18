"""
  * Esercizio 2
  * Scrivere una funzione ricorsiva in Python che, dati due interi positivi a e b, calcola a^b.
  *
  * Condizioni d'uscita dalla ricorsione :
  *     - se b = 0  =>  a^b = 1 per qualsiasi a
  *     - se a = 0  =>  a^b = 0 per qualsiasi b
  *     - se b = 1  =>  a^b = a per qualsiasi a
"""


def posRecPower(a,b):
# @param a,b: Number
# @return : Number; a^b
# definita solo per b > 0
  assert b >= 0, "b must be >= 0"
  if   b==0: return 1
  elif a==0: return 0
  elif b==1: return a
  else:
    return a * posRecPower(a,b-1)


def recPower(a,b):
# @param a,b: Number
# @return : Number; a^b
# definita per ogni b (anche negativi)
# usando la funzione per b positivi (posRecPower)
  return (posRecPower(a, b) if b >= 0 else 1.0 / posRecPower(a, -b))
