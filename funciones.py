import os
import pygame as pg

def listar_Archivos():
    Archivos = []
    lista = os.listdir("C:\Users\Franco\Desktop\Ejemplos FinishLynx\Output")
    for indexi in lista:
        if '.lif' in indexi:
            Archivos.append(indexi)
    return Archivos

def cargar_Imagen(filename, transparent=False):
        try: imagen = pg.image.load(filename)
        except pg.error:
            print("Fallo cargar imagen")
        imagen = imagen.convert()
        if transparent:
                color = imagen.get_at((0,0))
                imagen.set_colorkey(color, RLEACCEL)
        return imagen

