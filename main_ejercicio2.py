from clase_ejercicio2 import *
if __name__ == '__main__':
	lista=ManejadorViajero()
	lista.leerArchivo()
	numero=int(input('Ingrese numero de viajero\n'))
	r=lista.comprobar(numero)
	opc=None
	if r==None:
		print('El numero de viajero no existe')
	else: 
		while(opc!=0):
			opc=int(input('''---MENU DE OPCIONES---
				1)_ Consultar cantidad de millas.
				2)_ Acumular millas.
				3)_ Canjear millas.
				0)_ Finalice el programa.\n'''))
			if opc==1:
				print('La cantidad de millas que el viajero: ' +str(numero)+ ' tiene es '+str(lista.getMillas(r)))
			elif opc==2:
				millas=int(input('Ingrese cantidad de millas a acumular:\n'))
				print('La cantidad de millas que el viajero: ' +str(numero)+ ' acumulo es '+str(lista.getAcum(r, millas)))
			elif opc==3:
				millas=int(input('Ingrese cantidad de millas a canjear:\n'))
				print('La cantidad de millas que el viajero: ' +str(numero)+ ' le quedan es '+str(lista.getCanje(r, millas)))
	print('Hasta luego;)')
