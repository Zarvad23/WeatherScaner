import googletrans
from googletrans import Translator

def translate (place):
	trans = Translator()
	result = trans.translate(place)
	return place

	
