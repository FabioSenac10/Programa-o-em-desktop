import tkinter as tk

janela = tk.Tk()
janela.title("Calculadora")
janela.geometry("600x400")

def calculo():
    try:
        valor1 = float(entrada1.get())
        valor2 = float(entrada2.get())
        operacao = EntradaOperacao.get()

        if operacao == "+":
            calcular = valor1 + valor2
        elif operacao == "-":
            calcular = valor1 - valor2
        elif operacao == "*":
            calcular = valor1 * valor2
        elif operacao == "/":
            calcular = valor1 / valor2
        else:
            result.config(text="Operação inválida")
            return

        result.config(text=f"Resultado: {calcular}")

    except:
        result.config(text="Informe números válidos")

tk.Label(janela, text="Inserir Variável 1:").pack(pady=5)
entrada1 = tk.Entry(janela)
entrada1.pack()

tk.Label(janela, text="Informe a operação (+ - * /):").pack(pady=5)
EntradaOperacao = tk.Entry(janela)
EntradaOperacao.pack()

tk.Label(janela, text="Inserir Variável 2:").pack(pady=5)
entrada2 = tk.Entry(janela)
entrada2.pack()

result = tk.Label(janela, text="Resultado:")
result.pack(pady=10)

botao = tk.Button(janela, text="Calcular", command=calculo)
botao.pack(pady=10)

janela.mainloop()