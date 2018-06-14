"""
 * Problema 6
 * Scrivere una funzione (piu' eventuali funzioni ausiliarie) che, data un'immagine A,
 * verifica se A contiene almeno una riga i cui pixel hanno tutti lo stesso colore.
"""

def picWithSameColorRow(pict):
# @param pict: Picture
# @return : Boolean
	for y in range(getHeight(pict)):
		if sameColorRow(pict,y):
			return true
	return false


def sameColorRow(pict,y):
# @param pict: Picture
# @param y: Int; y coordinate
# @return : Boolean
	firstPixel = getPixel(pict,0,y)
	for x in range(getWidth(pict)):
		currPixel = getPixel(pict,x,y)
		if not samePixel(firstPixel,currPixel):
			return false
	return true		


def samePixel(p1,p2):
# @param p1: Pixel
# @param p2: Pixel
# @return : Boolean
	return (getRed(p1) == getRed(p2) and
			getGreen(p1) == getGreen(p2) and
			getBlue(p1) == getBlue(p2))