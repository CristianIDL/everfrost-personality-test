'''
src/save_features.py: Guardar las características procesadas en un archivo pickle.
'''

from pathlib import Path
import pickle

def save_features(data):
    # Guardar datos:
    output_path = Path('data/processed_data')
    # Crear directorio si no existe
    output_path.mkdir(parents=True, exist_ok=True)

    output_path_file = output_path / f'features.pkl'

    print(f"Guardando datos procesados en {output_path_file}")

    with open(output_path_file, 'wb') as f:
        pickle.dump(data, f)

    size_mb = output_path_file.stat().st_size / (1024 * 1024)
    print(f"Tamaño del archivo guardado: {size_mb:.2f} MB")