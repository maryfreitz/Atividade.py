login = input("Login: ")
senha = input("Senha: ")
if login == "admin" and senha == "123": 
    print(f"Olá {login}, seja bem-vindo!")
else:
    print("Login ou senha incorretos")