from hashid import HashID
from modules.type_navigation import navigation_menu

TRUSTED_LENGTHS = {
    32: ["MD5 or NTLM"],
    40: ["SHA-1"],
    64: ["SHA-256"],
    128: ["SHA-512"]
}

def detect_hashid(hash_value):
    hashid = HashID()
    results = list(hashid.identifyHash(hash_value))

    if "$argon2" in hash_value:
        return "Argon2"
    
    hash_length = len(hash_value)

    if hash_length in TRUSTED_LENGTHS:
        trusted_types = TRUSTED_LENGTHS[hash_length]
        for result in results:
            if result[0] in trusted_types:
                return result[0]
            
        return trusted_types[0]
    
    if results:
        return results[0][0]
    
    return "Unknown Hash"

def detect_hash():
    while True:
        hash_value = input("Enter the hash to detect: ").strip()
        if not hash_value:
            print("Error: No hash provided. Try again.")
            continue

        hash_type = detect_hashid(hash_value)
        print(f"\nHash Detected: {hash_type}\n")

        action = navigation_menu()
        if action == "detect":
            print("Restarting Hash Detection...")
            continue
        elif action == "encrypt":
            from modules.type_generate_hash import generate_hash
            print("Going to Encrypt Hash module...")
            generate_hash()  # Llama al módulo de generación de hash
            break
        elif action == "decrypt":
            from modules.type_decrypt_hash import decrypt_hash
            print("Going to Decrypt Hash module...")
            decrypt_hash()  # Llama al módulo de desencriptar hash
            break
        elif action == "exit":
            print("Exiting the program. Goodbye!")
            break
