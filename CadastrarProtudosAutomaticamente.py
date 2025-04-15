# pyautogui .... biblioteca que faz automações em python
import pyautogui
import time
# payautogui.click ... clica em algum lugar
# payautogui.press .... apertar 1 tecla
# payautogui.write .... escreve um texto
# payautogui.hotkey .... combinação de teclas (atalho)

pyautogui.PAUSE = 0.5    
   #função  para dar um intervalo de tempo

# Passo 1: Link da empresa : https://dlp.hashtagtreinamentos.com/python/intensivao/login

#Abri Google chrome
pyautogui.press('win')
pyautogui.write('chrome')
pyautogui.press('enter')

#Abrir site
pyautogui.write ('https://dlp.hashtagtreinamentos.com/python/intensivao/login')
pyautogui.press('enter')

#Loop de 3 segundo para carregamento do site
time.sleep(3)

# Passo 2: fazer login

#Fazer login
pyautogui.click(x=634, y=475)
pyautogui.write('thiago@gmail.com')

#Escrever senha
pyautogui.press('tab')
pyautogui.write('Thiagosenhaforte')
#Botão logar
pyautogui.press('tab')     
pyautogui.press('enter')

# Passo 3: Importar banco de dados
import pandas as pd

tabela = pd.read_csv('produtos.csv')

print(tabela)

# Passo 4: Cadastrar 1 protudo
for linha in tabela.index: #para cada linha da minha tabela
   pyautogui.click(x=598, y=331)

   codigo = tabela.loc[linha,  "codigo"] # .loc Sintaxe para localizar 
   pyautogui.write(codigo)
   
   pyautogui.press('tab')  
   marca = tabela.loc[linha,  "marca"]
   pyautogui.write(marca)
   
   pyautogui.press('tab') 
   tipo = tabela.loc[linha,  "tipo"]
   pyautogui.write(tipo)
   
   pyautogui.press('tab') 
   categoria = str(tabela.loc[linha,  "categoria"]) #str função para tranformar em texto
   pyautogui.write(categoria)
   
   pyautogui.press('tab') 
   preco_unitario =str( tabela.loc[linha,  "preco_unitario"])
   pyautogui.write(preco_unitario)
   
   pyautogui.press('tab') 
   custo =str(tabela.loc[linha,  "custo"])
   pyautogui.write(custo)
   
   pyautogui.press('tab') 
   obs = str(tabela.loc[linha,  "obs"])

   if obs != "nan":
       pyautogui.write(obs)
   
   pyautogui.press('tab') 
   pyautogui.press("enter")

      #Função para rolar a tela número positivo pra cima número negativo para baixo...Obs:Para subir tudo por um número grande ex:10.000,7.000
   pyautogui.scroll(10000) 
# Passo 5: Repitir para todos os produtos
