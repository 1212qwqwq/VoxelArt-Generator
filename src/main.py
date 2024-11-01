import os
import trimesh
import torch
import zipfile
from PIL import Image

# --- Función para cargar y leer modelos ---
def load_model(file_path):
    try:
        # Verifica si es un archivo comprimido
        if file_path.endswith(".zip"):
            with zipfile.ZipFile(file_path, 'r') as zip_ref:
                zip_ref.extractall("data/extracted/")
                file_path = "data/extracted/" + [f for f in zip_ref.namelist() if f.endswith(".obj")][0]

        # Cargar el archivo 3D
        model = trimesh.load(file_path)
        print(f"Modelo cargado exitosamente desde {file_path}")
        return model
    except Exception as e:
        print(f"Error al cargar el modelo: {e}")
        return None

# --- Función para entrenar el modelo ---
def train_model(model_data):
    print("Iniciando entrenamiento del modelo...")

    # Ejemplo de proceso de entrenamiento
    for epoch in range(5):  # Simulación de 5 ciclos de entrenamiento
        print(f"Ciclo de entrenamiento {epoch + 1}/5 completado.")

    # Guardar el modelo después de entrenar
    model_path = "models/model_checkpoint.pt"
    torch.save(model_data, model_path)
    print(f"Modelo guardado en '{model_path}'")

# --- Generador de modelos basados en descripciones ---
def generate_model(description):
    print(f"Generando un modelo de voxel art basado en la descripción: '{description}'")
    # Aquí es donde añadirías la generación de modelos a partir de texto en el futuro
    return f"Modelo '{description}' generado (simulación)."

# --- Procesar texturas del modelo ---
def load_textures(model_path):
    texture_path = os.path.join("textures", model_path)
    if os.path.exists(texture_path):
        texture = Image.open(texture_path)
        print("Textura cargada exitosamente.")
        return texture
    else:
        print("No se encontraron texturas.")
        return None

# --- Menú principal interactivo ---
def main_menu():
    while True:
        print("\n=== Menú Principal ===")
        print("1. Cargar y leer un modelo 3D")
        print("2. Entrenar el modelo")
        print("3. Generar un modelo a partir de una descripción")
        print("0. Salir")
        choice = input("Selecciona una opción: ")

        if choice == "1":
            file_path = input("Ingresa la ruta del archivo 3D (.obj o .zip): ")
            model = load_model(file_path)
            if model is not None:
                print("Modelo cargado exitosamente.")
                load_textures(file_path)
        elif choice == "2":
            model_data = "datos_de_entrenamiento"  # Esto debería ser el modelo real
            train_model(model_data)
        elif choice == "3":
            description = input("Describe el modelo que deseas generar: ")
            generate_model(description)
        elif choice == "0":
            print("Saliendo del programa.")
            break
        else:
            print("Opción no válida. Intenta de nuevo.")

# Ejecuta el menú principal
if __name__ == "__main__":
    main_menu()
