import random as r
import tkinter as tk
from tkinter import ttk

def gerar_atributos():
    # Declaração de variáveis
    atributos = {}

    # Entrada de dados
    nome = entry_nome.get()
    nome = nome.strip().lower()

    resultado_text.delete(1.0, tk.END)  # Limpa o texto anterior

    if nome == 'phony':
        resultado_text.insert(tk.END, 'Poxa vida Phonyzinho, todos os seus atributos foram 1 :(')
    elif nome == 'mr.yellow':
        resultado_text.insert(tk.END, 'Você tira o máximo em todos os atributos mas... Era só ilusão (Bryan ganha 20 de força)')
    elif nome == 'picles':
        resultado_text.insert(tk.END, 'Eu nem preciso zoar, sei que você vai tirar número baixo em todos os dados, toma 1 em tudo logo de uma vez.')
    else:
        # Processamento
        for i in range(6):
            nDado = []

            for j in range(4):
                dados = r.randint(1, 6)
                nDado.append(dados)
                    
            menor = min(nDado)
            nDado.remove(menor)
            soma = '0' + str(i+1) + '_Valor total: ' + str(sum(nDado))
            atributos[soma] = nDado

        resultado_text.insert(tk.END, f'Resultado dos dados do(a) {nome.capitalize()}:\n')
        for chave, valor in atributos.items():
            resultado_text.insert(tk.END, f'{chave} {valor}\n')

# Criar janela
janela = tk.Tk()
janela.title('Gerador de Atributos')
janela.geometry('600x400')  # Tamanho da janela

# Criar rótulo e entrada de texto para o nome
label_nome = tk.Label(janela, text='Digite o nome do personagem:', font=("Helvetica", 14))
label_nome.pack(pady=10)
entry_nome = tk.Entry(janela, font=("Helvetica", 12))
entry_nome.pack()

# Botão para gerar atributos
btn_gerar = tk.Button(janela, text='Gerar Atributos', command=gerar_atributos, font=("Helvetica", 12))
btn_gerar.pack(pady=10)

# Caixa de texto para exibir o resultado
resultado_text = tk.Text(janela, height=10, width=40, font=("Helvetica", 12))
resultado_text.pack(padx=20, pady=10)

janela.mainloop()
