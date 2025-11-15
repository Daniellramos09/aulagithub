n = int(input("Digite um número: "))
fatorial = 1
soma = 1
resto = 0
for i in range(1, n + 1, 1):
    fatorial *= i
    soma = (n *  (n - i)) * soma
    
    print(soma)
print("O fatorial de", {n}, "é", fatorial)



def CalcFatorial(n):
    f = 1
    for i in range(n, 0, -1):
        f *= i
    return f

n = int(input("Digite um número: "))
print(f"O fatorial de {n} é {CalcFatorial(n)}")


base = int(input("Digite a base: "))
expoente = int(input("Digite o expoente: "))
def calcular_potencia(base, expoente):
   
   
    resultado = base ** expoente
    return resultado

# --- Início do Programa Principal ---

print("Bem-vindo à Calculadora de Exponenciação!")
print("Por favor, insira a base e o expoente.")
print("------------------------------------------")


try:
   
    base_usr = float(input("Digite o valor da BASE: "))
    expo_usr = float(input("Digite o valor do EXPOENTE: "))
    
    resultado_calculo = calcular_potencia(base_usr, expo_usr)
    
   
    print("\n--- Resultado ---")
    print(f"O resultado de {base_usr} elevado a {expo_usr} é: {resultado_calculo:.2f}")

except ValueError:
    
    print("\n[ERRO] Entrada inválida!")
    print("Você deve digitar apenas valores numéricos (ex: 5 ou 2.5).")
except OverflowError:
  
    print("\n[ERRO] O resultado é um número grande demais para exibir.")

print("------------------------------------------")
print("Fim do programa.")


try:    
    n1 = float(input("numero 1: "))
    operadorAritmetico = (input("Operador Aritmético: "))
    n2 = float(input("numero 2: "))

    if operadorAritmetico ==  "soma":
        resultado_calculo = n1 + n2
    elif operadorAritmetico ==  "subtração":
         resultado_calculo = n1 - n2
    elif operadorAritmetico ==  "divisão":
        resultado_calculo = n1 * n2
    else:
         resultado_calculo = n1 / n2

    print(f"O resultado de {n1} {operadorAritmetico} {n2} é: {resultado_calculo:.2f}")
except ZeroDivisionError:
        print("Erro: Divisão por zero não é permitida.")



'''n1 = int(input("numero 1: "))
F = 1
for i in range(1, n1):
     F = F * (i - 1) + F * (i - 2)
     print(f"{F},")'''



'''PROGRAMA DA AGENDA '''
agenda = {}
def adicionar_contato(nome, telefone):
    agenda[nome] = telefone
    print(f"Contato {nome} adicionado com sucesso.")
def exibir_agenda():
    if not agenda:
        print("A agenda está vazia.")
    else:
        print("Contatos na agenda:")
        for nome, telefone in agenda.items():
            print(f"Nome: {nome}, Telefone: {telefone}")
def buscar_contato(nome):
    if nome in agenda:
        print(f"Contato encontrado - Nome: {nome}, Telefone: {agenda[nome]}")
    else:
        print(f"Contato {nome} não encontrado na agenda.")
while True:
    print("\nMenu da Agenda:")
    print("1. Adicionar Contato")
    print("2. Exibir Agenda")
    print("3. Buscar Contato")
    print("4. Sair")
    escolha = input("Escolha uma opção (1-4): ")
    if escolha == '1':
        nome = input("Digite o nome do contato: ")
        telefone = input("Digite o telefone do contato: ")
        adicionar_contato(nome, telefone)
    elif escolha == '2':
        exibir_agenda()
    elif escolha == '3':
        nome = input("Digite o nome do contato a buscar: ")
        buscar_contato(nome)
    elif escolha == '4':
        print("Saindo da agenda. Até mais!")
        break
    else:
        print("Opção inválida. Por favor, escolha uma opção válida.")



print("=== AGENDA PYTHON ===")
agenda = {}
while True:
    print("\nMenu da Agenda:")
    print("1. Adicionar Contato")
    print("2. Exibir Agenda")
    print("3. Buscar Contato")
    print("4. Sair")
    escolha = input("Escolha uma opção (1-4): ")
    if escolha == '1':
        nome = input("Digite o nome do contato: ")
        telefone = input("Digite o telefone do contato: ")
        adicionar_contato(nome, telefone)
    elif escolha == '2':
        exibir_agenda()
    elif escolha == '3':
        nome = input("Digite o nome do contato a buscar: ")
        buscar_contato(nome)
    elif escolha == '4':
        print("Saindo da agenda. Até mais!")
        break
    else:
        print("Opção inválida. Por favor, escolha uma opção válida.")



