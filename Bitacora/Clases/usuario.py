# -*- coding: utf-8 *-*
'''
Created on 14/02/2014

@author: Admin
'''
# -----------
# Librerias
# -----------
import socket
# -----------
# Constantes
# -----------
# ------------------------------
# Clases y Funciones utilizadas
# ------------------------------
import ifconfig


class Usuario():
    
    def __init__(self):
        "Los atributos del Usuario"
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

    def Obtener_IP_Equipo (self):
        "Se Obtiene la IP del Equipo"
        self.ip_ifconfig()

    def ip_ifconfig(self):
        "Se Obtiene la IP del Equipo por medio de ifconfig"
        # Creamos la instancia a la Clase ifconfig
        ob_ifconfig = ifconfig.ifconfig()
        
        # Creamos el Archivo para obtener la IP del Equipo
        ob_ifconfig.crear_archivo()
        
        # Obtenemos la IP del Equipo
        ob_ifconfig.guardar_ip()
        self.IP_Equipo = ob_ifconfig.get_IP()
    
    def obtener_usuario(self):
        return self.nombre_usuario
    
    def reset_usuario(self):
        "Metodo que resetea los Atributos del Usuario"
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
        
    def Imprimir_valores(self):
        print self.graAca
        print self.usuario
        print self.nombre_usuario
        print self.nombre
        print self.apePat
        print self.apeMat
        print self.clvUsu
        print self.hora_inicio
        print self.hora_salida
        print self.IP_Equipo