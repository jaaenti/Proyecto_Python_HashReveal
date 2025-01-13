import hashlib


# Función para cargar un diccionario desde un archivo
def cargar_diccionario(archivo):
    try:
        with open(archivo, 'r', encoding='utf-8') as f:
            return [linea.strip() for linea in f]
    except FileNotFoundError:
        print(f"Error: El archivo {archivo} no se encuentra.")
        return []
    except Exception as e:
        print(f"Error al leer el archivo: {e}")
        return []

# Función para desencriptar un hash comparando con un diccionario
def desencriptar_hash(hash_objetivo, algoritmo, diccionario):
    if algoritmo not in hashlib.algorithms_guaranteed:
        print(f"Error: El algoritmo {algoritmo} no es válido.")
        return None

    # Se calculan los hashes solo una vez por cada palabra en el diccionario
    for palabra in diccionario:
        hash_generado = hashlib.new(algoritmo, palabra.encode()).hexdigest()
        if hash_generado == hash_objetivo:
            return palabra
    return None


if __name__ == "__main__":
    # Diccionario de hashes de ejemplo
    hashes_ejemplo = {
        "5d41402abc4b2a76b9719d911017c592": "md5",  # Hash para "hello"
        "2aae6c35c94fcfb415dbe95f408b9ce91ee846ed": "sha1",  # Hash para "hello"
    }

    # Ruta al archivo "rockyou.txt"
    archivo_diccionario = "rockyou.txt" 

    # Cargar el diccionario desde un archivo
    diccionario = cargar_diccionario(archivo_diccionario)

    if diccionario:
        # Intentar desencriptar cada hash con su respectivo algoritmo
        for hash_objetivo, algoritmo in hashes_ejemplo.items():
            resultado = desencriptar_hash(hash_objetivo, algoritmo, diccionario)
            if resultado:
                print(f"Hash {hash_objetivo} ({algoritmo}) desencriptado: {resultado}")
            else:
                print(f"No se ha podido desencriptar el hash {hash_objetivo} ({algoritmo})")
    else:
        print("No se cargó el diccionario correctamente.")
