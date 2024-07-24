from tkinter import *
from tkinter import colorchooser
from tkinter import ttk

# Definindo as cores padrão
cores = {
    'bg_label': '#14171c',
    'fg_label': '#9842f5',
    'bg_botao_op': '#9842f5',
    'bg_botao_num': '#9c9c9c'
}

# Função para atualizar as cores
def atualizar_cores():
    app_label.config(bg=cores['bg_label'], fg=cores['fg_label'])
    for botao in botoes_botoes:
        if botao['text'] in {'+', '-', '*', '/', '=', 'C', '%'}:
            botao.config(bg=cores['bg_botao_op'])
        else:
            botao.config(bg=cores['bg_botao_num'])

# Função para abrir a janela de configuração
def abrir_configuracao():
    def selecionar_cor(cor, tipo):
        nova_cor = colorchooser.askcolor()[1]
        if nova_cor:
            cores[tipo] = nova_cor
            atualizar_cores()

    janela_configuracao = Toplevel(janela)
    janela_configuracao.title("Configurações")

    Label(janela_configuracao, text="Cor do Label").pack(pady=5)
    Button(janela_configuracao, text="Escolher cor", command=lambda: selecionar_cor('bg_label', 'bg_label')).pack(pady=5)
    Button(janela_configuracao, text="Escolher cor para o texto", command=lambda: selecionar_cor('fg_label', 'fg_label')).pack(pady=5)
    Button(janela_configuracao, text="Escolher cor dos botões de operação", command=lambda: selecionar_cor('bg_botao_op', 'bg_botao_op')).pack(pady=5)
    Button(janela_configuracao, text="Escolher cor dos botões de números", command=lambda: selecionar_cor('bg_botao_num', 'bg_botao_num')).pack(pady=5)

# Entrada de valores
def entrar_valores(event):
    global todos_valores
    todos_valores += str(event)
    valor_texto.set(todos_valores)

# Cálculo
def calcular():
    global todos_valores
    try:
        resultado = eval(todos_valores)
        valor_texto.set(str(resultado))
        todos_valores = str(resultado)
    except Exception:
        valor_texto.set("Erro")
        todos_valores = ''

# Limpar a tela
def limpar_tela():
    global todos_valores
    todos_valores = ''
    valor_texto.set('')

# Botões formatados
def criar_botao(frame, texto, row, col, rowspan=1, colspan=1, command=None, cor_fundo=cores['bg_botao_op']):
    botao = Button(frame, text=texto, bg=cor_fundo, font=('Ivy', 10, 'bold'), relief=RAISED, overrelief=RIDGE, command=command)
    botao.grid(row=row, column=col, rowspan=rowspan, columnspan=colspan, sticky=NSEW)
    return botao

# Inicializando a janela
janela = Tk()
janela.title('Calculadora')
janela.geometry('300x400')
janela.config(bg=cores['bg_botao_op'])

# Configurando grid 
janela.grid_rowconfigure(0, weight=1)
janela.grid_rowconfigure(1, weight=4)
janela.grid_columnconfigure(0, weight=1)

# Frame da tela
frame_tela = Frame(janela, bg=cores['bg_label'])
frame_tela.grid(row=0, column=0, sticky=NSEW)

# Frame do corpo
frame_corpo = Frame(janela, bg=cores['bg_botao_op'])
frame_corpo.grid(row=1, column=0, sticky=NSEW)

# Redimensionamento dos frames
for i in range(5): 
    frame_corpo.grid_rowconfigure(i, weight=1)
for i in range(4):
    frame_corpo.grid_columnconfigure(i, weight=1)

# Variável global para armazenar os valores
todos_valores = ''

# Criando label para exibir os valores
valor_texto = StringVar()
app_label = Label(frame_tela, textvariable=valor_texto, width=16, height=2, padx=7, relief=FLAT, anchor='e', justify=RIGHT, font=('Ivy', 18), bg=cores['bg_label'], fg=cores['fg_label'])
app_label.pack(expand=True, fill='both')

# Lista de botões e configs
botoes = [
    ('C', 0, 0, 1, 1, limpar_tela, cores['bg_botao_op']),
    ('%', 0, 1, 1, 1, lambda: entrar_valores('%'), cores['bg_botao_op']),
    ('/', 0, 2, 1, 1, lambda: entrar_valores('/'), cores['bg_botao_op']),
    ('*', 0, 3, 1, 1, lambda: entrar_valores('*'), cores['bg_botao_op']),
    ('7', 1, 0, 1, 1, lambda: entrar_valores('7'), cores['bg_botao_num']),
    ('8', 1, 1, 1, 1, lambda: entrar_valores('8'), cores['bg_botao_num']),
    ('9', 1, 2, 1, 1, lambda: entrar_valores('9'), cores['bg_botao_num']),
    ('-', 1, 3, 1, 1, lambda: entrar_valores('-'), cores['bg_botao_op']),
    ('4', 2, 0, 1, 1, lambda: entrar_valores('4'), cores['bg_botao_num']),
    ('5', 2, 1, 1, 1, lambda: entrar_valores('5'), cores['bg_botao_num']),
    ('6', 2, 2, 1, 1, lambda: entrar_valores('6'), cores['bg_botao_num']),
    ('+', 2, 3, 1, 1, lambda: entrar_valores('+'), cores['bg_botao_op']),
    ('1', 3, 0, 1, 1, lambda: entrar_valores('1'), cores['bg_botao_num']),
    ('2', 3, 1, 1, 1, lambda: entrar_valores('2'), cores['bg_botao_num']),
    ('3', 3, 2, 1, 1, lambda: entrar_valores('3'), cores['bg_botao_num']),
    ('=', 3, 3, 2, 1, calcular, cores['bg_botao_op']),
    ('0', 4, 0, 1, 2, lambda: entrar_valores('0'), cores['bg_botao_num']),
    ('.', 4, 2, 1, 1, lambda: entrar_valores('.'), cores['bg_botao_num'])
]

# Criando botões
botoes_botoes = []
for botao in botoes:
    texto, row, col, rowspan, colspan, comando, cor_fundo = botao + (None,) * (7 - len(botao))  
    if comando is None:
        comando = lambda t=texto: entrar_valores(t)
    b = criar_botao(frame_corpo, texto, row, col, rowspan, colspan, comando, cor_fundo)
    botoes_botoes.append(b)

# Adicionando botão de configuração
botao_configuracao = Button(janela, text="Configurações", command=abrir_configuracao, bg=cores['bg_botao_op'], font=('Ivy', 10, 'bold'), relief=RAISED, overrelief=RIDGE)
botao_configuracao.grid(row=2, column=0, sticky=NSEW, pady=10)

# Iniciando o loop principal da interface
janela.mainloop()
