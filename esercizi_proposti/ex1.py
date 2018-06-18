"""
  * Esercizio 1
  * Data una lista L di interi con possibili liste annidate al suo interno,
  * scrivere una funzione ricorsiva in Python per ognuno dei seguenti punti:
  *    (a) determinare la somma di tutti i valori contenuti in L (anche quelli nelle liste annidate)
  *    (b) determinare il massimo valore contenuto in L (considerando anche i valori nelle liste annidate)
"""

# ===== punto (a) =====

def listOfListSum(list):
# @param list: List of lists of integers
# @return : Int; sum of all elements of list
  total = 0
  for element in list:
    if type(element) == type([]):
      total += listOfListSum(element)  # recursive call
    else:
      total += element
  return total


# ===== punto (b) =====

def recursiveMax(list):
# @param list: List of List of integers
# @return : Integer; max of all values of list
  assert len(list) > 0, "List is empty"
  max = 0
  for element in list:
    if type(element) == type([]):
      max = greatest(max,recursiveMax(element)) # recursive call
    else:
      max = greatest(max,element)
  return max

def greatest(n,m):
# @param n,m: Integer
# @return : Integer; greatest between m and n
  return (n if n >= m else m)
