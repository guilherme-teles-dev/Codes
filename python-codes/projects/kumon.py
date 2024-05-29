import tkinter as tk

def calcular_soma(): #Aqui foi criado uma função capaz de somar dois números.
    try:
        num1 = float(entrada_num1.get())
        num2 = float(entrada_num2.get())
        resultado = num1 + num2
        label_resultado.config(text=f"Resultado: {resultado}")
    except ValueError:
        label_resultado.config(text="Erro: Insira apenas números válidos")

# Cria uma janela
janela = tk.Tk()
janela.title("Calculadora de Soma")

# Cria campos de entrada
entrada_num1 = tk.Entry(janela)
entrada_num1.pack(pady=5)

entrada_num2 = tk.Entry(janela)
entrada_num2.pack(pady=5)

# Cria um botão para calcular a soma
botao_calcular = tk.Button(janela, text="Calcular Soma", command=calcular_soma)
botao_calcular.pack(pady=5)

# Cria um rótulo para exibir o resultado
label_resultado = tk.Label(janela, text="")
label_resultado.pack(pady=5)

# Inicia o loop principal da interface gráfica
janela.mainloop()

