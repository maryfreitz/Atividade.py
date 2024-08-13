nome = input("Seu nome: ")
disciplina = input("Disciplina: ")
nota = float(input("Nota: "))
status = " "
if nota >= 5.5 and nota <= 6: 
    nota = 6 
else: 
    print(f'{status}')
if nota >= 6: 
    status = "aprovado"
else: 
    status = "reprovado"
if nota < 0 and nota > 10: 
    print("Nota inválida. Tente novamente")
else: 
    print(f"Nota válida. {nome} está {status} em {disciplina} com nota {nota}")