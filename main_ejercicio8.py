from claseconjunto import *
if __name__ == '__main__':
	opc=None
	while(opc!=0):
            opc = int(input('''--Menu--
            1) Crear conjunto
            2) Sumar conjuntos
            3) Restar conjuntos
            4) Comparar conjuntos
            0) Terminar con el programa.
            '''))
            if opc == 1:
             lista1=conjunto()
             print('Conjunto 1: \n')
             lista1.agregarNum() 
             print(lista1.getCon())
             lista2=conjunto()
             print('Conjunto 2: \n')
             lista2.agregarNum()
             print(lista2.getCon())
            
            elif opc == 2:
             lista3=lista1+lista2
             print(lista3)
            elif opc == 3:
             lista4=lista1-lista2
             print(lista4)
            elif opc == 4:
                if(lista1==lista2):
                 print('Los conjuntos son iguales')
                else:
                 print('Los conjuntos son distintos')
print("Hasta luego :D!!")
