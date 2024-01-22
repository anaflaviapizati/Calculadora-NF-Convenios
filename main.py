import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk


def verificar_numero_arquivo(numero):
    nome_arquivo = 'convenios.txt'

    try:
        with open(nome_arquivo, 'r', encoding='utf-8') as arquivo:
            for linha in arquivo:
                if linha.startswith(f"{numero} - "):
                    return True
    except FileNotFoundError:
        print(f"Arquivo '{nome_arquivo}' não encontrado.")
    except Exception as e:
        print(f"Ocorreu um erro: {e}")

    return False


def calcular_impostos():
    numero_usuario = entry_numero.get()

    if verificar_numero_arquivo(numero_usuario):
        valor = float(entry_valor.get())
        ir = round(valor * 0.015, 3)
        pis = round(valor * 0.065, 3)
        cofins = round(valor * 0.03, 3)
        clss = round(valor * 0.01, 3)

        resultado_text.set(f"IR: {ir} \n PIS: {pis} \n COFINS: {cofins} \n CLSS: {clss}")
    else:
        label_convenio.config(foreground="#ffff00", text=f"\nO convênio {numero_usuario} não está cadastrado!")


def buscar_convenio():
    numero_usuario = entry_numero.get()

    if verificar_numero_arquivo(numero_usuario):
        nome_convenio = obter_nome_convenio(numero_usuario)
        label_convenio.config(text=f"\nConvênio escolhido: {nome_convenio}", foreground="#90ee90")
    else:
        label_convenio.config(foreground="#ffff00", text=f"\nO convênio {numero_usuario} não está cadastrado!")


def obter_nome_convenio(numero):
    nome_arquivo = 'convenios.txt'

    try:
        with open(nome_arquivo, 'r', encoding='utf-8') as arquivo:
            for linha in arquivo:
                if linha.startswith(f"{numero} -"):
                    return linha.split(" - ", 1)[1].strip()
    except FileNotFoundError:
        print(f"Arquivo '{nome_arquivo}' não encontrado.")
    except Exception as e:
        print(f"Ocorreu um erro: {e}")

    return f"Convenio {numero}"


# Criar a janela principal
root = tk.Tk()
root.title("Calculadora Notas Fiscais - NF")

# Ajustar o tamanho e centralizar a interface
largura_janela = 360
altura_janela = 500  # Ajustado para 500 pixels
largura_tela = root.winfo_screenwidth()
altura_tela = root.winfo_screenheight()
x_pos = largura_tela // 2 - largura_janela // 2
y_pos = altura_tela // 2 - altura_janela // 2
root.geometry(f"{largura_janela}x{altura_janela}+{x_pos}+{y_pos}")

# Carregar a logo
logo_path = 'logo.png'
logo_image = Image.open(logo_path)
logo_image = logo_image.resize((212, 80), resample=Image.BICUBIC)
logo_photo = ImageTk.PhotoImage(logo_image)

# Adicionar a logo no rótulo
label_logo = ttk.Label(root, image=logo_photo)
label_logo.grid(row=0, column=0, columnspan=2, pady=10)

# Criar e posicionar widgets
label_numero = ttk.Label(root, justify="center", text="Digite o número do convênio para cálculo de impostos:")
entry_numero = ttk.Entry(root)

button_buscar = ttk.Button(root, text="Buscar Convênio", command=buscar_convenio)

label_convenio = ttk.Label(root, wraplength=350, justify="center")
label_valor = ttk.Label(root, justify="center", text="Digite o valor bruto para calcular os impostos (R$):")
entry_valor = ttk.Entry(root)

button_calcular = ttk.Button(root, text="Calcular Impostos", command=calcular_impostos)

resultado_text = tk.StringVar()
label_resultado = ttk.Label(root, textvariable=resultado_text, justify="center")

# Adicionar mensagem no rodapé
rodape_label = ttk.Label(root, justify="center", foreground="#90ee90",
                         text="Desenvolvido por MedCenter Hospital Dia ")

# Posicionar widgets usando grid
label_numero.grid(row=1, column=0, columnspan=2, sticky="w", padx=10, pady=5)
entry_numero.grid(row=2, column=0, columnspan=2, padx=10, pady=5)
button_buscar.grid(row=3, column=0, columnspan=2, pady=10)
label_convenio.grid(row=4, column=0, columnspan=2, padx=10, pady=1)
label_valor.grid(row=5, column=0, sticky="w", padx=25, pady=5)
entry_valor.grid(row=6, column=0, columnspan=2, padx=10, pady=5)
button_calcular.grid(row=7, column=0, columnspan=2, pady=10)
label_resultado.grid(row=8, column=0, columnspan=2, padx=10, pady=5)
rodape_label.grid(row=9, column=0, columnspan=2, pady=5)

# Iniciar a execução da interface gráfica
root.mainloop()
