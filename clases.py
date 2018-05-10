import pygame,sys,os
import funciones as F

class Serie():
    def __init__(self,archivo):
        self.Atletas = []
        self.archivo = archivo
        self.fuente = pygame.font.Font("arial.ttf", 30)
        self.cargar_Datos(self.archivo)

    def actualizar(self):
        self.Atletas = []
        self.cargar_Datos(self.archivo)    
        
    def cargar_Datos(self,archivos):
        py = 245
        texto = open(archivos,'r')
        for datos in texto.readlines():
            try:
                if 'Serie' in datos:
                    list_datos = datos.strip().split(',')
                    self.titulo = list_datos[3]
                    self.s_titulo = pygame.font.Font.render(self.fuente, self.titulo, 1,(255,255,255))
                    self.s_Trect = self.s_titulo.get_rect()
                    self.s_Trect.left = 200
                    self.s_Trect.top = 30
                else:
                    list_datos = datos.strip().split(',')
                    self.Atletas.append(Atleta(list_datos[0],list_datos[1],list_datos[2],list_datos[3],list_datos[4],list_datos[5],list_datos[6],py))
                    py+=65
            except:
                print 'Se intento cargar lo siguiente: {0}'.format(datos)
            
    
class Atleta():
    def __init__(self,puesto,ide,pista,apellido,nombre,club,marca,py):
        self.puesto = puesto
        self.ide = ide
        self.pista = pista
        self.nombre = nombre + apellido
        self.marca = marca
        self.club = club
        self.fuente = pygame.font.Font("arial.ttf", 30)
        self.s_puesto = pygame.font.Font.render(self.fuente, self.puesto, 1,(0,0,0))
        self.s_pista = pygame.font.Font.render(self.fuente, self.pista, 1,(0,0,0))
        self.s_nombre = pygame.font.Font.render(self.fuente, self.nombre, 1,(0,0,0))
        self.s_marca = pygame.font.Font.render(self.fuente, self.marca, 1,(0,0,0))
        self.s_club = pygame.font.Font.render(self.fuente, self.club, 1,(0,0,0))
        self.s_Lrect = self.s_puesto.get_rect()
        self.s_Prect = self.s_pista.get_rect()
        self.s_Nrect = self.s_nombre.get_rect()
        self.s_Mrect = self.s_marca.get_rect()
        self.s_Crect = self.s_club.get_rect()
        self.s_Nrect.left = 400 #inicio eje x 
        self.s_Nrect.top = py  #inicio eje y
        self.s_Lrect.left = 40
        self.s_Lrect.top = py
        self.s_Prect.left = 255
        self.s_Prect.top = py
        self.s_Mrect.left = 110
        self.s_Mrect.top = py
        self.s_Crect.left = 1000
        self.s_Crect.top = py


"""
recep = True
x = Serie(F.listar_Archivos()[0])
for a in x.Atletas:
    print a.puesto,a.ide,a.pista,a.nombre,a.marca,a.club
    
while recep:
    dato = raw_input("Opcion: ")
    if dato == 'p':
        pass
    elif dato == 'a':
        x.actualizar()
        for a in x.Atletas:
                print a.puesto,a.ide,a.pista,a.nombre,a.marca,a.club
    else:
        recep = False
"""
