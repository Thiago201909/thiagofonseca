"""
Modulo: Informções Biograficas
Autor: Thiago Fonseca
Data: 05/04/2025

Descrição:
Este programa recolhe informações fornecidas pelo usuário.
E retorna em informações biograficas

Regras:
1. O usuário deve inserir os dados solicitados.
2. O programa retorna invalido caso o usuário não informa a quantdade minina de palavras.
3. Não pode usar caracteres especias.

Dependências:
- Python 3.8.18 (módulo `sys` e `datetime` embutido
"""
import sys
from datetime import datetime

# Definir os caracteres especiais não permitidos
SPECIAL_CHARS = "!@#$%^&*()'-_+="

# Função para validar se a entrada contém caracteres especiais
def validar_entrada(entrada, tipo):
    if any(char in entrada for char in SPECIAL_CHARS):
        print(f'Erro: {tipo} inválido! Não pode conter caracteres especiais: {SPECIAL_CHARS}')
        return False
    return True

# Função para validar a data de nascimento
def validar_data_nascimento(data_nasc):
    try:
        datetime.strptime(data_nasc, "%d/%m/%Y")
        return True
    except ValueError:
        print("Erro: Data de nascimento inválida! Use o formato DD/MM/AAAA.")
        return False

# Função para validar o tamanho mínimo de uma entrada
def validar_tamanho(entrada, minimo, tipo):
    if len(entrada) < minimo:
        print(f'Erro: {tipo} deve ter pelo menos {minimo} letras.')
        return False
    return True

# Coleta e validação dos dados
nome = input('Digite seu nome:\n').strip()
while not validar_entrada(nome, 'Nome'):
    nome = input('Digite seu nome novamente:\n').strip()

data_nasc = input('Digite sua data de nascimento (DD/MM/AAAA):\n').strip()
while not validar_data_nascimento(data_nasc):
    data_nasc = input('Digite sua data de nascimento novamente (DD/MM/AAAA):\n').strip()

endere = input('Digite seu endereço:\n').strip()
while not (validar_entrada(endere, 'Endereço') and validar_tamanho(endere, 5, 'Endereço')):
    endere = input('Digite seu endereço novamente (mínimo 5 letras):\n').strip()

objet = input('Digite seu objetivo:\n').strip()
while not (validar_entrada(objet, 'Objetivo') and validar_tamanho(objet, 10, 'Objetivo')):
    objet = input('Digite seu objetivo novamente (mínimo 10 letras):\n').strip()

# Exibe as informações coletadas
print("\nInformações cadastradas:")
print(f'Nome: {nome}')
print(f'Data de nascimento: {data_nasc}')
print(f'Endereço: {endere}')
print(f'Objetivo: {objet}')