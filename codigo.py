# Passo a Paso do projeto
# Passo 1: Entrar no sistema da empresa
    # https://dlp.hashtagtreinamentos.com/python/intensivao/login
# pip install pyautogui
import pyautogui
import time

pyautogui.PAUSE = 0.5
# pyautogui.click -> clicar em algum lugar da tela
# pyautogui.write -> escrever um texto
# pyautogui.press -> pressiona 1 tecla do teclado

# pyautogui.hotkey("ctrl", "v")

# abrir o navegador (chrome)
pyautogui.press("win")
pyautogui.write("chrome")
pyautogui.press("enter")

link = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"
pyautogui.write(link)
pyautogui.press("enter")

# dar uma pausa um pouco maior (3 segundos)
time.sleep(5)

# Passo 2: Fazer login
pyautogui.click(x=751, y=511)  # valores de x e y vão depender da resolução da sua tela
pyautogui.write("fjss0504@gmail.com")

# escreve a senha
pyautogui.press("tab")
pyautogui.write("Fjss1989")

# clicar no botão logar
pyautogui.click(x=945, y=721) # valores de x e y vão depender da resolução da sua tela
time.sleep(3)
# Passo 3: Importar a base de dados
# pip install pandas numpy openpyxl
import pandas
tabela = pandas.read_csv("produtos.csv")  # tabula para ler arquivos pdf

# Passo 4: Cadastrar 1 produto
# para cada linha da minha tabela
for linha in tabela.index:

    # clicar no 1o produto
    pyautogui.click(x=664, y=366)  # valores de x e y vão depender da resolução da sua tela

    # codigo do produto
    codigo = tabela.loc[linha, "codigo"]
    pyautogui.write(codigo)
    pyautogui.press("tab")

    # marca
    pyautogui.write(tabela.loc[linha, "marca"])
    pyautogui.press("tab")

    # tipo
    pyautogui.write(tabela.loc[linha, "tipo"])
    pyautogui.press("tab")

    # categoria
    pyautogui.write(str(tabela.loc[linha, "categoria"]))
    pyautogui.press("tab")

    # preço
    pyautogui.write(str(tabela.loc[linha, "preco_unitario"]))
    pyautogui.press("tab")

    # custo
    pyautogui.write(str(tabela.loc[linha, "custo"]))
    pyautogui.press("tab")

    # obs
    obs = tabela.loc[linha, "obs"]
    if not pandas.isna(obs):
        pyautogui.write(obs)
    pyautogui.press("tab")

    # enviar
    pyautogui.press("enter")
    pyautogui.scroll(5000)