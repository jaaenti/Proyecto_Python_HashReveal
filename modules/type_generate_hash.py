import hashlib
from argon2 import PasswordHasher
from argon2.exceptions import HashingError

Hashes = ["MD5", "SHA-1", "SHA-256", "SHA-512","Argon2"]

def password_client():
    password = input("Enter your password: ").strip()
    if not password:
        print("Invalid password please enter another one")
        return None
    return password

def select_hash():
    print("""
  -------------
 |  1.MD5      |
 |  2.SHA-1    |
 |  3.SHA-256  |
 |  4.SHA-512  |
 |  5.Argon2   |    
  -------------
          """)
    while True:
       choice = input("Select Hash: ").strip()
       if choice == '1':
           return "MD5"
       elif choice == '2':
            return "SHA-1"
       elif choice == '3':
                return "SHA-256"
       elif choice == '4':
            return "SHA-512"
       elif choice == '5':
           return "Argon2"
       else:
           print("Invalid choice. Please enter a number between 1 and 5.")

def generate_hash():
    """
    Función principal para encriptar contraseñas.
    """
    while True:
        password = password_client()
        if not password:
            continue

        hash_type = select_hash()
        hashed_password = hashlib.new(hash_type.lower(), password.encode()).hexdigest()

        print(f"\nHash Generated ({hash_type}): {hashed_password}")

        retry = input("\nDo you want to encrypt another password? (y/n): ").strip().lower()
        if retry != 'y':
            print("Exiting encryption module.")
            break

if __name__ == "__main__":
    generate_hash()
