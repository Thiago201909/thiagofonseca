"""
Módulo: Jogo de Adivinhação de Números
Autor: [Thiago Fonseca]
Data: [03/04/2025]

Descrição:
Este programa implementa um jogo simples onde o usuário tenta adivinhar um número 
gerado aleatoriamente entre 1 e 50. O usuário pode digitar "sair" para encerrar o jogo.

Regras:
1. O jogador deve inserir um número inteiro entre 1 e 50.
2. Se o número inserido for inválido (não numérico ou fora do intervalo), uma mensagem de erro é exibida.
3. O número gerado aleatoriamente é comparado com a escolha do jogador.
4. O jogo continua até que o usuário insira "sair".

Dependências:
- Python 3.x (módulo `random` embutido)

"""

import random

def jogo_adivinhacao():
    """
    Inicia o jogo de adivinhação de números. O usuário insere um número entre 1 e 50,
    e o programa verifica se ele acertou o número gerado aleatoriamente.

    O jogo continua até que o usuário digite "sair".
    """

    while True:
        # Solicita a entrada do usuário
        jogador = input("\nEscolha um número entre 1 e 50 ou digite sair para encerrar o jogo:\n").strip()

        # Verifica se o usuário deseja sair do jogo
        if jogador.lower() == "sair":
            print("\nJogo encerrado!")
            break

        # Verifica se a entrada é um número válido
        if not jogador.isdigit():
            print("\nEntrada inválida! Digite um número inteiro entre 1 e 50.")
            continue

        # Converte a entrada para inteiro
        jogador = int(jogador)

        # Verifica se o número está dentro do intervalo permitido
        if jogador < 1 or jogador > 50:
            print("\nNúmero inválido! Escolha um número entre 1 e 50.")
            continue

        # Gera um número aleatório entre 1 e 50
        random_number = random.randint(1, 50)

        # Verifica se o jogador acertou
        if jogador == random_number:
            print(f"\nParabéns! Você acertou!\nSeu número: {jogador}\nNúmero gerado: {random_number}")
        else:
            print(f"\nVocê errou!\nSeu número: {jogador}\nNúmero gerado: {random_number}")

# Executa o jogo ao rodar o script
if __name__ == "__main__":
    jogo_adivinhacao()
