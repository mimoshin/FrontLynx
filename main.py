# KidsCanCode - Game Development with Pygame video series
# Tile-based game - Part 1
# Project setup
# Video link: https://youtu.be/3UxnelT9aCo
import pygame as pg
import clases as A
import funciones as F
import sys,os,time

class Menu:
    def __init__(self):
        self.LISTA_SERIES = []
        self.SERIE_ACTUAL = 0
        pg.init()
        self.pantalla = pg.display.set_mode((1366,768),pg.FULLSCREEN)
        self.fondo = F.cargar_Imagen("plantilla.png",False)
        self.reloj = pg.time.Clock()
        pg.key.set_repeat(500, 100)
        

    def nueva_Serie(self,texto):
        return A.Serie('C:\Users\Franco\Desktop\Ejemplos FinishLynx\Output/'+texto)
    
    def definir_Series(self):
        self.LISTA_SERIES = []
        archivos = F.listar_Archivos()
        self.TOTAL = len(archivos)
        for nume in range(self.TOTAL):
            self.LISTA_SERIES.append(self.nueva_Serie(archivos[nume]))
        self.SERIE_ACTUAL = 0
                                     
    def run(self):
        # game loop - set self.playing = False to end the game
        self.playing = True
        while self.playing:
            self.reloj.tick(15)
            self.events()
            self.texto()
            self.update()
           

    def quit(self):
        pg.quit()
        sys.exit()

    def update(self):
        pg.display.update()

    def texto(self):
        self.pantalla.blit(self.fondo,(0,0))
        self.pantalla.blit(self.LISTA_SERIES[self.SERIE_ACTUAL].s_titulo,self.LISTA_SERIES[self.SERIE_ACTUAL].s_Trect)
        for atleta in self.LISTA_SERIES[self.SERIE_ACTUAL].Atletas:
            self.pantalla.blit(atleta.s_puesto,atleta.s_Lrect)
            self.pantalla.blit(atleta.s_pista,atleta.s_Prect)
            self.pantalla.blit(atleta.s_nombre,atleta.s_Nrect)
            self.pantalla.blit(atleta.s_marca,atleta.s_Mrect)
            self.pantalla.blit(atleta.s_club,atleta.s_Crect)

    def events(self):
        # catch all events here
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.quit()
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    self.quit()
                if event.key == pg.K_LEFT:
                    if self.SERIE_ACTUAL > 0:
                        self.SERIE_ACTUAL -= 1
                if event.key == pg.K_RIGHT:
                    if self.SERIE_ACTUAL < self.TOTAL-1:
                        self.SERIE_ACTUAL += 1
                if event.key == pg.K_UP:
                    self.LISTA_SERIES[self.SERIE_ACTUAL].actualizar()
                if event.key == pg.K_DOWN:
                    self.definir_Series()
    
    

# create the game object
g = Menu()
g.definir_Series()
while True:
    g.run()

