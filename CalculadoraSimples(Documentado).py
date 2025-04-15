"""
Modulo:CalculadoraSimples.py
Autor:Thiago Fonseca Azeredo
Data:07/04/2025
Descrição:Implementação de um programa simples de calculos basicos em python.
"""
#Calculadora Simples

while True:
    
    especial = ['+','-','/','*','sair']  #valida as entradas
    oper = input('Escolha um operador (+ | - | / | *) ou sair para encerrar a caculadora:\n')
    if oper.lower() == 'sair': # encerramento do programa
        print('Calculadora encerrada!')    
        break
    if not oper  !=  especial: #confere se não vai ter alguma entrada diferente
        print('\nEntrada inválida!\n')
        continue
    num1 = int(input('Digite um número inteiro:\n'))
    num2 = int(input('Digite outro número inteiro:\n'))

#Condição soma
    if oper == '+':
        soma = num1 + num2
        print(f'\n{num1} {oper} {num2} = {soma}\n')
        continue
#Condição subtração    
    elif oper == '-':
          soma = num1 - num2
          print(f'\n{num1} {oper} {num2} = {soma}\n')
          continue
#Condição multiplicação  
    elif oper == '*':
          soma = num1 * num2
          print(f'\n{num1} {oper} {num2} = {soma}\n')
          continue
#Condição divisão      
    elif oper == '/':
          soma = num1 / num2
          print(f'\n{num1} {oper} {num2} = {soma:.1f}\n')
          continue

    
  
           #break
    
  
    