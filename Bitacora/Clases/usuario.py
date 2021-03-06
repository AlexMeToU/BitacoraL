# -*- coding: utf-8 *-*
'''
Created on 14/02/2014

@author: Admin
'''
# -----------
# Librerias
# -----------
import os
# -----------
# Constantes
# -----------
# ------------------------------
# Clases y Funciones utilizadas
# ------------------------------

class Usuario():
    
    def __init__(self,sistemaop):
        "Los atributos del Usuario"
        self.tipo_usuario=''
        self.graAca = ''
        self.usuario = ''
        self.pwd = ''
        self.nombre_usuario = ''
        self.nombre = ''
        self.apePat= ''
        self.apeMat= ''
        self.clvUsu= ''
        self.hora_inicio = ''
        self.hora_salida = ''
        self.IP_Equipo='0.0.0.0'
        self.tipo_usuario=''
        
        # Elementos para Registrar la Asistencia
        self.gpo = ''
        self.materia = ''
        self.hora_materia = ''
        self.clvHor= ''
        
        self.sistemaop = sistemaop
        
        # Archivo
        if self.sistemaop == "linux2":
            self.file = "/tmp/user_unix.txt"
        else:
            self.file = "Clases/user_unix.txt"
        
        # Apuntador a Archivo
        self.f = None
        
    def get_user_unix(self):
        "Obtenemos el Usuario de Unix"
        if self.sistemaop == "linux2":
            os.system("clear")
            os.system("whoami > /tmp/user_unix.txt")
        
        self.abrir_archivo("r")
        linea = self.f.readline()
        access = False
        if linea == "root\n":
            access = True
        else:
            access = False
        return access
        
    def abrir_archivo(self,modo):
        "Metodo para Abrir Archivo"
        try:
            self.f = open(self.file,modo)
        except Exception:
            print "No se Abrio Archivo"
            self.f = None

    def set_IP(self,ip):
        "Se Guarda la IP del Equipo"
        self.IP_Equipo = ip
        
    def set_hora_inicio(self,hora):
        self.hora_inicio = hora
        
    def set_hora_final(self,hora):
        self.hora_salida = hora
        
    def get_nombre_usuario(self):
        return self.nombre_usuario
    
    def get_tipo_usuario(self):
        return self.tipo_usuario

    def set_gpo(self,gpo):
        self.gpo = gpo
    
    def get_gpo(self):
        return self.gpo
    
    def get_clvUsu(self):
        return self.clvUsu
    
    def get_clvHor(self):
        return self.clvHor
    
    def get_IP(self):
        return self.IP_Equipo
    
    def guardar_datos(self,tipo_usuario,nombre,apePat,apeMat,graAca,clvUsu,nombre_usuario):
        "Metodo para Guardar los Datos del Usuario Logeado"
        self.tipo_usuario = tipo_usuario
        self.nombre = nombre
        self.apePat = apePat
        self.apeMat = apeMat
        self.graAca = graAca
        self.clvUsu = clvUsu
        self.nombre_usuario = nombre_usuario
        
    def guardar_datos_clase(self,gpo,materia,hora_materia,clvHor):
        "Metodo para Guardar los Datos de la Clase"
        self.gpo = gpo
        self.materia = materia
        self.hora_materia = hora_materia
        self.clvHor= clvHor
        
    def reset_usuario(self):
        "Metodo que resetea los Atributos del Usuario"
        self.tipo_usuario=''        
        self.graAca = ''
        self.usuario = ''
        self.pwd = ''
        self.nombre_usuario = ''
        self.nombre = ''
        self.apePat= ''
        self.apeMat= ''
        self.clvUsu= ''
        self.hora_inicio = ''
        self.hora_salida = ''
        self.IP_Equipo='0.0.0.0'
        self.gpo = ''
        self.materia = ''
        self.hora_materia = ''
        self.clvHor= ''
