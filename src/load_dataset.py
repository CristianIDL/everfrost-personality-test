'''
src/load_dataset.py: Procesamiento del dataset de vectores de características. 
'''

from src.save_features import save_features
import numpy as np
import pandas as pd
import time

def load_dataset(path='data/personality_dataset.csv'):

    tiempo_inicio = time.time()

    # Extraer datos del CSV
    df = pd.read_csv(path)

    # Verificar si 'class_label' está en las columnas
    if 'class_label' not in df.columns:
        raise ValueError("El dataset debe contener una columna 'class_label'.")

    # Array con los vectores de características
    X = np.array(df.drop(columns=['class_label']))
    
    # Array con la etiqueta de clase
    y = np.array(df['class_label'])

    tiempo_total = time.time() - tiempo_inicio

    print(f"Tiempo de procesamiento del dataset: {tiempo_total:.2f} segundos")
    print(f"Número de muestras: {X.shape[0]}, Número de características: {X.shape[1]}")

    # Crear diccionario de datos
    data = {
        "features": X,
        "labels": y,
        "n_samples": X.shape[0],
        "n_features": X.shape[1]
    }

    return data

if __name__ == "__main__":

    # Cargamos las características y etiquetas del dataset
    datos_cargados = load_dataset('data/personality_dataset.csv')

    print("Datos cargados:", list(datos_cargados['features'].shape), list(datos_cargados['labels'].shape))    
    
    # Guardamos los datos procesados
    save_features(datos_cargados)