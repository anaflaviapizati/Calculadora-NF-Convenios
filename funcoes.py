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

match numero-usuario

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