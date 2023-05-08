import csv
class ViajeroFrecuente:
    __num_viajero = ''
    __dni = ''
    __nombre = ''
    __apellido = ''
    __millas_acum = None
    def __init__(self,num,dni,nom,apellido,millas):
        self.__num_viajero = num
        self.__dni = dni
        self.__nombre = nom
        self.__apellido = apellido
        self.__millas_acum = millas
    def getNumViajero(self):
        return(self.__num_viajero)
    def getTotalMillas(self):
        return(self.__millas_acum)
    def __gt__ (self,otroViajero):
        if(self.__millas_acum > otroViajero.getTotalMillas()):
            milla_mayor = self.__millas_acum
        else:
            milla_mayor = otroViajero.getTotalMillas()
        return (milla_mayor)
    def __add__(self,millas):
        return self.millas_acum + millas
    def __sub__(self,millas):
        return self.millas_acum - millas
    def __eq__(self, millas):
        return self.millas_acum==millas
    
class manejadorViajero:
    def __init__(self):
        self.__listaViajero= []
    def agregarViajero(self,unViajero):
        self.__listaViajero.append(unViajero)
    def testViajero(self):
        archivo = open('viajeros.csv')
        reader = csv.reader(archivo,delimiter=',')
        for fila in reader:
            num = fila[0]
            dni = fila[1]
            nom = fila[2]
            apellido = fila[3]
            millas = int(fila[4])
            unViajero = ViajeroFrecuente(num,dni,nom,apellido,millas)
            self.agregarViajero(unViajero)
        archivo.close()
    def buscaViajero(self,num):
        i=0
        Retorno = None
        b = False
        while not b and i < len(self.__listaViajero):
            if self.__listaViajero[i].getNumViajero()==num:
                b =True
                Retorno=i
            else:
                i+=1
        return Retorno
    def getMillas(self,n):
        return(self.__listaViajero[n].getTotalMillas())
    def acumularMillas(self,nuevas_millas,n):
        m = self.__listaViajero[n]+ nuevas_millas
        return m
    def canjearMillas(self,cant,n):
        m=self.__listaViajero[n]-cant
        return m
    def comparar_millas(self, cant, n):
        if(self.__listaViajero[n].getTotalMillas() == cant):
            print("Las millas ingresadas son iguales.")
        else:
            print("Las millas ingresadas no son iguales.")
    def comparaViajeros(self):
        maximo = max(self.__listaViajero)
        for i in range(len(self.__listaViajero)):
            if self.__listaViajero[i].getTotalMillas() == maximo.getTotalMillas():
                print("El viajero",self.__listaViajero[i].getNumViajero(),"tiene el maximo de millas.")