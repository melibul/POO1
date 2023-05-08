import csv
class PlanAhorro:
	__cant_plan=0
	__cant_licitar=0
	def __init__(self, cod,mod,valor):
		self.__codigo=cod
		self.__modelo=mod
		self.__valor=valor
	def getModelo(self):
		return self.__modelo
	def getCodigo(self):
		return self.__codigo
	@classmethod
	def getCant_cuotas(cls):
		return cls.__cant_plan
	@classmethod
	def getCant_licitar(cls):
		return cls.__cant_licitar
	@classmethod
	def variables_clase(cls, plan, auto):
		cls.__cant_plan=plan
		cls.__cant_licitar=auto
	def valor_cuota(self):
		cuota=(self.__valor/self.getCant_cuotas())+self.__valor*0.10
		return cuota
	def actualizar(self, importe):
		self.__valor=importe
	def getValor(self):
		return self.__valor
	@classmethod
	def actualizar_cuota(cls, cant):
		cls.__cant_licitar=cant

class manejadorPlan():
	def __init__(self):
		self.__manejador=[]
	def leerArchivo(self):
		archivo=open('planes.csv')
		reader=csv.reader(archivo,delimiter=';')
		for fila in reader:
			unArchivo=PlanAhorro(int(fila[0]), fila[1], float(fila[2]))
			band=False
			self.__manejador.append(unArchivo)
			if(band==False):
				PlanAhorro.variables_clase(int(fila[3]),int(fila[4]))
				band=True
	def modifica_valor(self):
		i=0
		for i in range(len(self.__manejador)):
			print('Codigo: '+str(self.__manejador[i].getCodigo()))
			print('Modelo: '+str(self.__manejador[i].getModelo()))
			nuevo_valor=float(input('Ingrese nuevo valor del auto con codigo:' +str(self.__manejador[i].getCodigo()))+'\n')
			self.__manejador[i].actualizar(nuevo_valor)
	def mostrar_planes(self, valor):
		i=0
		while i<len(self.__manejador):
			if (self.__manejador[i].valor_cuota()<valor):
				print('Codigo: '+str(self.__manejador[i].getCodigo()))
				print('Modelo: '+str(self.__manejador[i].getModelo()))
			i=i+1
	def monto_licitar(self, valor):
		i=0
		band=False
		while i<len(self.__manejador) and  not band:
			if(self.__manejador[i].getValor()==valor):
				monto=self.__manejador[i].getCant_licitar()*self.__manejador[i].valor_cuota()
				print('El monto que se debe pagar para licitar el vehiculo es '+str(monto))
				band=True
			else:
				i=i+1
	def modificar_cuotas(self, cod):
		i=0
		band=False
		while i<len(self.__manejador) and  not band:
			if(self.__manejador[i].getCodigo()==cod):
				cant=int(input('Ingrese cantidad de cuotas:\n'))
				self.__manejador[i].actualizar_cuota(cant)
				band=True
			else:
				i=i+1		

