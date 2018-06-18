"""
  * Esercizio 5
  * Definire in Python una classe Iterator che prende come parametro del costruttore una lista qualsiasi.
  * L’Iterator permette di attraversare la lista in entrambe le direzioni,
  * aggiungere e rimuovere un elemento subito dopo la posizione in cui si trova lungo la lista
  * e inoltre tiene traccia della posizione attuale nella lista. I metodi devono essere:
  *     - hasNext : ritorna vero se esiste un elemento dopo la posizione attuale, falso altrimenti
  *     - hasPrevious: ritorna vero se esiste un elemento prima della posizione attuale, falso altrimenti
  *     - next: ritorna l’elemento successivo alla posizione attuale
  *     - previous: ritorna l’elemento precedente alla posizione attuale
  *     - add: aggiunge un elemento subito dopo la posizione attuale
  *     - remove: rimuove l’elemento subito dopo la posizione attuale e lo ritorna
"""

class Iterator:
  def __init__(self,list):
  # @param list: List of Objects
    self.list = list
    self.length = len(list)
    # set position before first element (index 0)
    # if not empty array; else -2
    self.pos = -1 if self.length > 0 else -2

  def hasNext(self):
  # @return Bool: true if there is a next element,
  #               false otherwise
    return (self.pos < self.length - 1) and self.pos != -2

  def hasPrevious(self):
  # @return Bool: true if there is a previous element,
  #               false otherwise
    return self.pos >= 0

  def next(self):
  # @return Object: next element (if present)
    self.pos += 1 # update position
    return self.list[self.pos]

  def previous(self):
  # @return Object: previous element (if present)
    prev = self.list[self.pos]
    self.pos -= 1 #update position
    return prev

  def add(self,elem):
  # @param elem: Object to insert after curr. posit.
    self.list.insert(self.pos + 1,elem)
    self.length += 1 # update list length

  def remove(self):
  # @return Object: next element after curr. posit.
    self.length -= 1 # update list length
    return self.list.pop(self.pos + 1)

"""
  * Esercizio 6
  * Scrivere una funzione Python che, data un’immagine P e un float avg,
  * si scorre la lista (usando l’Iterator definito in precedenza ) dei pixel di P
  * e ritorna vero se almeno un pixel ha la media delle componenti
  * del proprio colore strettamente maggiore di avg e falso altrimenti.
"""


def checkColor(P,avg):
# @param P: Picture
# @param avg: Float
  i = Iterator(getPixels(P))
  while i.hasNext():
    if greaterThanAvgColor(i.next(),avg):
      return true
  return false

def greaterThanAvgColor(pixel,avg):
# @param pixel: Pixel
# @param avg: Float
  pAvg = (getRed(pixel) + getGreen(pixel) + getBlue(pixel) ) / 3
  return pAvg > avg
