def navigation_menu():
    """
    Muestra un menú de navegación después de realizar una acción,
    permitiendo al usuario decidir qué hacer a continuación.
    """
    while True:
        print("\nWhat do you want to do next?")
        print("1. Detect a hash")
        print("2. Encrypt a hash")
        print("3. Decrypt a hash")
        print("4. Exit program")
        
        choice = input("Enter your choice: ").strip()
        
        if choice == '1':
            return "detect"  # Regresa a la opción de detección de hash
        elif choice == '2':
            return "encrypt"  # Regresa a la opción de encriptar hash
        elif choice == '3':
            return "decrypt"  # Regresa a la opción de desencriptar hash
        elif choice == '4':
            print("Exiting the program. Goodbye!")
            return "exit"  # Sale del programa
        else:
            print("Invalid input. Please enter '1', '2', '3', or '4'.")
