from hashid import HashID

# Lista de longitudes y tipos confiables
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

def navgation_menu():
    while True:
        print("\nWhat do you want to do next?")
        print("1. Detect another hash")
        print("2. Go to the next module")
        print("3. Go to the next module")
        print("4. Exit program")
        choice = input("Enter your choice: ").strip()
        
        if choice == '1':
            return "retry"
        elif choice == '2':
            return "next_module"
        elif choice == '3':
            return "next_module2"
        elif choice == '4':
            print("Exiting the program. Goodbye!")
            return "exit"
        else:
            print("Invalid input. Please enter '1', '2', '3' or '4'.")

def detect_hash():
    while True:
        hash_value = input("Enter the hash to detect: ").strip()
        if not hash_value:
            print("Error: No hash provided. Try again.")
            continue

        hash_type = detect_hashid(hash_value)
        print(f"\nHash Detected: {hash_type}\n")

        action = navgation_menu()
        if action == "retry":
            continue
        elif action == "next_module":
            print("Going to the next module... (implement this functionality here)")
            break
        elif action == "exit":
            break

if __name__ == "__main__":
    detect_hash()
