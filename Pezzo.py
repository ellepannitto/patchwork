import Permutazione


class Pezzo:
	def __init__(self, strlist, costo, passi, bottoni, first):
		self.costo = int(costo)
		self.passi = int(passi)
		self.bottoni = int(bottoni)
		
		self.first = True if first else False
		
		self.permutazioni = []
	
		base = []
		
		for el in strlist:
			l = []
			for c in el:
				l.append(c)
			base.append(l)
				
		
		self.permutazioni.append(Permutazione.Permutazione(base))
		
		r1 = self.ruota(base)
				
		for el in r1:
			if not self.contains(el):
				self.permutazioni.append(Permutazione.Permutazione(el))
		
		
		if not self.contains(self.rifletti(base)):
			self.permutazioni.append(Permutazione.Permutazione(self.rifletti(base)))
		
		r2 = self.ruota(self.rifletti(base))
		for el in r2:
			if not self.contains(el):
				self.permutazioni.append(Permutazione.Permutazione(el))
			
		for el in self.permutazioni:
			print vars(el)
			print
		

		
		
		#~ for el in strlist:
			#~ print el
		#~ print self.l1, self.l2
		#~ raw_input()
	

		
	def contains(self, piece):
		
		return any(el.equals(piece) for el in self.permutazioni)
					
	def ruota(self, matrix):
		
		ret = []
		
		n = 3
			
		while n > 0:
			
			newm = []
		
			#~ for el in matrix:
				#~ print el
				
			#~ raw_input()
			
			for i in range(len(matrix[0])):
				l = [el[i] for el in matrix]
				newm.append(list(reversed(l)))
				
			#~ for el in newm:
				#~ print el
			#~ raw_input()
			
			ret.append(newm)
			matrix = newm
			
			n-=1
		
		return ret
		
	def rifletti(self, matrix):
		
		ret = []
		
		for el in matrix:
			ret.append(list(reversed(el)))
			
		return ret	
		
	def __str__(self):
		return str(self.permutazioni[0]) + str(self.first)
			

if __name__=="__main__":
	fobj = open("pezzi")
	
	pezzi = []
	
	p = None
	
	for line in fobj:
		if line == "\n":
			if p:
				print "nuovo pezzo"
				pezzi.append(Pezzo(m, p[0], p[1], p[2], 1 if len(p)>2 else 0))
				#~ raw_input()
				

		else:
			
			if not line[0] in [".", "x"]: 
				p = line.split()
				m = []
			else:
				m.append(line[:-1])


