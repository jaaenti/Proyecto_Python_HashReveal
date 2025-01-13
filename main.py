from modules.type_detect_hash import *
from modules.type_generate_hash import *
from modules.type_decrypt_hash import *
from modules.type_navigation import *


print("""
 _   _              _     ______                            _ 
| | | |            | |    | ___ \                          | |
| |_| |  __ _  ___ | |__  | |_/ /  ___ __   __  ___   __ _ | |
|  _  | / _` |/ __|| '_ \ |    /  / _ \\ \ / / / _ \ / _` || |
| | | || (_| |\__ \| | | || |\ \ |  __/ \ V / |  __/| (_| || |
\_| |_/ \__,_||___/|_| |_|\_| \_| \___|  \_/   \___| \__,_||_|
|
|
|-----> Autor: JaaEnti, Pakhusso, Roc, Pol, Toni
|-----> Version: 1.0.0
|-----> https://github.com/jaaenti/Proyecto_Python_HashReveal 
|                                                                                                                                                                
""")



def choose():
    while True:
        print("""
              
    --------------------------
    | 1. Detect hash type    |
    | 2. Encrypt hash        |
    | 3. Decrypt hash        |
    | 4. Help                |
    | 5. Exit                |
    --------------------------
               
    """)
        user_input = input("Choose the option: ").strip()  
        if user_input.isdigit():  
            option = int(user_input)
            if option == 1:
                print("Option 1 selected: Detect hash type.")
                detect_hash()  # Llama a la función para detectar el hash
                navigation_menu()  # Muestra el menú después de ejecutar la opción
            elif option == 2:
                print("Option 2 selected: Encrypt Hash.")
                generate_hash()  # Llama a la función para generar el hash
                navigation_menu()  # Muestra el menú después de ejecutar la opción
            elif option == 3:
                print("Option 3 selected: Decrypt hash.")
                hash_to_decrypt = input("Enter the hash to decrypt: ").strip()
                dictionary_file = input("Enter the path to the dictionary file: ").strip()
                try:
                    result = decrypt_hash_auto(hash_to_decrypt, dictionary_file)
                    if result:
                        print(f"Hash successfully decrypted! The original value is: {result}")
                    else:
                        print("Hash could not be decrypted with the provided dictionary.")
                except FileNotFoundError:
                    print("Error: Dictionary file not found.")
                except Exception as e:
                    print(f"An error occurred: {e}")
                navigation_menu()  
            elif option == 4:
                print("Option 4 selected: Help.")
                print("""This program allows you to:
                      1. Detect the type of a hash.
                      2. Encrypt a hash using a specified algorithm.
                      3. Decrypt a hash using a dictionary file.
                      Make sure to provide valid inputs for each option.""")
                navigation_menu()  
            elif option == 5:
                print("Exiting the program. Goodbye!")
                break  
            else:
                print("Error, please select a valid option from the menu.")
        else:
            print("Error, please enter a valid number.")

choose()
