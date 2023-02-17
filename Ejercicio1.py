class Persona():
    def __init__(self):
        self.__nombre= ""
        self.__cedula= ""
        self.__genero= ""
#Setters 
    def asignarNombre(self,nombre):
        self.__nombre= nombre 
    def asignarCedula(self,cedula):
        self.__cedula= cedula 
    def asignarGenero(self,genero):
        self.__genero= genero

#getters
    def verNombre(self): 
        return self.__nombre
    def verCedula(self):
        return self.__cedula 
    def verGenero(self):
        return self.__genero 


class Paciente(Persona):
    def __init__(self):
        self.__servicio = ""
    def asignarServicio(self,servicio):
        self.__servicio = servicio 
    def verServicio(self,servicio):
        return self.__servicio 

p1= Paciente()
p2= Paciente()
p1.asignarNombre("Pepito")
p1.asignarCedula(123413)
p1.asignarGenero("mujer")
print (p1.verNombre())

class Paciente:
    def __init__(self):
        self.__nombre= ''
        self.__cedula= 0
        self.__genero= ''
        self.__servicio= ''

    def verNombre(self):
        return self.__nombre
    def verCedula(self):
        return self.__cedula
    def verGenero(self):
        return self.__genero
    def verGservicio(self):
        return self.__servicio

    def asignarNombre(self,n):
        self.__nombre = n 
    def asignarCedula(self,c):
        self.__cedula = c
    def asignarGenero(self,g):
        self.__genero = g
    def asignarServicio(self,s):
        self.__servicio = s 

class sistema:
    def __init__(self):
        self.__numero_pacientes = len(self.__lista_pacientes)
    def ingresarPacientes(self):
        nombre= input("Ingrese nombre:")
        cedula= int(input("Ingrese la cedula: "))
        genero= input("Ingrese el genero:")
        servicio= input("Ingrese el servicio: ")
        p= Paciente()
        p.asignarNombre(nombre)
        p.asignarCedula(cedula)
        p.asignarGenero(genero)
        p.asignarServicio(servicio)

        self.__lista_pacientes.append(p)
        self.__numero_pacientes = len(self.__lista_pacientes)
        def
class Empleado_Hospital(Persona):
    def __init__(self):
        self.__turno = ''
    def asignarTurno(self,turno):
        self.__turno= turno
    def verTurno(self,turno):
        return self.__turno

class Enfermera (Empleado_Hospital):
    def __init__(self):
        self.__rango= ''
    def asignarRango(self,rango):
        self.__rango = rango
    def verRango(self,rango):
        return self.__rango

class Medico(Empleado_Hospital):
    def __init__(self):
        self.__especialidad= ''
    def asignarEspecialidad(self,especialidad):
        self.__especialidad= especialidad
    def verEspecialidad(self,especialidad):
        return self.__especialidad



