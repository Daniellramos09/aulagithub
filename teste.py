
#Fibonacci
def CalcFatorial(n):
    f = 1
    for i in range(n, 0, -1):
        f *= i
    return f

n = int(input("Digite um número: "))
print(f"O fatorial de {n} é {CalcFatorial(n)}")




print("Por favor, insira a base e o expoente.")
try:
    
    base_usr = float(input("Digite o valor da BASE: "))
    expo_usr = float(input("Digite o valor do EXPOENTE: "))
    
    resultado_calculo = calcular_potencia(base_usr, expo_usr)
    

    print(f"O resultado de {base_usr} elevado a {expo_usr} é: {resultado_calculo:.2f}")

except ValueError:
    print("\n[ERRO] Entrada inválida!")
    print("Você deve digitar apenas valores numéricos (ex: 5 ou 2.5).")
except OverflowError:
    print("\n[ERRO] O resultado é um número grande demais para exibir.")

print("------------------------------------------")
print("Fim do programa.")