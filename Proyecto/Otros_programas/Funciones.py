import glob
import json
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
import numpy as np
from collections import Counter
import csv 
import warnings
warnings.filterwarnings("ignore")

def crear_data_frame():
    rutas = ["D:\PROGRAMACION\Antes-de-que-Gastes-Project\Restaurantes-y-Bares\Arroyo Naranjo",
             "D:\PROGRAMACION\Antes-de-que-Gastes-Project\Restaurantes-y-Bares\Boyeros",
             "D:\PROGRAMACION\Antes-de-que-Gastes-Project\Restaurantes-y-Bares\Centro Habana",
             "D:\PROGRAMACION\Antes-de-que-Gastes-Project\Restaurantes-y-Bares\Cerro",
             "D:\PROGRAMACION\Antes-de-que-Gastes-Project\Restaurantes-y-Bares\Cotorro",
             "D:\PROGRAMACION\Antes-de-que-Gastes-Project\Restaurantes-y-Bares\Diez de Octubre",
             "D:\PROGRAMACION\Antes-de-que-Gastes-Project\Restaurantes-y-Bares\Guanabacoa",
             "D:\PROGRAMACION\Antes-de-que-Gastes-Project\Restaurantes-y-Bares\Habana del Este",
             "D:\PROGRAMACION\Antes-de-que-Gastes-Project\Restaurantes-y-Bares\Habana Vieja",
             "D:\PROGRAMACION\Antes-de-que-Gastes-Project\Restaurantes-y-Bares\La Lisa",
             "D:\PROGRAMACION\Antes-de-que-Gastes-Project\Restaurantes-y-Bares\Marianao",
             "D:\PROGRAMACION\Antes-de-que-Gastes-Project\Restaurantes-y-Bares\Playa",
             "D:\PROGRAMACION\Antes-de-que-Gastes-Project\Restaurantes-y-Bares\Plaza",
             "D:\PROGRAMACION\Antes-de-que-Gastes-Project\Restaurantes-y-Bares\Regla",
             "D:\PROGRAMACION\Antes-de-que-Gastes-Project\Restaurantes-y-Bares\San Miguel",]
    data = []
    for ruta in rutas:
        for archivo in glob.glob(ruta + "/*.json"):
            with open(archivo, 'r', encoding='utf-8') as f:
                contenido = json.load(f)
                data.append(contenido)
    df = pd.DataFrame(data)
    return df