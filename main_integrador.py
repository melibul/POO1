from clases_integrador import *
import os
def m_menu():
    print ("1: Informar promedio con y sin aplazos de un alumno")
    print ("2: Informar estudiantes promocionales aprobados por materia")
    print ("3: Obtener listado ordenado según año y alfabéticamente de alumnos")
    print ("4: Salir")
    
if __name__=='__main__':
    lista_alum=ManejadorAlumno(0)
    lista_mat=ManejadorMateria()
    lista_alum.carga_alumnos()
    lista_mat.carga_materias()
    while True:
        os.system('cls')
        m_menu()
        menu={
            "1": 'lista_mat.mostrarprom_alumno()',
            "2": 'lista_mat.mostrar_aprobados(lista_alum)',
            "3": 'lista_alum.ordenar_lista()',
            "4": 'print("Gracias por usar el sistema")'
        }
        opc=input("Ingrese la opción elegida: \n")
        os.system('cls')
        if opc in menu:
            if opc=='4':
                eval(menu[opc])
                break
            else:
                eval(menu[opc])
            aux=input("\nIngrese cualquier botón para continuar\n")
        else:
            print ("Ha ingresado una opción incorrecta, por favor, ingrese una opción nuevamente")