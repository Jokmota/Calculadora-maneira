# puxando tkinter pro script
from tkinter import *
from tkinter import ttk

# Definindo as cores
cor1_roxa = '#9842f5'
cor2_cinza_escuro = '#14171c'
cor3_cinza = '#9c9c9c'

# entrada de valores
def entrar_valores(event):
    global todos_valores
    todos_valores += str(event)
    valor_texto.set(todos_valores)

# cálculo
def calcular():
    global todos_valores
    try:
        resultado = eval(todos_valores)
        valor_texto.set(str(resultado))
        todos_valores = str(resultado)
    except Exception as e:
        valor_texto.set("Erro")
        todos_valores = ''

# limpar a tela
def limpar_tela():
    global todos_valores
    todos_valores = ''
    valor_texto.set('')

# botões formatados
def criar_botao(frame, texto, row, col, rowspan=1, colspan=1, command=None, cor_fundo=cor1_roxa):
    botao = Button(frame, text=texto, bg=cor_fundo, font=('Ivy', 10, 'bold'), relief=RAISED, overrelief=RIDGE, command=command)
    botao.grid(row=row, column=col, rowspan=rowspan, columnspan=colspan, sticky=NSEW)
    return botao

# Inicializando a janela
janela = Tk()
janela.title('Calculadora')
janela.geometry('300x400')
janela.config(bg=cor1_roxa)

# Configurando grid 
janela.grid_rowconfigure(0, weight=1)
janela.grid_rowconfigure(1, weight=4)
janela.grid_columnconfigure(0, weight=1)

# Frame da tela
frame_tela = Frame(janela, bg=cor2_cinza_escuro)
frame_tela.grid(row=0, column=0, sticky=NSEW)

# Frame do corpo
frame_corpo = Frame(janela, bg=cor1_roxa)
frame_corpo.grid(row=1, column=0, sticky=NSEW)

# redimensionamento dos frames
for i in range(5): 
    frame_corpo.grid_rowconfigure(i, weight=1)
for i in range(4):
    frame_corpo.grid_columnconfigure(i, weight=1)

# Variável global para armazenar os valores
todos_valores = ''

# Criando label para exibir os valores
valor_texto = StringVar()
app_label = Label(frame_tela, textvariable=valor_texto, width=16, height=2, padx=7, relief=FLAT, anchor='e', justify=RIGHT, font=('Ivy 18'), bg=cor2_cinza_escuro, fg=cor1_roxa)
app_label.pack(expand=True, fill='both')

# Lista de botões e configs
botoes = [
    ('C', 0, 0, 1, 1, limpar_tela, cor1_roxa), 
    ('%', 0, 1, 1, 1, lambda: entrar_valores('%'), cor1_roxa),
    ('/', 0, 2, 1, 1, lambda: entrar_valores('/'), cor1_roxa),
    ('*', 0, 3, 1, 1, lambda: entrar_valores('*'), cor1_roxa),
    ('7', 1, 0, 1, 1, lambda: entrar_valores('7'), cor3_cinza),
    ('8', 1, 1, 1, 1, lambda: entrar_valores('8'), cor3_cinza),
    ('9', 1, 2, 1, 1, lambda: entrar_valores('9'), cor3_cinza),
    ('-', 1, 3, 1, 1, lambda: entrar_valores('-'), cor1_roxa),
    ('4', 2, 0, 1, 1, lambda: entrar_valores('4'), cor3_cinza),
    ('5', 2, 1, 1, 1, lambda: entrar_valores('5'), cor3_cinza),
    ('6', 2, 2, 1, 1, lambda: entrar_valores('6'), cor3_cinza),
    ('+', 2, 3, 1, 1, lambda: entrar_valores('+'), cor1_roxa),
    ('1', 3, 0, 1, 1, lambda: entrar_valores('1'), cor3_cinza),
    ('2', 3, 1, 1, 1, lambda: entrar_valores('2'), cor3_cinza),
    ('3', 3, 2, 1, 1, lambda: entrar_valores('3'), cor3_cinza),
    ('=', 3, 3, 2, 1, calcular, cor1_roxa),
    ('0', 4, 0, 1, 2, lambda: entrar_valores('0'), cor3_cinza),
    ('.', 4, 2, 1, 1, lambda: entrar_valores('.'), cor3_cinza)
]

# Botões com a formatação
for botao in botoes:
    texto, row, col, rowspan, colspan, comando, cor_fundo = botao + (None,) * (7 - len(botao))  
    if comando is None:
        comando = lambda t=texto: entrar_valores(t)
    criar_botao(frame_corpo, texto, row, col, rowspan, colspan, comando, cor_fundo)

# Iniciando o loop principal da interface
janela.mainloop()
