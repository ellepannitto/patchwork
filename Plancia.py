import Pezzo
import random


class Plancia:
	
	def __init__(self):
		
		self.codaPezzi = self.caricaPezzi()
		
		print [str(el) for el in self.codaPezzi]
		
		random.shuffle(self.codaPezzi)
		
		print [str(el) for el in self.codaPezzi]
		
		i = self.startingPosition()
		
		print i
		
		self.changeQueue(i)
		
		print [str(el) for el in self.codaPezzi]
		
		
	def caricaPezzi(self):
		fobj = open("pezzi")
	
		pezzi = []
		
		p = None
		
		for line in fobj:
			if line == "\n":
				if p:
					pezzi.append(Pezzo.Pezzo(m, p[0], p[1], p[2], 1 if len(p)>3 else 0))
					#~ raw_input()

			else:
				
				if not line[0] in [".", "x"]: 
					p = line.split()
					m = []
				else:
					m.append(line[:-1])

		return pezzi


	def startingPosition(self):
		
		trovato = False
		i=-1
		while not trovato:
			i+=1
			if self.codaPezzi[i].first:
				trovato = True
				
		return i
		
	def changeQueue(self, i, j=0):
		
		self.codaPezzi = self.codaPezzi[i:]+self.codaPezzi[:i-j]
		


if __name__=="__main__":
	p = Plancia()
