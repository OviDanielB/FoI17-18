"""
  * Problema delle torri di Hanoi (versione ricorsiva)
"""

def hanoi(N, begin, end, aux):
#@param N: disks number
#@param begin: begin point name (es. "A")
#@param end: end point name (es."C") 
#@param aux: helper point name (es. "B")

 # check 
  if begin == end or begin == aux or end == aux:
    print "ERR: begin, end and helper points' names must be different!"
    return

# recursive base
  if N == 1:
    printMove(begin, end)
    return

# recursive step
  hanoi(N-1, begin, aux, end)
  printMove(begin, end)
  hanoi(N-1, aux, end, begin)

i = 0
def printMove(x,y):
#@param x,y: string
  global i
  i += 1 # moves counter
  print "%d) Move a disk from %s to %s \n" % (i,x,y)
