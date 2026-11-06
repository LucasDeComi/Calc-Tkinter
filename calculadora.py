import tkinter as tk

# variáveis
nextClear = False
fontVisor = 24

janela = tk.Tk()
janela.title("Calculadora")
    
def limpar():
    visor.delete(0, tk.END)
    
def deletar():
    textoVisor = visor.get()
    visor.delete(len(textoVisor) - 1, tk.END)

def digitar(caracter):
    textoVisor = visor.get()
    lastChar = ""
    lockChars = ["+", "-", "*", "/", "."]
    if textoVisor != "":
        lastChar = textoVisor[-1]
    if not lastChar in lockChars and not caracter in lockChars:
        visor.insert(tk.END, caracter)
    
def calcular():
    textoVisor = visor.get()
    resultado = ""
    limpar()
    try:
        resultado = eval(textoVisor)
    except:
        resultado = "Erro: Expressão incorreta"
    visor.insert(tk.END, resultado)

visor = tk.Entry(janela, width=24, justify="right", font=fontVisor)
visor.grid(row=0, column=0, columnspan=4, padx=5, pady=5)

botao_c = tk.Button(janela, text="C", width=6, command=limpar)
botao_c.grid(row=1, column=0, padx=3, pady=3)

botao_del = tk.Button(janela, text="del", width=6, command=deletar)
botao_del.grid(row=1, column=1, padx=3, pady=3)

botao_div = tk.Button(janela, text="÷", width=6, command=lambda: digitar("/"))
botao_div.grid(row=1, column=2, padx=3, pady=3)

botao_mult = tk.Button(janela, text="×", width=6, command=lambda: digitar("*"))
botao_mult.grid(row=1, column=3, padx=3, pady=3)

botao_7 = tk.Button(janela, text="7", width=6, command=lambda: digitar("7"))
botao_7.grid(row=2, column=0, padx=3, pady=3)

botao_8 = tk.Button(janela, text="8", width=6, command=lambda: digitar("8"))
botao_8.grid(row=2, column=1, padx=3, pady=3)

botao_9 = tk.Button(janela, text="9", width=6, command=lambda: digitar("9"))
botao_9.grid(row=2, column=2, padx=3, pady=3)

botao_sub = tk.Button(janela, text="-", width=6, command=lambda: digitar("-"))
botao_sub.grid(row=2, column=3, padx=3, pady=3)

botao_4 = tk.Button(janela, text="4", width=6, command=lambda: digitar("4"))
botao_4.grid(row=3, column=0, padx=3, pady=3)

botao_5 = tk.Button(janela, text="5", width=6, command=lambda: digitar("5"))
botao_5.grid(row=3, column=1, padx=3, pady=3)

botao_6 = tk.Button(janela, text="6", width=6, command=lambda: digitar("6"))
botao_6.grid(row=3, column=2, padx=3, pady=3)

botao_add = tk.Button(janela, text="+", width=6, command=lambda: digitar("+"))
botao_add.grid(row=3, column=3, padx=3, pady=3)

botao_1 = tk.Button(janela, text="1", width=6, command=lambda: digitar("1"))
botao_1.grid(row=4, column=0, padx=3, pady=3)

botao_2 = tk.Button(janela, text="2", width=6, command=lambda: digitar("2"))
botao_2.grid(row=4, column=1, padx=3, pady=3)

botao_3 = tk.Button(janela, text="3", width=6, command=lambda: digitar("3"))
botao_3.grid(row=4, column=2, padx=3, pady=3)

botao_equal = tk.Button(janela, text="=", width=6, height=3, command=calcular)
botao_equal.grid(row=4, rowspan=2, column=3, padx=3, pady=3)

botao_0 = tk.Button(janela, text="0", width=15, command=lambda: digitar("0"))
botao_0.grid(row=5, column=0, columnspan=2, padx=3, pady=3)

botao_virg = tk.Button(janela, text=".", width=6, command=lambda: digitar("."))
botao_virg.grid(row=5, column=2, padx=3, pady=3)

janela.mainloop()