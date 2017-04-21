
class Pezzo:
	def __init__(self, strlist, costo, passi, bottoni, first):
		self.costo = int(costo)
		self.passi = int(passi)
		self.bottoni = int(bottoni)
		
		self.first = True if first else False
		
		base = []
		
		for el in strlist:
			l = []
			for c in el:
				l.append(c)
			base.append(l)
				
		self.permutazioni=[]
		
		self.permutazioni.append(base)
		
		r1 = self.ruota(base)
				
		for el in r1:
			if not self.contains(el):
				self.permutazioni.append(el)
		
		
		if not self.contains(self.rifletti(base)):
			self.permutazioni.append(self.rifletti(base))
		
		r2 = self.ruota(self.rifletti(base))
		for el in r2:
			if not self.contains(el):
				self.permutazioni.append(el)
			
		#~ for el in self.permutazioni:
			#~ for l in el:
				#~ print l
			#~ print
		
		self.l1 = self.count_hor(self.permutazioni[0])
		self.l2 = self.count_ver(self.permutazioni[0])
		
		
		#~ for el in strlist:
			#~ print el
		#~ print self.l1, self.l2
		#~ raw_input()
	
	def count_hor(self, mat):
		
		r = []
		
		for line in mat:
			maxlen = 0
			l = 0
			for x in line:
				if x == 'x':
					l +=1
				else:
					l=0
					
				if l > maxlen:
					maxlen=l
				
			r.append(maxlen)
		
		return r
		
	def count_ver(self, mat):
		
		r =  []
		
		for i in range(len(mat[0])):
			maxlen = 0
			l = 0
		
			line = [el[i] for el in mat]
			
			for x in line:
				if x == 'x':
					l +=1
				else:
					l=0
					
				if l > maxlen:
					maxlen=l
				
			r.append(maxlen)		
		
		return r
		
	def contains(self, piece):
		
		cond = False
		for el in self.permutazioni:
			if len(el) == len(piece) and len(el[0])==len(piece[0]):
				
				v = True
				
				for i in range(len(el)):
					for j in range(len(el[i])):
						if not el[i][j]==piece[i][j]:
							v = False
				
				if v:
					cond = True
		
		return cond
			
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
				pezzi.append(Pezzo(m, p[0], p[1], p[2], 1 if len(p)>2 else 0))
				raw_input()

		else:
			
			if not line[0] in [".", "x"]: 
				p = line.split()
				m = []
			else:
				m.append(line[:-1])


