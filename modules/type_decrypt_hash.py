import hashlib
import string
import itertools
import time
from modules.type_detect_hash import detect_hashid
from modules.type_navigation import navigation_menu
from argon2 import PasswordHasher
from argon2.exceptions import VerifyMismatchError

DICTIONARY_FILE = "dictionary.txt"
ph = PasswordHasher()

def cargar_diccionario(archivo):
    """
    Carga las palabras de un archivo de diccionario.
    """
    try:
        with open(archivo, 'r', encoding='ISO-8859-1') as file:
            return [line.strip() for line in file]
    except FileNotFoundError:
        print(f"Error: El archivo {archivo} no fue encontrado.")
        raise
    except Exception as e:
        print(f"Error al leer el archivo de diccionario: {e}")
        raise

def desencriptar_argon2(hash_objetivo, diccionario):
    """
    Intenta desencriptar un hash Argon2 probando palabras en un diccionario.
    """
    for palabra in diccionario:
        try:
            ph.verify(hash_objetivo, palabra)
            return palabra  
        except VerifyMismatchError:
            continue
    return None

def brute_force_argon2(hash_objetivo, max_length=4):
    """
    Intenta desencriptar un hash Argon2 usando fuerza bruta generando combinaciones
    de caracteres posibles.
    """
    caracteres = string.ascii_letters + string.digits
    for length in range(1, max_length + 1):
        for comb in itertools.product(caracteres, repeat=length):
            palabra = ''.join(comb)
            try:
                ph.verify(hash_objetivo, palabra)
                return palabra
            except VerifyMismatchError:
                continue
    return None

def desencriptar_hash(hash_objetivo, algoritmo, diccionario):
    """
    Intenta desencriptar un hash probando palabras en un diccionario (para MD5, SHA-1, SHA-256, etc).
    """
    algoritmos = [algoritmo.lower()] if " or " not in algoritmo else algoritmo.lower().split(" or ")

    for palabra in diccionario:
        for alg in algoritmos:
            try:
                hash_generado = hashlib.new(alg.strip(), palabra.encode()).hexdigest()
                if hash_generado == hash_objetivo:
                    return palabra
            except ValueError:
                continue
    return None

def brute_force_decrypt_hash(hash_objetivo, max_length=4):
    """
    Intenta desencriptar un hash utilizando fuerza bruta (solo para MD5 y SHA).
    """
    caracteres = string.ascii_letters + string.digits 
    for length in range(1, max_length + 1):
        for comb in itertools.product(caracteres, repeat=length):
            palabra = ''.join(comb)
            hash_generado = hashlib.md5(palabra.encode()).hexdigest() 
            if hash_generado == hash_objetivo:
                return palabra
            for sha_type in ['sha1', 'sha256', 'sha512']: 
                hash_generado = hashlib.new(sha_type, palabra.encode()).hexdigest()
                if hash_generado == hash_objetivo:
                    return palabra
    return None

def decrypt_hash_auto(hash_objetivo):
    """
    Detecta automáticamente el tipo de hash y lo intenta desencriptar usando un diccionario o fuerza bruta.
    """
    print(f"Detectando el tipo de hash para: {hash_objetivo}")
    tipo_hash = detect_hashid(hash_objetivo)

    if tipo_hash == "Unknown Hash":
        print("No se pudo determinar el tipo de hash. Intentando con fuerza bruta...")
        start_time = time.time()  
        resultado = brute_force_decrypt_hash(hash_objetivo)
        end_time = time.time()  

        elapsed_time = end_time - start_time  
        print(f"Tiempo de ejecución (fuerza bruta): {elapsed_time:.2f} segundos.")

        if resultado:
            print(f"¡Hash desencriptado exitosamente con fuerza bruta! El valor original es: {resultado}")
        else:
            print("No se pudo desencriptar el hash usando fuerza bruta.")
        return None

    print(f"Se detectó el tipo de hash: {tipo_hash}")
    try:
        diccionario = cargar_diccionario(DICTIONARY_FILE)
        if tipo_hash.lower() == "argon2":
            start_time = time.time()  
            resultado = brute_force_argon2(hash_objetivo)  
            end_time = time.time()  

            elapsed_time = end_time - start_time  
            print(f"Tiempo de ejecución (fuerza bruta Argon2): {elapsed_time:.2f} segundos.")

            if resultado:
                print(f"¡Hash Argon2 desencriptado exitosamente! El valor original es: {resultado}")
            else:
                print("No se pudo desencriptar el hash Argon2 usando fuerza bruta.")
        else:
            start_time = time.time()  
            resultado = desencriptar_hash(hash_objetivo, tipo_hash, diccionario)
            end_time = time.time()

            elapsed_time = end_time - start_time 
            print(f"Tiempo de ejecución: {elapsed_time:.2f} segundos.")

        if resultado:
            print(f"¡Hash desencriptado exitosamente! El valor original es: {resultado}")
        else:
            print(f"No se pudo desencriptar el hash usando el tipo detectado ({tipo_hash}).")
    except Exception as e:
        print(f"Error durante la desencriptación: {e}")
        return None

def decrypt_hash():
    """
    Función principal para manejar la desencriptación de hashes.
    """
    while True:
        print("\n--- Decrypt Hash ---")
        hash_objetivo = input("Enter the hash to decrypt: ").strip()
        if not hash_objetivo:
            print("Error: Hash no puede estar vacío.")
            continue

        try:
            decrypt_hash_auto(hash_objetivo)
        except FileNotFoundError:
            print(f"Error: El archivo {DICTIONARY_FILE} no fue encontrado en la carpeta del proyecto.")
        except Exception as e:
            print(f"Error inesperado: {e}")

        action = navigation_menu()
        if action == "detect":
            from modules.type_detect_hash import detect_hash
            print("Going to Detect Hash module...")
            detect_hash()
        elif action == "encrypt":
            from modules.type_generate_hash import generate_hash
            print("Going to Encrypt Hash module...")
            generate_hash()
        elif action == "decrypt":
            print("Restarting Hash Decryption...")
        elif action == "exit":
            print("Exiting the program. Goodbye!")
            break


