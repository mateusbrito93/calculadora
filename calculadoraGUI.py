import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk  # Importar a biblioteca Pillow para manipulação de imagens
import os
from PIL import Image, ImageTk

# Função para calcular o salário e vales juntos
def calcular_tudo():
    try:
        salario = float(entry_salario.get())
        gratificacao = float(entry_gratificacao.get())
        inss_percentual = float(entry_inss.get()) / 100
        vale_transporte = float(entry_vale_transporte.get())
        vale_alimentacao = float(entry_vale_alimentacao.get())
        dias_trabalhados = int(entry_dias_trabalhados.get())

        # Primeiro cálculo: (Salário + Gratificação) - INSS
        total1 = (salario + gratificacao) - ((salario + gratificacao) * inss_percentual)

        # Segundo cálculo: Total1 + (Dias Trabalhados * Vale Transporte/Alimentação)
        total2 = total1 + dias_trabalhados * (vale_transporte + vale_alimentacao)

        label_resultado.config(text=f'Salário Total: R$ {total2:.2f}')
    except ValueError:
        messagebox.showerror("Erro", "Por favor, insira valores válidos.")

# Função para calcular apenas os vales
def calcular_vales():
    try:
        vale_transporte = float(entry_vale_transporte.get())
        vale_alimentacao = float(entry_vale_alimentacao.get())
        dias_trabalhados = int(entry_dias_trabalhados.get())

        # Cálculo: (vale_transporte + vale_alimentacao) * dias_trabalhados
        total1 = (vale_transporte + vale_alimentacao) * dias_trabalhados

        label_resultado.config(text=f'Total Vales: R$ {total1:.2f}')
    except ValueError:
        messagebox.showerror("Erro", "Por favor, insira valores válidos.")

# Função para calcular o salário
def calcular_salario():
    try:
        salario = float(entry_salario.get())
        gratificacao = float(entry_gratificacao.get())
        inss_percentual = float(entry_inss.get()) / 100

        # Cálculo: (Salário + Gratificação) - INSS
        total1 = (salario + gratificacao) - ((salario + gratificacao) * inss_percentual)

        label_resultado.config(text=f'Salário: R$ {total1:.2f}')
    except ValueError:
        messagebox.showerror("Erro", "Por favor, insira valores válidos.")

# Criar a janela principal
root = tk.Tk()
root.title("Calculadora de Salário")

# Definir o ícone da janela usando o caminho absoluto
icon_path = os.path.join(os.path.dirname(__file__), 'money.ico')
root.iconbitmap(icon_path)

# Título chamativo
#title_label = tk.Label(root, text="DSNS", font=("Arial", 24, "bold"), fg="blue")
#title_label.grid(row=0, column=0, columnspan=3, pady=10)

# Definir o caminho absoluto para o logo
logo_path = os.path.join(os.path.dirname(__file__), 'logo.png')

# Carregar a imagem redimensionada
image = Image.open(logo_path)
image = image.resize((100, 100))  # Redimensione conforme necessário
logo = ImageTk.PhotoImage(image)
logo_label = tk.Label(root, image=logo)
logo_label.grid(row=1, column=0, columnspan=3)

# Salário
tk.Label(root, text="Salário:").grid(row=2, column=0, padx=10, pady=5, sticky='e')
entry_salario = tk.Entry(root)
entry_salario.insert(0, "2006.48")
entry_salario.grid(row=2, column=1)

# Gratificação
tk.Label(root, text="Gratificação:").grid(row=3, column=0, padx=10, pady=5, sticky='e')
entry_gratificacao = tk.Entry(root)
entry_gratificacao.insert(0, "402.05")
entry_gratificacao.grid(row=3, column=1)

# INSS (%)
tk.Label(root, text="INSS (%):").grid(row=4, column=0, padx=10, pady=5, sticky='e')
entry_inss = tk.Entry(root)
entry_inss.insert(0, "8.12")
entry_inss.grid(row=4, column=1)

# Vale Transporte
tk.Label(root, text="Vale Transporte (R$):").grid(row=5, column=0, padx=10, pady=5, sticky='e')
entry_vale_transporte = tk.Entry(root)
entry_vale_transporte.insert(0, "9.80")
entry_vale_transporte.grid(row=5, column=1)

# Vale Alimentação
tk.Label(root, text="Vale Alimentação (R$):").grid(row=6, column=0, padx=10, pady=5, sticky='e')
entry_vale_alimentacao = tk.Entry(root)
entry_vale_alimentacao.insert(0, "21.50")
entry_vale_alimentacao.grid(row=6, column=1)

# Dias Trabalhados
tk.Label(root, text="Dias Trabalhados:").grid(row=7, column=0, padx=10, pady=5, sticky='e')
entry_dias_trabalhados = tk.Entry(root)
entry_dias_trabalhados.grid(row=7, column=1)

# Botões para cálculo
btn_calcular_vales = tk.Button(root, text="Calcular Vales", command=calcular_vales)
btn_calcular_vales.grid(row=8, column=0, padx=10, pady=10)

btn_calcular_salario = tk.Button(root, text="Calcular Salário", command=calcular_salario)
btn_calcular_salario.grid(row=8, column=1, padx=10, pady=10)

btn_calcular_tudo = tk.Button(root, text="Calcular Tudo", command=calcular_tudo)
btn_calcular_tudo.grid(row=8, column=2, padx=10, pady=10)

# Label para mostrar o resultado
label_resultado = tk.Label(root, text="Resultado: R$ 0.00", font=('Arial', 14))
label_resultado.grid(row=9, column=0, columnspan=3, pady=20)

# Criar rodapé com o texto "Powered By Mateus Brito 2024"
footer_label = tk.Label(root, text="Powered By Mateus Brito 2024", font=("Arial", 8), fg="gray")
footer_label.grid(row=10, column=0, columnspan=3, pady=10, sticky='s')

# Executar a interface
root.mainloop()
