class Alumno:
    def __init__(self,dni,ape,nom,carrera,anio):
        self.__dni=dni
        self.__ap=ape
        self.__nom=nom
        self.__carrera=carrera
        self.__aniocar=anio

    def get_dni(self):
        return self.__dni
    
    def get_nomap(self):
        return self.__ap+" "+self.__nom
    
    def get_anio(self):
        return self.__aniocar
    
    def __lt__(self,otro):
        return (self.__aniocar, (self.__ap + self.__nom)) < (otro.get_anio(), (otro.get_nomap()))
    
    def mostrar_datos(self):
        print ("{}, {} {}, {}, {}".format(self.__dni,self.__ap,self.__nom,self.__carrera,self.__aniocar))

class materiaA:
    def __init__(self,dni,nommat,fecha,nota,aprob):
        self.__dni=dni
        self.__nommate=nommat
        self.__fecha=fecha
        self.__nota=nota
        self.__cond=aprob

    def get_dni(self):
        return self.__dni
    
    def get_nota(self):
        return self.__nota
    
    def get_cond(self):
        return self.__cond
    
    def get_nomate(self):
        return self.__nommate
    
    def get_fecha(self):
        return self.__fecha
    
    def mostrar(self):
        print (self.__dni)
        print (self.__nommate)
        print (self.__fecha)
        print (self.__nota)
        print (self.__cond)

import numpy as np
import csv
class ManejadorAlumno:
    __cantidad=0
    __dimension=0
    __incremento=5
    def __init__(self,dimension,incremento=8):
        self.__listaalum=np.empty(dimension,dtype=Alumno)
        self.__cantidad=0
        self.__dimension=dimension
        self.__incremento=incremento
        
    def carga_alumnos(self):
        if self.__cantidad==self.__dimension:
            self.__dimension+=self.__incremento
            self.__listaalum.resize(self.__dimension)
        archivo=open("alumnos.csv")
        reader=csv.reader(archivo,delimiter=';')
        i=0
        for fila in reader:
            if i!=0:
                alumnoaux=Alumno(fila[0],fila[1],fila[2],fila[3],fila[4])
                self.__listaalum[self.__cantidad]=alumnoaux
                self.__cantidad+=1
            i+=1
    
    def buscar_alum(self,dni):
        i=0
        while i<self.__cantidad and dni!=self.__listaalum[i].get_dni():
            i+=1
        if i!=self.__cantidad:
            print ("{}       {}".format(self.__listaalum[i].get_dni(),self.__listaalum[i].get_nomap().ljust(17)),end="           ")
        return self.__listaalum[i].get_anio()
            
    def ordenar_lista(self):
        alumnos_ordenados=sorted(self.__listaalum)
        for alumno in alumnos_ordenados:
            alumno.mostrar_datos()


import csv
class ManejadorMateria:
    def __init__(self):
        self.__listamat=[]
        
    def carga_materias(self):
        archivo=open("materiasAprobadas.csv")
        reader=csv.reader(archivo,delimiter=';')
        i=0
        for fila in reader:
            if i!=0:
                alumnoaux=materiaA(fila[0],fila[1].upper(),fila[2],int(fila[3]),fila[4])
                self.__listamat.append(alumnoaux)
            i+=1
            
    def mostrarprom_alumno(self):
        dni=input("Ingrese el dni del alumno ")
        lista_indices=[]
        i=0
        for fila in self.__listamat:
            if fila.get_dni()==dni:
                lista_indices.append(i)
            i+=1 
        if len(lista_indices)==0:
            print ("No se encontró el Alumno buscado")
        else:
            prom=[0,0]
            for cant in range (len(lista_indices)):
                prom[0]+=self.__listamat[lista_indices[cant]].get_nota()                
                if self.__listamat[lista_indices[cant]].get_cond()=='E':
                    if self.__listamat[lista_indices[cant]].get_nota()>=4:
                        prom[1]+=self.__listamat[lista_indices[cant]].get_nota()
                if self.__listamat[lista_indices[cant]].get_cond()=='P':
                    if self.__listamat[lista_indices[cant]].get_nota()>=7:
                        prom[1]+=self.__listamat[lista_indices[cant]].get_nota()
                if self.__listamat[lista_indices[cant]].get_cond()=='X':
                    if self.__listamat[lista_indices[cant]].get_nota()>=6:
                        prom[1]+=self.__listamat[lista_indices[cant]].get_nota()
            print ("El promedio del alumno con aplazos es "+str(prom[0]/len(lista_indices)))
            print ("El promedio del alumno sin aplazos es "+str(prom[1]/len(lista_indices)))
            
    def mostrar_aprobados(self,alumnos):
        materia=input("Ingrese la materia a buscar: ")
        print ("DNI            Apellido y Nombre           Fecha           Nota        Año que cursa")
        for fila in self.__listamat:
            if materia.upper()==fila.get_nomate():
                if fila.get_cond()=='P':
                    if fila.get_nota()>=7:
                        p=alumnos.buscar_alum(fila.get_dni())
                        print("{}      {}           {}".format(fila.get_fecha(),str(fila.get_nota()),p))