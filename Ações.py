import pyautogui
import pyperclip
import webbrowser
import time
import yfinance

ticker = input("Digite o código da ação desejada: ")

dados = yfinance.Ticker(ticker).history(start="2020-01-01", end="2020-12-31")
fechamento = dados.Close

maxima = round(fechamento.max(), 2)
minima = round(fechamento.min(), 2)
valor_medio = round(fechamento.mean(), 2)

destinatario = "gabrielrangel.analytics@gmail.com"
assunto = "Análises do Projeto 2020"
mensagem = f"""
Prezado gestor, 

Seguem as análises solicitadas da Ação {ticker}:

Cotação máxima: {maxima}
Cotação mínima: {minima}
Valor médio: {valor_medio}

Qualquer dúvida, estou á disposição!

Atte.
"""

# abrir o navegador e ir para o gmail 
webbrowser.open("www.gmail.com")
time.sleep(3) 

# configurando uma pausa de 3 segundos
pyautogui.PAUSE = 3

#clicar no botão escrever 
pyautogui.click(x=151, y=176)

# digitar o email do destinatário e teclar TAB 
pyperclip.copy(destinatario)
pyautogui.hotkey("ctrl","v")
pyautogui.hotkey("tab")

# digitar o assunto do email 
pyperclip.copy(assunto)
pyautogui.hotkey("ctrl","v")
pyautogui.hotkey("tab")

# digitar a mensagem 
pyperclip.copy(mensagem)
pyautogui.hotkey("ctrl","v")

# clicar no botão enviar 
pyautogui.click(x=1325, y=1007)

# fechar o gmail 
pyautogui.hotkey("ctrl", "f4")

print("Email enviado com sucesso")