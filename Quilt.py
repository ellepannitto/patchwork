#!/usr/bin/python

def valid_alignment ( needle, haystack, posstart ):
	
	print "check if is a valid alignment"
	print "needle", needle 
	print "haystack", haystack
	print "pos start", posstart 
	
	still_valid = False
	
	if posstart >=0 and posstart+len(needle) <= len(haystack):
		j=0
		still_valid = True
		while j<len(needle) and still_valid:
			print "j=",j
			still_valid = False
			if any ( x>=needle[j] for x in haystack[posstart+j] ):
				still_valid = True
			j += 1
	
	print still_valid, "\n\n"
	#~ raw_input ()

	return still_valid
	
	
def count_hor( mat ):
		
	r = []
	
	for line in mat:
		curlis = []
		l = 0
		for x in line:
			if x == '.':
				l +=1
			else:
				if l>0:
					curlis.append(l)
				l=0
		
		if l>0:
			curlis.append(l)		
		
		r.append(curlis)
	
	return r
		
def count_ver(mat):
		
	r =  []
	
	for i in range(len(mat[0])):
		curlis = []
		l = 0
	
		line = [el[i] for el in mat]
		
		for x in line:
			if x == '.':
				l +=1
			else:
				if l>0:
					curlis.append(l)
				l=0
		
		if l>0:
			curlis.append(l)		
		
		r.append(curlis)
		
	
	return r

def parse_quilt ( quilt_str_array ):
	ret = Quilt ( len(quilt_str_array) )
	
	mat = [[ c for c in line.strip() ] for line in quilt_str_array ]
	
	ret.hholes = count_hor ( mat )
	ret.vholes = count_ver ( mat )
	ret.matrix = mat
	
	return ret	
		

class Quilt:
	
	def __init__ ( self, dim ):
		self.dim = dim
		self.hholes = [ [ dim ] * dim ]
		self.vholes = [ [ dim ] * dim ]
		self.martrix = [ [ '.' ]* dim ] * dim 
		
	
	def all_the_possible_alignments ( self, needle, haystack ):
		result_set = []
		m = max (needle)
		posmax = needle.index ( m )
		for i in range ( len(haystack) ):
			if any ( [ x >= m for x in haystack[i] ] ) and valid_alignment ( needle, haystack, i-posmax ) :
				result_set.append ( i-posmax )
		
		return result_set
		
	
	def candidate_positions ( self, l_hor, l_ver, top=-1 ):
		'''
			finds the top candidate positions for a piece, given the maximum amount of contiguous squares in each row (l1) and in each col (l2). 
			returns a list of all the positions in which that piece may be put. If a position is not returned, the piece cannot fit in that position for sure.
		'''
	
		#TODO: implement score
		
		valid_horizontal_alignment = self.all_the_possible_alignments ( l_hor, self.hholes )
		valid_vertical_alignment = self.all_the_possible_alignments ( l_ver, self.vholes )
		
		return [ (x,y) for y in valid_vertical_alignment for x in valid_horizontal_alignment ] 

	def try_insert(self, pos, piece_mat):
		
		
		cond = True
		
		for i in range(pos[0], pos[0]+len(piece_mat)):
			for j in range(pos[1], pos[1]+len(piece_mat[0])):
				
				if self.matrix[i][j]=='x' and piece_mat[i-pos[0]][j-pos[1]] == 'x':
					cond =  False
				
		return cond
		

if __name__ == "__main__":
	import Pezzo
	
	q = parse_quilt ( open ("quilt_test").readlines() )
	
	p = Pezzo.Pezzo(["x.", 
					 "xx", 
					 "xx", 
					 ".x"], 4, 2, 0, 0)
	
	print "QUILT:"
	print q.matrix
	
	for perm in p.permutazioni:
		positions = q.candidate_positions ( perm.l_hor, perm.l_ver)
		
		print perm.matrice
		print 
		
		for pos in positions:
			print "Provo:", pos
			print q.try_insert(pos, perm.matrice)

		raw_input()
	
	
