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
|-----> https://github.com/jaaenti 
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

        user_input = input("Choose the option 'number': ").strip()  
        if user_input.isdigit():  
            option = int(user_input) 
            if option == 1:
                print("s")
                return 
            elif option == 2:
                print("e")
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
