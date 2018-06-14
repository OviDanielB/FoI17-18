"""
  * Problema 1
  * Scrivere una funzione ricorsiva che, data una stringa s, restituisce vero se la stringa
  * contiene la stessa quantità di cifre numeriche e caratteri alfabetici, falso altrimenti. Nota: ricordare i
  * metodi isdigit() e isalpha() del tipo di dato str in Python.
"""

def check(s, a, n):
#@param s: string to check
#@param a: counter for alpha character
#@param n: counter for digit character
#@return : Boolean
  
  #recursive base
  if len(s) == 0:
    return (a == n)
    
  #recursive step
  if s[0].isalpha():
    return check(s[1:], a+1, n)
  elif s[0].isdigit():
    return check(s[1:], a, n+1)
    

# usage examples 
print check("c1c2",0,0)  #true
print check("c1c2x",0,0) #false