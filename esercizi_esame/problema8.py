"""
  * Problema 8
  *  Si definisca come luminositÃ  di un colore la media aritmetica del valore delle tre
  * componenti di una sua rappresentazione RGB. Si definisca come luminosita'  media di un insieme di
  * pixel la media aritmetica della luminosita'  dei colori dei pixel dell'insieme. Scrivere una funzione
  * (piu' eventuali funzioni ausiliarie) che, data una immagine A, verifica se tutte le righe di A hanno la
  * stessa luminosita'  media.
"""

def getPixelBrightness(pix):
  return (pix.getRed() + pix.getBlue() + pix.getGreen()) / 3.0

def getRowBrightness(img, y):
#@param img: Picture
#@param y: Int 
#@return : Float; average brightness for the row at index 'row' in img

  brightness = 0.0
  for x in range(0, getWidth(img)):
    pix = getPixel(img, x, y)
    brightness += getPixelBrightness(pix)   
  return brightness / getWidth(img)

def checkBrightness(img):
#@param img: Picture
#@return : Boolean

  brightness = getRowBrightness(img, 0)
  for row in range(1, getHeight(img)):
    if( getRowBrightness(img, row) != brightness):
      return false
  return true
    