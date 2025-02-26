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

# La funcion para crear los dataframes con los jsons
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
            with open(archivo, "r", encoding="utf-8") as f:
                contenido = json.load(f)
                data.append(contenido)
    df = pd.DataFrame(data)
    return df


####
####

# Llamar a la función para obtener el DataFrame
df = crear_data_frame()

# Función para calcular la puntuación valida
def calcular_puntuacion_valida(rating):
    if not isinstance(rating, dict):  # Ignorar si no es un diccionario
        return None
    
    # Extraer las estrellas y el número de reseñas de cada plataforma
    google = rating.get("google", {})
    tripadvisor = rating.get("tripadvisor", {})
    facebook = rating.get("facebook", {})
    
    # Calcular la puntuación valida para cada plataforma
    puntuaciones = []
    for plataforma in [google, tripadvisor, facebook]:
        if isinstance(plataforma, dict):
            stars = plataforma.get("stars")
            reviews = plataforma.get("number_of_reviews")
            if stars is not None and reviews is not None and reviews > 0:
                puntuaciones.append(stars * reviews)  # Ponderación: stars * reviews
    
    # Retornar el promedio de las puntuaciones validas
    if puntuaciones:
        return sum(puntuaciones) / len(puntuaciones)
    else:
        return None

# Aplicar la función para calcular la puntuación valida de cada local
df["puntuacion_valida"] = df["location_details"].apply(
    lambda x: calcular_puntuacion_valida(x.get("rating", {}))  # Usar un diccionario vacío si "rating" no existe
)

# Filtrar los locales por capacidad (grande, media, chica) y eliminar valores nulos en puntuación
df_filtrado = df[df["location_details"].apply(lambda x: x.get("establishment_capacity") in ["grande", "media", "chica"])]
df_filtrado = df_filtrado.dropna(subset=["puntuacion_valida"])

# Crear un DataFrame para almacenar los top-5 de cada capacidad
top_5_por_capacidad = []

# Obtener el top-5 para cada capacidad
for capacidad in ["grande", "media", "chica"]:
    df_capacidad = df_filtrado[df_filtrado["location_details"].apply(lambda x: x.get("establishment_capacity") == capacidad)]
    top_5 = df_capacidad.nlargest(5, "puntuacion_valida")[["place_name", "puntuacion_valida"]]
    top_5["capacidad"] = capacidad
    top_5_por_capacidad.append(top_5)

top_5_df = pd.concat(top_5_por_capacidad)

####
####

# Llamar a la función para obtener el DataFrame
df = crear_data_frame()

# Extraer los valores de decoración de cada local
df['decoracion'] = df['location_details'].apply(lambda x: x.get('decoration', 'Desconocido'))

# Contar la frecuencia de cada tipo de decoración
decoracion_count = df['decoracion'].value_counts().reset_index()
decoracion_count.columns = ['decoracion', 'count']