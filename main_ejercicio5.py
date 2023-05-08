from clase_ejercicio5 import *
if __name__ == '__main__':
	lista=manejadorPlan()
	lista.leerArchivo()
	opc=None
	while opc != 0:
	    opc=int(input('''=== MENÚ DE OPCIONES ===
	    1)_Actualizar valor de vehiculo de cada plan.
	    2)_Mostrar codigo y modelo del vehiculo.
	    3)_Mostrar monto que se debe pagar para licitar.
	    4)_Modificar cantidad de cuotas para licitar.
	    0)_ Finalizar y cerrar.\n'''))

	    if opc==1:
	    	lista.modifica_valor()
	    elif opc==2:
	    	valor=float(input('Ingrese valor\n'))
	    	lista.mostrar_planes(valor)
	    elif opc==3:
	    	valor=float(input('Ingrese valor\n'))
	    	lista.monto_licitar(valor)
	    elif opc==4:
	    	cod=int(input('Ingrese codigo del vehiculo\n'))
	    	lista.modificar_cuotas(cod)
	print('Adios <3')
