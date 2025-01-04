 import hashlib


def cargar_diccionario(archivo):
    with open(archivo, 'r', encoding='utf-8') as archivo:
        return [linea.strip() for linea in archivo]


def desencriptar_hash(hash_objetivo, algoritmo, diccionario):
    for palabra in diccionario:
        hash_generado = hashlib.new(algoritmo, palabra.encode()).hexdigest()
        if hash_generado == hash_objetivo:
            return palabra
    return None


import hashlib


def cargar_diccionario(archivo):
    with open(archivo, 'r', encoding='utf-8') as archivo:
        return [linea.strip() for linea in archivo]


def desencriptar_hash(hash_objetivo, algoritmo, diccionario):
    for palabra in diccionario:
        hash_generado = hashlib.new(algoritmo, palabra.encode()).hexdigest()
        if hash_generado == hash_objetivo:
            return palabra
    return None


if __name__ == "__main__":
    
    hashes_ejemplo = {
        "5d41402abc4b2a76b9719d911017c592": "md5",  
        "2aae6c35c94fcfb415dbe95f408b9ce91ee846ed": "sha1", 
    }
    archivo_diccionario = "diccionario.txt"

   
    diccionario = cargar_diccionario(archivo_diccionario)

    for hash_objetivo, algoritmo in hashes_ejemplo.items():
        resultado = desencriptar_hash(hash_objetivo, algoritmo, diccionario)
        if resultado:
            print(f"Hash {hash_objetivo} ({algoritmo}) desencriptado: {resultado}")
        else:
            print(f"No se ha podido desencriptar el hash {hash_objetivo} ({algoritmo})")
