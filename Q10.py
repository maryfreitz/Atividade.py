print('Você deseja abrir a calculadora?')
print("""
        6 - sim 
        7 - não 
          """)
op = str(input('op: '))
if op == "7":
    print("que pena :( ")
while op != "7" :
    print('''
          -------- Calc.py -------- 
          Escolha uma opção 
          1 - soma 
          2 - subtração 
          3 - multiplicação 
          4 - divisão 
          5 - elevar ao quadrado 
          0 - sair 
          --------------------------
          ''')
    escolha = str(input('op: '))
    if escolha == "1":
            print("você escolheu soma")
            n1 = float(input("Diga um número: "))
            n2 = float(input("Diga outro número: "))
            print(f'a soma é igual a {n1 + n2}')
    if escolha == "2":
            print("você escolheu subtração")
            n3 = float(input("Diga um número: "))
            n4 = float(input("Diga outro número: "))
            print(f'a subtração é igual a {n3 - n4}')
    if escolha == "3":
            print("você escolheu multiplicação")
            n5 = float(input("Diga um número: "))
            n6 = float(input("Diga outro número: "))
            print(f'a multiplicação é igual a {n5 * n6}')
    if escolha == "4":
            print("você escolheu divisão")
            n7 = float(input("Diga um número: "))
            n8 = float(input("Diga outro número: "))
            print(f'a divisão é igual a {n7 / n8}')
    if escolha == "5":
            print("você escolheu elevar ao quadrado")
            n9 = float(input("Diga um número: "))
            print(f'{n9} ao quadrado é igual a {n9*n9}')
    if escolha == "0":
           print("Bye bye :) ")
           break 