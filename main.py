from modules.type_detect_hash import detect_hash
print("""
   __     ______     ______     __   __        ______   __  __     ______        ______     __     ______   ______   ______     ______    
  /\ \   /\  __ \   /\  __ \   /\ "-.\ \      /\__  _\ /\ \_\ \   /\  ___\      /\  == \   /\ \   /\  == \ /\  == \ /\  ___\   /\  == \   
 _\_\ \  \ \ \/\ \  \ \  __ \  \ \ \-.  \     \/_/\ \/ \ \  __ \  \ \  __\      \ \  __<   \ \ \  \ \  _-/ \ \  _-/ \ \  __\   \ \  __<   
/\_____\  \ \_____\  \ \_\ \_\  \ \_\\"\_\       \ \_\  \ \_\ \_\  \ \_____\     \ \_\ \_\  \ \_\  \ \_\    \ \_\    \ \_____\  \ \_\ \_\ 
\/_____/   \/_____/   \/_/\/_/   \/_/ \/_/        \/_/   \/_/\/_/   \/_____/      \/_/ /_/   \/_/   \/_/     \/_/     \/_____/   \/_/ /_/ 

|
|
|-----> Autor: JaaEnti, Pakhusso
|-----> Version: 1.0.0
|-----> https://github.com/jaaenti/Proyecto_Python_JoanTheRipper 
|                                                                                                                                                                
""")
def choose():
    while True:
        print("""
              
    --------------------------
    | 1. Detect hash type    |
    | 2. Decrypt a hash      |
    | 3. Help                |
    | 4. Exit                |
    --------------------------
              
    """)

        user_input = input("Choose the option: ").strip()  
        if user_input.isdigit():  
            option = int(user_input) 
            if option == 1:
                print("Option 1 selected: Decrypt a hash.")
                detect_hash()
                return 
            elif option == 2:
                print("Option 2 selected: .")
                detect_hash()
                return 
            elif option == 3:
                print("u")
                return 
            elif option == 4:
                print("Exiting the program. Goodbye!")
                return  
            else:
                print("Error, please select a valid option from the menu.")
        else:
            print("Error, please enter a valid number.")



choose()
