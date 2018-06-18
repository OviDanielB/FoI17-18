"""
  * Esercizio 7
  * Definire in Python una classe Knapsack (zaino) che prende come parametro del costruttore un numero intero positivo C
  * che indica la capacit ́a massima dello zaino. La classe ha come attributo una lista di Item
  * (a sua volta una classe con un nome e un numero intero positivo che indica l’occupazione nello zaino)
  * e permette l’inserimento di un Item solo se non viene ecceduta la sua capacita' massima aggiungendo l’occupazione dell’Item.
  * Inoltre il Knapsack deve tenere traccia e ritornare su richiesta lo spazio rimanente,
  * il numero di elementi al suo interno, l’elemento con occupazione massima e quello con occupazione minima.
"""

class Item:
  def __init__(self,name,occup):
  # @param name: String; item name
  # @param occup: Integer; item space req.
    self.name = name
    self.occup = occup
  def __str__(self): # method printing item
    return "Name: %s, Space requirement: %d" % (self.name, self.occup)
  def __repr__(self): # method printing item when in a list
    return "%s,%d" % (self.name, self.occup)

class Knapsack:
  def __init__(self,c):
  # @param c: Integer; maximum capacity
    self.maxC = c
    self.rem = c
    self.list = []
    # keep track of min and max
    # avoiding to compute it every
    # time it's needed; initialized to None
    self.max = None
    self.min = None

  def insert(self,item):
  # @param item: Item to be inserted
  # @return Bool: true if inserted,false otherwise
    if item.occup <= self.rem:
      # item can fit into knapsack
      self.list.append(item)
      self.rem -= item.occup # update remaining space
      # update max and min with new item
      self.max = self.__maxItem(self.max,item)
      self.min = self.__minItem(self.min,item)
      print "Remaining " + str(self.rem)
      return true
    print "Can't insert item. Not enough space left!"
    return false # item doesn't fit

  def getMax(self):
  # @return Item: with max space requirement
    return self.max

  def getMin(self):
  # @return Item: with min space requirement
    return self.min

  def remainingSpace(self):
  # @return Integer: remaining space (>= 0)
    return self.rem

  def itemsCount(self):
  # @return Integer: number of Items inserted
    return len(self.list)

  def __maxItem(self,item1,item2):
  # @param item1,item2: Item to be compared
  #??@return Item: with max space req. between item1 and 2
    return (item1 if item1 != None and item1.occup >= item2.occup
                 else item2)
                 
  def __minItem(self,item1,item2):
  # @param item1,item2: Item to be compared
  #??@return Item: with min space req. between item1 and 2
    return (item1 if item1 != None and item1.occup < item2.occup
                 else item2)


"""
  * Esercizio 8
  * Presi in considerazione il Knapsack e i relativi Item definiti nell’esercizio precedente,
  * una matrice (rappresentata come lista di liste) A di dimensioni NxM che ha come elementi istanze
  * di Item e un numero intero positivo T, scrivere una funzione in Python che per ogni colonna di A
  * crea un Knapsack di capacit ́a T e ritorna vero se, per ogni colonna di A, tutti gli item
  * della relativa colonna possono essere inseriti nell’i-esimo Knapsack, altrimenti falso.
"""

import random as rnd

def fitInKnapsackMatrix(A,T):
# @param A: List of Lists of Items
# @param T: Integer; single knapsack capacity
  assert len(A) > 0 and len(A[0]) > 0, "Matrix must not be empty!"
  for x in range(len(A[0])):
    k = Knapsack(T)
    for y in range(len(A)):
      if not k.insert(A[y][x]):
        return false
  return true


def randomItemMatrix(n,m,cap):
# @param n,m: Integer; matrix dimensions
# @param cap: Integer: maximum random item size
# @return List of Lists with random Items
  matrix = []
  for x in range(n):
    matrix.append([])
    for y in range(m):
      randomItem = Item("it" + str(x) + "-" + str(y),
             int(rnd.random() * cap % cap) )
      matrix[x].append(randomItem)
  print matrix
  return matrix
