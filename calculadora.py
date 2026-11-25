import tkinter as tk

# variáveis
nextClear = False
fontVisor = ("Arial", 18)
fontBotao = ("Arial", 16)
calc = ""
clearBeforeType = True

janela = tk.Tk()
janela.title("Calculadora")

for coluna in range(4):
    janela.columnconfigure(coluna, weight=1)
    
def limpar():
    visor.delete(0, tk.END)
    
def deletar():
    textoVisor = visor.get()
    visor.delete(len(textoVisor) - 1, tk.END)

def digitar(caracter):
    textoVisor = visor.get()
    opChars = ["+", "-", "*", "/"]
    if caracter == "." and caracter in textoVisor:
        return
    if caracter in opChars:
        if  textoVisor == "":
            return
        global calc
        calc += textoVisor + str(caracter)
        limpar()
        return
    visor.insert(tk.END, caracter)
    
def calcular():
    global calc
    textoVisor = visor.get()
    calc += textoVisor
    resultado = ""
    limpar()
    try:
        resultado = eval(calc)
    except:
        resultado = "Erro: Expressão incorreta"
    visor.insert(tk.END, resultado)
    calc = ""

visor = tk.Entry(janela, width=20, justify="right", font=fontVisor)
visor.grid(row=0, column=0, columnspan=4, padx=5, pady=5, sticky="ew", ipadx=50, ipady=4)

botao_c = tk.Button(janela, text="C", width=5, font=fontBotao, command=limpar)
botao_c.grid(row=1, column=0, padx=3, pady=3, sticky="nsew")

botao_del = tk.Button(janela, text="del", width=5, font=fontBotao, command=deletar)
botao_del.grid(row=1, column=1, padx=3, pady=3, sticky="nsew")

botao_div = tk.Button(janela, text="÷", width=5, font=fontBotao, command=lambda: digitar("/"))
botao_div.grid(row=1, column=2, padx=3, pady=3, sticky="nsew")

botao_mult = tk.Button(janela, text="×", width=5, font=fontBotao, command=lambda: digitar("*"))
botao_mult.grid(row=1, column=3, padx=3, pady=3, sticky="nsew")

botao_7 = tk.Button(janela, text="7", width=5, font=fontBotao, command=lambda: digitar("7"))
botao_7.grid(row=2, column=0, padx=3, pady=3, sticky="nsew")

botao_8 = tk.Button(janela, text="8", width=5, font=fontBotao, command=lambda: digitar("8"))
botao_8.grid(row=2, column=1, padx=3, pady=3, sticky="nsew")

botao_9 = tk.Button(janela, text="9", width=5, font=fontBotao, command=lambda: digitar("9"))
botao_9.grid(row=2, column=2, padx=3, pady=3, sticky="nsew")

botao_sub = tk.Button(janela, text="-", width=5, font=fontBotao, command=lambda: digitar("-"))
botao_sub.grid(row=2, column=3, padx=3, pady=3, sticky="nsew")

botao_4 = tk.Button(janela, text="4", width=5, font=fontBotao, command=lambda: digitar("4"))
botao_4.grid(row=3, column=0, padx=3, pady=3, sticky="nsew")

botao_5 = tk.Button(janela, text="5", width=5, font=fontBotao, command=lambda: digitar("5"))
botao_5.grid(row=3, column=1, padx=3, pady=3, sticky="nsew")

botao_6 = tk.Button(janela, text="6", width=5, font=fontBotao, command=lambda: digitar("6"))
botao_6.grid(row=3, column=2, padx=3, pady=3, sticky="nsew")

botao_add = tk.Button(janela, text="+", width=5, font=fontBotao, command=lambda: digitar("+"))
botao_add.grid(row=3, column=3, padx=3, pady=3, sticky="nsew")

botao_1 = tk.Button(janela, text="1", width=5, font=fontBotao, command=lambda: digitar("1"))
botao_1.grid(row=4, column=0, padx=3, pady=3, sticky="nsew")

botao_2 = tk.Button(janela, text="2", width=5, font=fontBotao, command=lambda: digitar("2"))
botao_2.grid(row=4, column=1, padx=3, pady=3, sticky="nsew")

botao_3 = tk.Button(janela, text="3", width=5, font=fontBotao, command=lambda: digitar("3"))
botao_3.grid(row=4, column=2, padx=3, pady=3, sticky="nsew")

botao_equal = tk.Button(janela, text="=", width=5, height=2, font=fontBotao, command=calcular)
botao_equal.grid(row=4, rowspan=2, column=3, padx=3, pady=3, sticky="nsew")

botao_0 = tk.Button(janela, text="0", width=10, font=fontBotao, command=lambda: digitar("0"))
botao_0.grid(row=5, column=0, columnspan=2, padx=3, pady=3, sticky="nsew")

botao_virg = tk.Button(janela, text=".", width=5, font=fontBotao, command=lambda: digitar("."))
botao_virg.grid(row=5, column=2, padx=3, pady=3, sticky="nsew")

janela.mainloop()