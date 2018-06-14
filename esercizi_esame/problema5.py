"""
  * Problema 5
  * Si definisca una classe PoligonoRegolare. Ogni oggetto della classe ha come attributi
  * il numero di lati e la lunghezza di un lato, e come operazioni due metodi che restituiscono,
  * rispettivamente, la lunghezza del lato e il perimetro del poligono. Si definisca inoltre una classe
  * Qadrato, derivata dalla classe PoligonoRegolare, che ha un metodo aggiuntivo che restituisce l'area
  * del quadrato. Dare la definizione completa delle due classi in Python, che include la definizione dei
  * rispettivi costruttori e dei metodi indicati. Fornire, inoltre, alcuni frammenti di codice Python che
  * esemplificano l'uso delle classi (creazione di oggetti delle due classi, uso dei metodi).
"""

class PoligonoRegolare:

  def __init__(self, n, len):
  # @param n: Int
  # @param len: Float
    self.n = n
    self.len = len
    
  def getLen(self):
    return self.len
    
  def getPerimetro(self):
    return self.n * self.len
    

class Quadrato(PoligonoRegolare):
  
  def __init__(self, len):
    PoligonoRegolare.__init__(self,4, len)
    
  def getArea(self):
    return self.len * self.len
    
    
# usage examples
poligono = PoligonoRegolare(5, 2.5)
poligono.getLen() # 2.5
poligono.getPerimetro() # 12.5

quadrato = Quadrato(2)
quadrato.getLen() # 2
quadrato.getPerimetro() # 8
quadrato.getArea() # 4

poligono.getArea() # ERRORE: metodo definito solo per classe Quadrato
