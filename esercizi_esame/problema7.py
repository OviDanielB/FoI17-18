"""
  * Problema 7
  * Si definisca una classe che ha come attributo una tupla di N interi aventi valore
  * iniziale 0, con N definito al momento della creazione di un oggetto della classe. Inoltre, la classe
  * dispone di un metodo per visualizzare tutta la tupla, e di un metodo per modificare l'attributo tupla
  * con una nuova tupla dove il valore k Ì¬ stato sommato all'elemento in posizione i della vecchia tupla.
  * Definire poi una classe derivata dalla prima, dove il valore iniziale del primo elemento della tupla
  * (possibilmente diverso da 0) puÌ? essere specificato al momento della creazione di un oggetto della
  * classe. Fornire, inoltre, alcuni frammenti di codice Python che esemplificano l'uso delle classi
  * (creazione di oggetti delle due classi, uso dei metodi).
"""
class Tuple:
 def __init__(self,N):
 #@param N: tuple lengh
  self.N = N
  self.t = (0,)
  for i in range(0, self.N - 1):
   self.t = self.t + (0,)
 
 def showTuple(self):
   print self.t
 
 def updateTuple(self,i,k):
 #@param i: item position
 #@param k: value to sum
  self.tlist = []
  for x in range(0, self.N):
   if x == i:
    self.tlist.append(self.t[x] + k)
   else:
    self.tlist.append(self.t[x])
  self.t = self.tlist
 
class ValueTuple(Tuple):
 def __init__(self, value, N):
 #@param value: init values
 #@param N: tuple lenght
  assert value != 0
  Tuple.__init__(self, N)
  lt = []
  lt = self.t
  self.t = (value,) + lt[1:]
 
 
# usage examples
t = ValueTuple(4,4)
t.showTuple()
t.updateTuple(1,5)
t.showTuple()