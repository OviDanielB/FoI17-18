"""
  * Esercizio 9
  * Data una lista l di interi, scrivere una funzione ricorsiva in Python che ordini gli elementi di l in modo crescente.
  * Suggerimento: Se la lista contiene n elementi posizionare al primo posto l’elemento massimo e ordinare gli n-1
  * elementi restanti.
"""

def order(list):
# @param list: List of numbers
# @return List: sorted initial list
  if len(list) == 0:
    return list
  else:
    index = findMinIndex(list)
    # after pop the list has item at index removed
    return [list.pop(index)] + order(list)

def findMinIndex(list):
# @param list: List of numbers (not empty)
# @return Int: index of elem with
#              minimum value
  min = list[0]
  index = 0
  for i in range(0, len(list)):
   if(list[i] < min):
     min = list[i]
     index = i
  return index
