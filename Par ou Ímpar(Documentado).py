"""
Módulo: Jogo par ou ímpar
Autor: [Thiago Fonseca]
Data: [05/04/2025]

Descrição:
Este programa implementa um jogo simples onde o usuário insere um número entre 1 e 1000 e o programa retorna dizendo se o número escolhido é par ou ímpar. 
O usuário pode digitar "sair" para encerrar o jogo.

Regras:
1. O jogador deve inserir um número inteiro entre 1 e 1000.
2. Se o número inserido for inválido (não numérico ou fora do intervalo), uma mensagem de erro é exibida.
3. O jogo continua até que o usuário insira "sair".

Dependências:
- Python 3.8.18
"""

def jogo_parouimpar():
    """
    Inicia o jogo de par ou ímpar.
    O usuário insere um número entre 1 e 1000.
    O programa retorna informando se o número inserido é par ou ímpar.
    O jogo continua até que o usuário digite sair.
    """
    while True:
        # Solicita a entrada do usuário
        num = input('Boas-vindas! Digite um número entre 1 e 1000 ou digite "sair" para encerrar o jogo:\n')

        # Verifica se o usuário quer sair
        if num.lower() == 'sair':
            print('\nJogo encerrado!')
            break

        # Verifica se a entrada é um número válido
        if not num.isdigit():
            print('\nNúmero inválido!')
            continue

        # Converte a entrada para número inteiro
        num = int(num)

        # Verifica se o número está no intervalo permitido
        if num < 1 or num > 1000:
            print('\nNúmero inválido!\n')
            continue

        # Verifica se o número é par ou ímpar
        if num % 2 == 0:
            print(f'\n{num} é um número par.\n')
        else:
            print(f'\n{num} é um número ímpar.\n')

# Executa o jogo ao rodar o script
if __name__ == "__main__":
    jogo_parouimpar()
