# nota1 = float(input('Nota1: '))
# nota2 = float(input('Nota2: '))
# nota3 = float(input('Nota3: '))

# media = ((nota1 * 2) + (nota2 * 3) + (nota3 * 5)) / 10

# print(f'A média do aluno é: {media}')

# base = int(input('Base: '))
# expoente = int(input('Expoente: '))

# resultado = base ** expoente

# print(resultado)\
    
# grausC = float(input('Digite os graus: '))

# F = ((9 * grausC) + 160) / 5

# print(f'{grausC}C em fahrenheit é: {F}F')

# n1 = int(input('N1: '))
# n2 = int(input('N2: '))

# if   n1  > n2:
#     print(n1)
# elif n1 == n2:
#     print('numeros iguais')
# else:
#     print(n2)
    
# valor   = float(input('Qual é o valor: '))
# parcelas = int(input('Qual o número de parcelas: '))
# salario = float(input('Qual o valor do salário: '))

# valorParcelas = valor / parcelas

# if valorParcelas > salario:
#     print(f'Empréstimo não foi aprovado! Parcela maior que o salário. Valor das parcelas: {valorParcelas} Salário: {salario}')
# else:
#     print(f'O empréstimo foi aprovado! Valor das parcelas: {valorParcelas} Salário: {salario}')

# nomeCorretor = str(input('Digite o nome do corretor: '))
# valorDaVenda = float(input('Digite o valor da venda: '))

# if  valorDaVenda > 50000:
#     porcentagem = 12 / 100
# elif valorDaVenda > 30000 and valorDaVenda < 50000:
#     porcentagem = 9.5 / 100
# else:
#     porcentagem = 7 / 100
    
# comissao = valorDaVenda * porcentagem
    
# print(f'nome do corretor: {nomeCorretor}')
# print(f'Valor da comissão: {comissao}')

# lado1 = int(input('Digite o primeiro lado do triangulo: '))
# lado2 = int(input('Digite o segundo lado do triangulo: '))
# lado3 = int(input('Digite o terceiro lado do triangulo: '))

# if lado1 < (lado2 + lado3) and lado2 < (lado1 + lado3) and lado3 < (lado2 + lado1):
#     if (lado1 == lado2) and (lado2 == lado3):
#         print('Triangulo equilatero')
#     elif (lado1 == lado2) != lado3 or (lado2 == lado3) != lado1:
#         print('Triangulo Isosceles!')
#     else:
#         print('Triangulo Escaleno!')
# else:
#     print('Não é um triangulo!')

# diaNumero = int(input('Digida o dia da semana em número: '))
# diasDaSemana = ['Domingo','Segunda-Feira','Terça-Feira','Quarta-Feira','Quinta-Feira','Sexta-Feira','Sábado']

# print(f'Dia da semana: {diasDaSemana[diaNumero - 1]}')
# n = 1
# match(n):
#     case 1:
#         dia = 's'
#     case 2:
#         dia = 'd'

# n1 = float(input('digite o número: '))
# op = str(input('digite o operador matemático: '))
# n2 = float(input('digite o número: '))

# match(op):
#     case '+':
#         print(f'resultado:{n1 + n2}')
#     case '-':
#         print(f'resultado:{n1 - n2}')
#     case '/':
#         print(f'resultado:{n1 / n2}')
#     case '*':
#         print(f'resultado:{n1 * n2}')
#     case _:
#         print('Operador inválido!')

# Uma loja fornece 10% de desconto para funcionários e 5% de desconto para clientes vips. Faça um programa que calcule o valor total a ser pago por uma pessoa. O programa deverá ler o valor total da compra efetuada e um código que identifique se o comprador é um cliente comum (1), funcionário (2) ou vip (3).

# cod = int(input('Digite o código de identificação: '))
# valor = int(input('Digite o valor total da compra: '))

# match(cod):
#     case 1:
#         print(f'Valor total sem desconto: R$ {valor}')
#     case 2:
#         print(f'Valor com 5% de desconto: R$ {valor - (valor * 0.05)}')
#     case 3:
#         print(f'Valor com 10% de desconto: R$ {valor - (valor * 0.1)}')
#     case _:
#         print('Código Inválido!')
# ENQUANTO VERDADEIRO FAÇA
# Executa de 0 à N;
# i = 0
# num = 1
# r = 0

# while num <= 10:
#     i = 1
#     print(f'Tabuada de: {num}')
#     while i <= 10:
#         print(f'{i} x {num} = {num * i}')
#         i += 1
#     num += 1
     
    
    

