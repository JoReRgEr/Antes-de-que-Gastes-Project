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
    ruta = "D:\PROGRAMACION\Antes-de-que-Gastes-Project\Restaurantes-y-Bares"
    data = []
    for archivo in glob.glob(ruta + "/*.json"):
        with open(archivo, 'r', encoding='utf-8') as f:
            contenido = json.load(f)
            data.append(contenido)     
    df = pd.DataFrame(data)
    return df