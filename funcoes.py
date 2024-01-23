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
        deducao = round(valor * 0.4, 3)
        ir = round(valor * 0.015, 3)
        pis = round(valor * 0.065, 3)
        cofins = round(valor * 0.03, 3)
        clss = round(valor * 0.01, 3)
        vliquido = round(valor - (ir + pis + cofins + clss), 3)

        # Limpar resultados anteriores
        for row in tree.get_children():
            tree.delete(row)

        # Adicionar novos resultados à tabela
        tree.insert("", "end", values=["DEDUÇÃO", f"R${deducao}"])
        tree.insert("", "end", values=["IR", f"R${ir}"])
        tree.insert("", "end", values=["PIS", f"R${pis}"])
        tree.insert("", "end", values=["COFINS", f"R${cofins}"])
        tree.insert("", "end", values=["CLSS", f"R${clss}"])
        tree.insert("", "end", values=["VALOR LÍQUIDO", f"R${vliquido}"])

    else:
        label_convenio.config(foreground="#800000", text=f"\nO convênio {numero_usuario} não está cadastrado!")


def buscar_convenio():
    numero_usuario = entry_numero.get()

    if verificar_numero_arquivo(numero_usuario):
        nome_convenio = obter_nome_convenio(numero_usuario)
        label_convenio.config(text=f"{nome_convenio}", foreground="#006400")
    else:
        label_convenio.config(foreground="#8B0000", text=f"\nO convênio {numero_usuario} não está cadastrado!")




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


def on_enter_key_calcular(event):
    calcular_impostos()


def on_enter_key_buscar(event):
    buscar_convenio()