class Registro:
    __temperatura= 0.0
    __humedad= 0.0
    __presion= 0.0

    def __init__(self,temp,hum,pres):
        self.__humedad=hum
        self.__presion=pres
        self.__temperatura=temp

    def get_humedad (self):
        return self.__humedad
    
    def get_temperatura (self):
        return self.__temperatura
    
    def get_presion (self):
        return self.__presion
    
    def mostrar_datos(self):
        print (self.__temperatura)
        print (self.__humedad)
        print (self.__presion)
import os
import datetime
import csv
D=30
H=24
class ManejadorRegistro:
    __listaregistro=[]
    
    def __init__(self):
        self.__listaregistro=[[None for columna in range(H)]for fila in range(D)]
    
    def cargaarchivo (self):
        archivo='Meteorologia.csv'
        for fila in range(D):
            for columna in range(H):
                print ("Ingrese datos del día "+str(fila+1))
                print ("Ingrese datos de la hora "+ str(datetime.time(columna)))
                temp=float(input("Ingrese la temperatura actual "))
                humed=float(input("Ingrese la humedad actual "))
                pres=float(input("Ingrese la presión actual "))
                registroaux=Registro(temp,humed,pres)
                self.__listaregistro[fila][columna]=registroaux
                os.system('cls')
            i=0
            os.system('cls')
        with open (archivo, 'w', newline='') as archivo_csv:
                escritor_csv = csv.writer(archivo_csv, delimiter=';')
                for fila in self.__listaregistro:
                    j=0
                    for columna in fila:
                        escritor_csv.writerow([i+1,datetime.time(j),columna.get_temperatura(),columna.get_humedad(),columna.get_presion()])
                        j+=1
                    i+=1

    def mayormenor (self):
        mayortemp=0.0
        diahoramaytemp=[0,'']
        menortemp=999.9
        diahoramentemp=[0,'']
        mayorhum=0.0
        diahoramayhum=[0,'']
        menorhum=999.9
        diahoramenhum=[0,'']
        mayorpres=0.0
        diahoramaypres=[0,'']
        menorpres=999.9
        diahoramenpres=[0,'']
        d=0
        for fila in self.__listaregistro:
            i=0
            for columna in fila:
                if columna.get_temperatura()>mayortemp:
                    mayortemp=columna.get_temperatura()
                    diahoramaytemp=[d+1,datetime.time(i)]
                if columna.get_temperatura()<menortemp:
                    menortemp=columna.get_temperatura()
                    diahoramentemp=[d+1,datetime.time(i)]
                if columna.get_humedad()>mayorhum:
                    mayorhum=columna.get_humedad()
                    diahoramayhum=[d+1,datetime.time(i)]
                if columna.get_humedad()<menorhum:
                    menorhum=columna.get_humedad()
                    diahoramenhum=[d+1,datetime.time(i)]
                if columna.get_presion()>mayorpres:
                    mayorpres=columna.get_presion()
                    diahoramaypres=[d+1,datetime.time(i)]
                if columna.get_presion()<menorpres:
                    menorpres=columna.get_presion()
                    diahoramenpres=[d+1,datetime.time(i)]
                i+=1
            d+=1
        print ('Mayor temperatura: \nDia: '+str(diahoramaytemp[0]),"Hora:",diahoramaytemp[1])
        print ('Menor temperatura: \nDia: '+str(diahoramentemp[0]),"Hora:",diahoramentemp[1])

        print ('Mayor humedad: \nDia: '+str(diahoramayhum[0]),"Hora:",diahoramayhum[1])
        print ('Menor humedad: \nDia: '+str(diahoramenhum[0]),"Hora:",diahoramenhum[1])

        print ('Mayor presión: \nDia: '+str(diahoramaypres[0]),"Hora:",diahoramaypres[1])
        print ('Menor presión: \nDia: '+str(diahoramenpres[0]),"Hora:",diahoramenpres[1])
        aux=input()

    def temppromedio(self):
        promtemp=[0.0]*24
        d=0
        for fila in self.__listaregistro:
            i=0
            for columna in fila:
                promtemp[i]+=columna.get_temperatura()
                i+=1
            d+=1
        j=0
        for hora in promtemp:
            print ('El promedio de la hora',datetime.time(j),'del mes es: \n'+str((hora/d)))
            j+=1
        aux=input()

    def listarvalores (self):
        dia=int(input("Ingrese el día: "))
        resultado=self.__listaregistro[dia-1]
        for indice, instancia in enumerate(resultado):
            print ("Hora       Temperatura     Humedad     Presion")
            print(datetime.time(indice),"       ",instancia.get_temperatura(),"       ",instancia.get_humedad(),"      ",instancia.get_presion())
        aux=input()