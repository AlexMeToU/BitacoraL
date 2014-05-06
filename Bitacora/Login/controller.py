# -*- coding: utf-8 *-*
#!/usr/bin/env python
'''
Created on 28/01/2014

@author: Admin
'''
# -----------
# Librerias
# -----------
import os
import sys
import subprocess
import threading
import time
import logging
from datetime import datetime
import hashlib
# -----------
# Constantes
# -----------
apagarL = "sudo shutdown -h now"
apagarW = "shutdown /s /f /t 01"
# ------------------------------
# Clases y Funciones utilizadas
# ------------------------------
import model
import Clases.usuario
import Clases.filtro
# ------------------------------
# Funcion principal del juego
# ------------------------------


class controlador:
    
    def __init__(self,sistemaop):
        # Creamos un objeto usuario para la informacion del usuario a logear
        self.usuario = Clases.usuario.Usuario()
        
        # Creamos un objeto modelo para comunicarnos con el MODELO de la Aplicacion
        self.modelo = model.modelo()
        
        # Diccionario con los Tipos de Usuario del Sistema
        self.tipo_usuarios = {"profesor":"prof","asistente":"asist","alumno":"alum"}
        
        # Instancia a la Clase filtro
        self.filtro = Clases.filtro.filtro()
        
        # SO para pruebas en Windows
        self.sistemaop = sistemaop
        
    """---------------------------------------Metodos-------------------------------------------------------"""
    def Obtener_Hora_Servidor(self):
        "Se Verifica la Hora del Servidor"
        consulta,edo_consulta = self.modelo.hora_sistema()
        if edo_consulta == "SUCCESS":
            self.usuario.hora_inicio = consulta[0][0]
        cad = str (self.usuario.hora_inicio)
        logging.info('Hora del Sistema:')
        logging.info(cad)            
        return edo_consulta

    def registrar_inicio (self):
        "Se Registra el Inicio de Sesion"
        return self.modelo.registrar_inicio(self.usuario.clvUsu,self.usuario.hora_inicio,self.usuario.IP_Equipo)
        
    def obtener_usuario_logeado(self):
        return self.usuario

    """--------------------------------------Eventos-------------------------------------------------------"""

    def Iniciar_Sesion(self,usuario,pwd):
        "Click en Boton Iniciar Sesion"
        # Se obtienen los datos ingresados en el formulario de Logeo
        self.usuario.usuario = self.filtro.filtrar_cadena(usuario) 
        self.usuario.pwd = self.filtro.filtrar_cadena(pwd)
        consulta = ""
        m = hashlib.md5()
        m.update(self.usuario.pwd)        
        # Se compara el usuario y pwd ingresado con los del Super Usuario
        #if self.usuario.usuario == "super_usuario" and self.usuario.pwd =="COZDSOWLBOXY":
        if self.usuario.usuario == "super_usuario" and m.hexdigest() =="f1eabafa36de3c1abcd217b1baae2875":        
            # Si es el Super Usuario asignamos self.super_usuario= 1 y salimos de la Aplicacion
            #logging.info('Se logeo Super')
            #logging.info ("Hora de Inicio = ["+str(datetime.now().strftime('%Y-%m-%d %H:%M:%S'))+"]")            
            consulta = None
            return "super"
        else:
            # Buscamos en Cada Tipo de Usuario los Datos Ingresados
            for key in self.tipo_usuarios.keys():
                if self.tipo_usuarios[key] == "alum":
                    # Primero se verifica que sea un Alumno
                    consulta,edo_consulta = self.modelo.validar_usuario_alumno(self.usuario.usuario,self.usuario.pwd)
                    # Si la Consulta Falla enviamos el Mensaje a la Vista
                    if edo_consulta == "FAILED_VALIDATE":
                        return edo_consulta
                    else:
                        if len(consulta) > 0:
                            for registro in consulta:
                                # Guardamos la informacion recibida desde la BD
                                self.usuario.tipo_usuario = self.tipo_usuarios[key]
                                self.usuario.nombre = registro [1] #Nombre
                                self.usuario.apePat = registro [2] #ApePat
                                self.usuario.apeMat = registro [3] #ApeMat
                                self.usuario.clvUsu = registro [0] #Matricula
                                self.usuario.nombre_usuario = registro[1]+' '+registro[2]+' '+registro[3]
                            break
                            
                elif self.tipo_usuarios[key] == "asist":
                    # Se verifica que sea un Asistente
                    consulta,edo_consulta = self.modelo.validar_usuario_tecaux(self.usuario.usuario,self.usuario.pwd)
                    # Si la Consulta Falla enviamos el Mensaje a la Vista
                    if edo_consulta == "FAILED_VALIDATE":
                        return edo_consulta
                    else:
                        if len(consulta) > 0:
                            for registro in consulta:
                                # Guardamos la informacion recibida desde la BD
                                self.usuario.tipo_usuario = self.tipo_usuarios[key]
                                self.usuario.nombre = registro [1] #Nombre
                                self.usuario.apePat = registro [2] #ApePat
                                self.usuario.apeMat = registro [3] #ApeMat
                                self.usuario.graAca = registro [4] #Grado
                                self.usuario.clvUsu = registro [5] #log
                                self.usuario.nombre_usuario = registro[4]+' '+registro[1]+' '+registro[2]+' '+registro[3]
                            break
                elif self.tipo_usuarios[key] == "prof":
                    # Se verifica que sea un Profesor 
                    consulta,edo_consulta = self.modelo.validar_usuario_profesor(self.usuario.usuario,self.usuario.pwd)
                    # Si la Consulta Falla enviamos el Mensaje a la Vista                    
                    if edo_consulta == "FAILED_VALIDATE":
                        return edo_consulta
                    else:
                        if len(consulta) > 0:
                            for registro in consulta:
                                # Guardamos la informacion recibida desde la BD
                                self.usuario.tipo_usuario = self.tipo_usuarios[key]
                                self.usuario.nombre = registro [1] #Nombre
                                self.usuario.apePat = registro [2] #ApePat
                                self.usuario.apeMat = registro [3] #ApeMat
                                self.usuario.graAca = registro [4] #Grado
                                self.usuario.clvUsu = registro [5] #log
                                self.usuario.nombre_usuario = registro[4]+' '+registro[1]+' '+registro[2]+' '+registro[3]
                            break

            if len(consulta) > 0:
                self.usuario.Obtener_IP_Equipo(self.sistemaop)
                if self.usuario.IP_Equipo == "0.0.0.0":
                    #print "Fallo al Leer IP"
                    return "FAILED_GET_IP"

                edo_hora_servidor = self.Obtener_Hora_Servidor()
                if edo_hora_servidor == "FAILED_GET_HOUR":
                    #print "Fallo al Leer Hora del Servidor"
                    return edo_hora_servidor
                edo_registro = self.modelo.registrar_inicio(self.usuario.clvUsu,self.usuario.hora_inicio,self.usuario.IP_Equipo)
                return edo_registro
            else:
                #print "Usuario No Valido"
                return "USER_NO_VALIDO"

    def ApagarEquipo(self):
        "Click en Boton Apagar Equipo"
        os.system(apagarL)