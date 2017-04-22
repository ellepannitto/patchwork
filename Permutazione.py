class Permutazione:
	
	def __init__(self, mat):
		self.matrice = mat

		self.l_hor = self.count_hor()
		self.l_ver = self.count_ver()
	
	def count_hor(self):
		mat = self.matrice		
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
		
	def count_ver(self):
		
		mat = self.matrice
		
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
	
	def equals (self, piece):
		
		cond = False
		
		if len(self.matrice) == len(piece) and len(self.matrice[0])==len(piece[0]):			
			v = True
			
			for i in range(len(self.matrice)):
				for j in range(len(self.matrice[i])):
					if not self.matrice[i][j]==piece[i][j]:
						v = False
			
			if v:
				cond = True
				
		return cond
