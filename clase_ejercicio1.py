import csv
class Email():
	__idCuenta=''
	__dominio=''
	__tipoDominio=''
	__contraseña=None
	def __init__(self, cuenta,dom,tipo, contra):
		self.__idCuenta= cuenta
		self.__dominio=dom
		self.__tipoDominio=tipo
		self.__contraseña=contra
	def retornaEmail(self):
		return (self.__idCuenta+'@'+self.__dominio+'.'+self.__tipoDominio)
	def getDominio(self):
		return self.__dominio
	def mensaje(self, nombre, correo):
		print('Estimado '+nombre+' te enviaremos tus mensajes a la direccion '+correo)
	def comprobar(self, vieja):
		if(self.__contraseña==vieja):
			nueva=input('Ingrese contraseña nueva\n')
			self.__contraseña=nueva
			print('Contraseña cambiada correctamente')
		else:
			print('La contraseña ingresada es distinta a la actual')

	def crearCuenta(cls, mail):
		x=mail.split("@")
		y=x[1].split(".")
		Cuenta=x[0]
		dominio=y[0]
		tipoDominio=y[1]
		contra=None
		email = Email(Cuenta,dominio,tipoDominio,contra)
		return email 

class manejadorEmail():
	def __init__(self):
		self.__manejador=[]
	def leerArchivo(self):
		archivo=open('email.csv')
		reader=csv.reader(archivo,delimiter=',')
		for fila in reader:
			email = Email(fila[0],fila[1],fila[2], fila[3])
			self.__manejador.append(email)
		archivo.close()

	def mostrar(self):
		with open('email.csv', 'r') as file:
			reader = csv.reader(file)
			for row in reader:
				print(row)
	def contDom(self, domi):
		cont=0
		for email in self.__manejador:
			if email.getDominio() == domi:
				cont += 1
		return cont
		

