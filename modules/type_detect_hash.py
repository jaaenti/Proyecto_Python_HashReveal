import hashlib

def get_hash_input(): # Funcion para el usuario
    hash_value = input("Enter the hash you want to identify: ").strip()
    if not hash_value:
        print("Error: No valid hash entered. Please try again.")
        return None
    return hash_value

def identify_hash(hash_value): # Funcion para identificar el hash
    hash_length = len(hash_value)

    if "$argon2" in hash_value:
        return "Argon2"
    if hash_length == 32:
        # ¡¡Mirar como diferenciar MD5 de NTLM!!
        if hash_value.islower() and all(c in "abcdef0123456789" for c in hash_value):
            return "MD5"
        else:
            return "NTLM"
    elif hash_length == 40:
        return "SHA-1"
    elif hash_length == 64:
        return "SHA-256"
    elif hash_length == 128:
        return "SHA-512"
    elif hash_length == 8:
        return "CRC32"
    else:
        return "Unknown"


def validate_hash_length(hash_value): # Verifica la longitud del hash que se puso en el input anterior
    valid_lengths = [32, 40, 64, 128, 8]
    if "$argon2" in hash_value: # Esto lo he puesto porque me salia el 'Warning' y los hash tipo argon tienen '$argon2' siempre
        return
    if len(hash_value) not in valid_lengths:
        print("Warning: The entered hash does not match common lengths.")

def display_results(hash_value): # Muestra el hash que acaba de identificar
    validate_hash_length(hash_value)
    hash_type = identify_hash(hash_value)
    print("\nHash Detected:")
    print(f"Hash Type: {hash_type}")

def retry_prompt(): # Bucle para repetir el proceso...
    while True:
        retry = input("Do you want to identify another hash? (y/n): ").strip().lower()
        if retry == 'y':
            return True
        elif retry == 'n':
            print("Exiting hash detector.")
            return False
        else:
            print("Invalid input. Please enter 'y' or 'n'.")

def detect_type_hashes(): 
    while True:
        hash_value = get_hash_input()
        if not hash_value:
            continue

        display_results(hash_value)

        if not retry_prompt():
            break
detect_type_hashes()
