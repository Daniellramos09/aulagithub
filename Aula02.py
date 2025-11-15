

# Exercicio 1
"""n1 = int(input("Infome o dia da semana:"))
if n1 == 1 :
    print("domingo")
elif n1 == 2:
    print("Segunda")
elif n1 == 3:
    print("Terça")
elif n1 == 4:
    print("Quarta")
elif n1 == 5:
    print("Quinta")
elif n1 == 6:
    print("Sexta")
elif n1 == 7:
    print("Sabado")
else:
   print("Numero não correspondente")"""
   
   

# Exercicio 2
"""n1 = int(input("n1 escreva"))
n2 = int(input("n2 escreva"))
 
if n1 > n2:
    print("ordem crescente", n1, n2)
else:
    print("ordem descrecente", n2, n1)"""
   
 


# Exercicio 3
"""n1 = int(input("escreva um numero:"))
if n1 % 2 == 0:
    print("par")
else:
    print("Impar")"""
 




# Exercicio 4
"""n1 = int(input("escreva a nota 1"))
n2 = int(input("escreva a nota 2"))
n3 = int(input("escreva a nota 3"))
 
media = (n1 + n2 + n3) / 3
 
if media > 6:
    print("Aprovado")
else: print("Reprovado")"""
 




# Exercicio 5
 
"""peso = int(input("escreva o seu peso:"))
altura = float(input("escreva escreva sua altura"))
 
imc = peso / (altura * altura)
 
if imc < 26:
    print("Normal")
elif imc == 26 and imc < 30:
    print("Obeso")
else :
    print("Obeso")"""


# Exercicio 6


T = 0
Resp = 1
while Resp != 0:
    print(" 1 - hot Dog \n 2 - Hambuguer \n  3 - chesseburguer \n 4 - refrigerante em lata \n   5 - batata fritas \n 6 - misto quente \n 7 - sucos naturais \n ")
    cod = int(input("Informe a opção:"))    
    while (cod < 1 or cod > 7):
        cod = int(input("Informe a opção:"))
    Q = int(input("Informe a quantidade desejada:"))
    match (cod):
            case 1 : P = 11.20
            case 2 : P = 16.60  
            case 3 : P = 22.00
            case 4 : P = 8.00
            case 5 : P = 32.50
            case 6 : P = 12.00 
            case 7 : P = 8.0
    Vp = P * Q
    T = T + Vp
    Resp = int(input("Deseja mais um produto?"))
   
print(f"valor a ser pago é {T: .2f}")      


