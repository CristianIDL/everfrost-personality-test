'''
src/train_model.py: Entrenamiento del modelo de clasificación utilizando los vectores de características extraídos.
'''

from load_dataset import load_dataset
from save_features import save_features
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
import numpy as np

def train_model(data,knn_k=3):

    X = data['features']
    y = data['labels']

    # Dividir el dataset en conjunto de entrenamiento y prueba
    X_train, X_test, y_train, y_test = train_test_split(
        X, 
        y, 
        random_state=42,
        test_size=0.2,)
    
    # Crear el modelo KNN
    knn = KNeighborsClassifier(n_neighbors=knn_k, metric='euclidean', weights='distance')
    knn.fit(X_train, y_train)
    # Guardar el modelo entrenado en un archivo pickle
    save_features(knn)

    # Métricas
    accuracy = knn.score(X_test, y_test)
    print(f"Precisión del modelo KNN con k={knn_k}: {accuracy:.2f}")

    # Matriz de confusión
    cm = confusion_matrix(y_test, knn.predict(X_test))
    print("Matriz de confusión:")
    print(cm)

    # Visualizar matriz de confusión
    # Obtener nombres únicos de las etiquetas
    unique_labels = np.unique(y)
    
    # Crear la visualización
    disp = ConfusionMatrixDisplay(confusion_matrix=cm, display_labels=unique_labels)
    disp.plot(cmap='Blues', values_format='d')
    plt.title(f'Matriz de Confusión - KNN (k={knn_k})')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

    return knn
    
if __name__ == "__main__":
    # Cargamos los datos procesados
    data = load_dataset('data/personality_dataset.csv')

    # Entrenamos el modelo con los datos cargados
    knn = train_model(data, knn_k=3)

    # Hacemos una prueba con una clasificación de ejemplo
    # Ejemplo de vector de características para clasificación
    astrofusioner_example = [0.43,-0.83,-0.13,-0.01,0.23,0.37,0.03]  # Ejemplo de vector para Astrofusioner
    intergraph_example = [-0.55,0.04,-0.58,0.45,-0.63,-0.05,0.7]  # Ejemplo de vector para Intergraph
    esentromancer_example = [-0.11,0.81,0.61,-0.37,-0.09,-0.9,-0.51]  # Ejemplo de vector para Essentromancer

    # Clasificar el ejemplo utilizando el modelo entrenado
    prediction = knn.predict([astrofusioner_example, intergraph_example, esentromancer_example])
    print(f"Predicción para Astrofusioner: {prediction[0]}")
    print(f"Predicción para Intergraph: {prediction[1]}")
    print(f"Predicción para Essentromancer: {prediction[2]}")

    # Ejemplo de vector nuevo para clasificación
    new_example = [0.75, -0.61, -0.84, 0.91, 0.56, 0.72, 0.25]  # Ejemplo de vector para clasificación
    prediction = knn.predict([new_example])
    print(f"Predicción para Ejemplo nuevo: {prediction[0]}")

