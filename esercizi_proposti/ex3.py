"""
  * Esecizio 3
  * Scrivere una funzione ricorsiva in Python che, data una string S, la inverte.
"""

# ===== prima variante =====
def recReverse(s):
  if s == "": # condizione uscita
    return s
  else:
    # l'ultimo elemento viene escluso
    # nella chiamata ricorsiva
    return s[-1] + recReverse(s[:-1])


# ===== seconda variante =====
def recReverse2(s):
  if s == "": # condizione uscita
    return s
  else:
    # il primo elemento viene escluso
    # nella chiamata ricorsiva
    return recReverse2(s[1:]) + s[0]
