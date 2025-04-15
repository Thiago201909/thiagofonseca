"""
Módulo: Calculo da idade canina
Autor: [Thiago Fonseca]
Data: [05/04/2025]

Descrição:
Este programa implementa um calculo sobre a idade humana canina
O usuário informa o ano ou o ano e mês do cão.
O programa retorna o ano e mês do cão em idade humana.

Regras:
1. O usuário deve inserir a idade do cão.
2. O programa faz o calculo e retorna a idade humana. 

Dependências:
- Python 3.x (módulo `random` embutido)
"""
import math

#Entrada dos dados em float para evitar letras
id_dog = float(input('Digite a idade do seu doguinho (ex:0 ou 0.0):'))

#Verificação para obter uma número positivo
if id_dog <= 0:
    print("A idade deve ser um número positivo.")
else:
    anos = int(id_dog)  # Parte inteira da idade
    meses = math.floor((id_dog - anos) * 11)  # Calcula os meses evitando arredondamentos inesperados

    idade_humana = 16 * math.log(id_dog) + 31  # Cálculo da idade humana

    print(f'\n{anos} anos e {meses} meses caninos equivalem a {idade_humana:.1f} anos humanos.')