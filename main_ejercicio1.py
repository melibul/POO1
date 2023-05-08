from clase_ejercicio1 import *

def crearCuenta(mail):
		x=mail.split("@")
		y=x[1].split(".")
		Cuenta=x[0]
		dominio=y[0]
		tipoDominio=y[1]
		contra=input('Ingrese contraseña\n')
		email = Email(Cuenta,dominio,tipoDominio,contra)
		return email 
if __name__ == '__main__':
	opc=None
	while(opc!='0'):
		opc=input('''---MENU DE OPCIONES---
			1)_ Retornar email.
			2)_ Recibir mensaje.
			3)_ Modificar Contraseña.
			4)_ Leer de un archivo.
			5)_ Contar cantidad de dominios iguales.
			0)_ Terminar programa.
			''')
		if opc=='1':
			ids=input('Ingrese id de cuenta\n')
			dom=input('Ingrese dominio de mail\n')
			tipo=input('Ingrese tipo de dominio\n')
			con=input('Ingrese contraseña\n')
			mail1=Email(ids,dom,tipo,con)
			print (mail1.retornaEmail())
		elif opc=='2':
			nombre=input('Ingrese nombre\n')
			direccion=input('Ingrese direccion\n')
			mail2=crearCuenta(direccion)
			direccion=mail2.retornaEmail()
			mail2.mensaje(nombre,direccion)
		elif opc=='3':
			vieja=input('Ingrese contraseña antigua\n')
			mail2.comprobar(vieja)
		elif opc=='4':
			man=manejadorEmail()
			man.leerArchivo()
			man.mostrar()
		elif opc=='5':
			man=manejadorEmail()
			man.leerArchivo()
			domi=input('Ingrese dominio que quiere comparar\n')
			cont=man.contDom(domi)
			print('La cantidad de emails con el dominio '+domi+' es '+str(cont))
	print('Adios ;)')		


