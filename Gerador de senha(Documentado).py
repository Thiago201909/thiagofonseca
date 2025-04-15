"""
Módulo: Gerador de senhas
Autor: [Thiago Fonseca]
Data: [05/04/2025]

Descrição:
Este programa implementa um programa simples onde o usuário insere alguns dados entre letras e números.
O programa retorna três sugestões.

Regras:
1. O usuário deve inserir uma senha com letras e números.
2. O programa embaralha esses dados e gera três sugestões.

Dependências:
- Python 3.8.18 (módulo `random` e `string` embutido)
"""
import random
import string

def gerar_senha(base):
    """
    Gera uma senha mais segura a partir de uma senha base fornecida pelo usuário.

    Parâmetros:
    - base (str): A senha base inserida pelo usuário, sem espaços.

    Retorno:
    - str: Uma nova senha contendo os caracteres da base original, além de um caractere especial,
           um número e uma letra maiúscula, todos embaralhados para garantir aleatoriedade.
    """
    # Define os conjuntos de caracteres adicionais que serão incluídos na senha
    caracteres_especiais = "!@#$%^&*()-_=+<>?"
    numeros = string.digits
    letras_maiusculas = string.ascii_uppercase

    # Converte a senha base em uma lista de caracteres
    senha = list(base)

    # Adiciona um caractere aleatório de cada tipo para aumentar a complexidade
    senha.append(random.choice(caracteres_especiais))
    senha.append(random.choice(numeros))
    senha.append(random.choice(letras_maiusculas))

    # Embaralha a ordem dos caracteres para evitar padrões previsíveis
    random.shuffle(senha)

    # Retorna a nova senha como uma string
    return "".join(senha)

# Entrada do usuário
# remove todos os espaços em branco (inclusive no meio da senha)
senha_base = input("Digite sua senha base: ").replace(" ", "")

# Gera uma lista com três sugestões de senhas mais seguras
sugestoes = [gerar_senha(senha_base) for _ in range(3)]

# Exibe as sugestões ao usuário
print("\nSugestões de senha mais seguras:")
for i, senha in enumerate(sugestoes, 1):
    print(f"{i}. {senha}")
