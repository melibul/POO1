class conjunto():
	def __init__(self):
		self.__conjunto=set()
	def agregarNum(self):
		num=int(input('Ingrese un numero, finalice con 0\n'))
		while num!= 0:
			self.__conjunto.add(num)
			num=int(input('Ingrese un numero, finalice con 0\n'))
	def getCon(self):
		return self.__conjunto
	def ordena(self):
		return sorted(self.__conjunto)
	def __add__(self, otroConjunto):
		return self.__conjunto.union(otroConjunto.getCon())
	def __sub__(self, otroConjunto):
		return self.__conjunto.difference(otroConjunto.getCon())
	def __eq__(self, otroConjunto):
		return self.__conjunto == otroConjunto.getCon()