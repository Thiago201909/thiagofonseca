"""
Módulo: jogo_pedra_papel_tesoura.py
Descrição: Implementação de um jogo simples de Pedra, Papel e Tesoura em Python.
Autor: Thiago Fonseca Azeredo
Data: 07/04/2025
"""

import random

def obter_escolha_usuario():
    """
    Solicita ao usuário uma escolha entre 'pedra', 'papel', 'tesoura' ou 'sair'.
    
    Retorna:
        str: A escolha validada do usuário.
    """
    opcoes = ["pedra", "papel", "tesoura", "sair"]
    escolha = input("Escolha pedra, papel, tesoura ou sair para encerrar:\n ").strip().lower()
    
    # Loop de validação até o usuário inserir uma opção válida
    while escolha not in opcoes:
        print("Opção inválida! Tente novamente.")
        escolha = input("Escolha pedra, papel, tesoura ou 'sair' para encerrar:\n ").strip().lower()
    
    return escolha

def obter_escolha_computador():
    """
    Gera aleatoriamente a escolha do computador entre 'pedra', 'papel' e 'tesoura'.
    
    Retorna:
        str: A escolha do computador.
    """
    return random.choice(["pedra", "papel", "tesoura"])

def determinar_vencedor(jogador, computador):
    """
    Determina o vencedor com base nas escolhas do jogador e do computador.
    
    Args:
        jogador (str): A escolha do jogador.
        computador (str): A escolha do computador.
        
    Retorna:
        str: Resultado da rodada indicando o vencedor.
    """
    # Se as escolhas forem iguais, há empate
    if jogador == computador:
        return "Empate!"
    
    # Regras do jogo: cada chave vence o valor correspondente
    regras = {
        "pedra": "tesoura",   # pedra vence tesoura
        "papel": "pedra",     # papel vence pedra
        "tesoura": "papel"    # tesoura vence papel
    }
    
    # Verifica se o jogador venceu com base nas regras
    if regras[jogador] == computador:
        return "Você venceu!"
    else:
        return "Computador venceu!"

def jogar():
    """
    Controla o fluxo principal do jogo, exibindo instruções,
    capturando entradas, exibindo resultados e encerrando quando solicitado.
    """
    print("Bem-vindo ao jogo Pedra, Papel e Tesoura!\n")
    
    # Loop principal do jogo
    while True:
        jogador = obter_escolha_usuario()
        
        if jogador == "sair":
            print("\nObrigado por jogar! Até a próxima.")
            break
        
        computador = obter_escolha_computador()
        
        print(f"\nVocê escolheu: {jogador}")
        print(f"Computador escolheu: {computador}")
        
        resultado = determinar_vencedor(jogador, computador)
        print("\n" + resultado + "\n")

# Inicia o jogo
jogar()
