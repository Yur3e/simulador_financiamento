import tkinter as tk
from tkinter import ttk

class PayHome:
    def __init__(self, vlm, anosp, jsa, porctend):
        self.vlm = vlm
        self.anosp = anosp
        self.jsa = jsa
        self.porctend = porctend

    def calculate(self):
        porcentagem_entrada = self.vlm * (self.porctend / 100)
        valor_emprestimo = self.vlm - porcentagem_entrada
        taxa_juros_anual = self.jsa / 100
        taxa_juros_mensal = taxa_juros_anual / 12
        num_parcelas = self.anosp * 12
        amortizacao_mensal = valor_emprestimo / num_parcelas

        saldo_devedor = valor_emprestimo
        result_text = ""
        for meses in range(1, num_parcelas + 1):
            juros_mensais = saldo_devedor * taxa_juros_mensal
            parcela_mensal = amortizacao_mensal + juros_mensais
            saldo_devedor -= amortizacao_mensal

            result_text += f"Mês {meses}: Amortização = R$ {amortizacao_mensal:.2f}, Juros = R$ {juros_mensais:.2f}, Parcela Mensal = R$ {parcela_mensal:.2f}\n"

        return result_text

def calculate_button_clicked():
    vlm = float(vlm_entry.get())
    anosp = int(anosp_entry.get())
    jsa = float(jsa_entry.get())
    porctend = float(porctend_entry.get())

    payhome = PayHome(vlm, anosp, jsa, porctend)
    result_text = payhome.calculate()

    result_textbox.delete("1.0", tk.END)
    result_textbox.insert(tk.END, result_text)

# Criando a janela principal
root = tk.Tk()
root.title("Simulador de Financiamento")
root.geometry("400x300")  # Definindo o tamanho da janela (largura x altura)
root.resizable(False, False)  # Bloqueando o redimensionamento da janela


# Criando os widgets
vlm_label = ttk.Label(root, text="Valor do Imóvel:")
vlm_entry = ttk.Entry(root)

anosp_label = ttk.Label(root, text="Anos de Financiamento:")
anosp_entry = ttk.Entry(root)

jsa_label = ttk.Label(root, text="Taxa de Juros Anual (%):")
jsa_entry = ttk.Entry(root)

porctend_label = ttk.Label(root, text="Porcentagem de Entrada (%):")
porctend_entry = ttk.Entry(root)

calculate_button = ttk.Button(root, text="Calcular", command=calculate_button_clicked)

result_label = ttk.Label(root, text="Resultados:")
result_textbox = tk.Text(root, height=10, width=50)

# Posicionando os widgets na janela
vlm_label.grid(row=0, column=0, sticky=tk.W)
vlm_entry.grid(row=0, column=1)

anosp_label.grid(row=1, column=0, sticky=tk.W)
anosp_entry.grid(row=1, column=1)

jsa_label.grid(row=2, column=0, sticky=tk.W)
jsa_entry.grid(row=2, column=1)

porctend_label.grid(row=3, column=0, sticky=tk.W)
porctend_entry.grid(row=3, column=1)

calculate_button.grid(row=4, column=0, columnspan=2)

result_label.grid(row=5, column=0, sticky=tk.W)
result_textbox.grid(row=6, column=0, columnspan=2)

# Iniciando o loop principal da janela
root.mainloop()
