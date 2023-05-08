import csv
class ViajeroFrecuente:
	def __init__(self, num_viajero,dni,nomb,ape,millas):
		self.__num_viajero=num_viajero
		self.__dni=dni
		self.__nombre=nomb
		self.__apellido=ape
		self.__millas_acum=millas
	def cantidadTotaldeMillas(self):
		return self.__millas_acum
	def acumularMillas(self, milla):
		self.__millas_acum=self.__millas_acum+milla
		return self.__millas_acum
	def canjearMillas(self, milla):
		if(self.__millas_acum>=milla):
			self.__millas_acum=self.__millas_acum-milla
			return self.__millas_acum
		else:
			print('Error en la operacion')
	def getNum(self):
		return self.__num_viajero

class ManejadorViajero():
	def __init__(self):
		self.__manejador=[]
	def leerArchivo(self):
		archivo=open('viajeros.csv')
		reader=csv.reader(archivo,delimiter=',')
		for fila in reader:
			viajero=ViajeroFrecuente(int(fila[0]),fila[1],fila[2],fila[3],int(fila[4]))
			self.__manejador.append(viajero)
		archivo.close()
	def getMillas(self, r):
		return self.__manejador[r].cantidadTotaldeMillas()
	def getAcum(self, r, milla):
		return self.__manejador[r].acumularMillas(milla)
	def getCanje(self, r, milla):
		return self.__manejador[r].canjearMillas(milla)
	def comprobar(self, numero):
		i=0
		band=False
		r=None
		while not band and i<len(self.__manejador):
			if(self.__manejador[i].getNum()==numero):
				band=True
				r=i
			else:
				i=i+1
		return r

