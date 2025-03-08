import itertools
import tkinter as tk
from tkinter import filedialog, messagebox, ttk
import argparse
from tqdm import tqdm

def gerar_wordlist(base_palavras, tamanho_min, tamanho_max, arquivo_saida, incluir_numeros=False, incluir_especiais=False):
    """Gera uma wordlist combinando palavras da base fornecida e salva em um arquivo."""
    try:
        caracteres_extras = ""
        if incluir_numeros:
            caracteres_extras += "0123456789"
        if incluir_especiais:
            caracteres_extras += "!@#$%^&*()_-+=<>?"

        contador = 0
        with open(arquivo_saida, "w") as f:
            for tamanho in range(tamanho_min, tamanho_max + 1):
                for combinacao in itertools.permutations(base_palavras + list(caracteres_extras), tamanho):
                    palavra = "".join(combinacao)
                    f.write(palavra + "\n")
                    contador += 1
        messagebox.showinfo("Sucesso", f"Wordlist gerada com {contador} combinações e salva em {arquivo_saida}!")
    except Exception as e:
        messagebox.showerror("Erro", f"Erro: {str(e)}")

def selecionar_arquivo():
    arquivo = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt")])
    if arquivo:
        entrada_arquivo.delete(0, tk.END)
        entrada_arquivo.insert(0, arquivo)

def iniciar_geracao():
    palavras_base = entrada_palavras.get().strip().split()
    try:
        tamanho_min = int(entrada_min.get())
        tamanho_max = int(entrada_max.get())
        arquivo_saida = entrada_arquivo.get()
        incluir_numeros = var_numeros.get()
        incluir_especiais = var_especiais.get()
        
        if not palavras_base:
            messagebox.showwarning("Aviso", "Digite pelo menos uma palavra base.")
            return
        if not arquivo_saida:
            messagebox.showwarning("Aviso", "Selecione um arquivo de saída.")
            return
        if tamanho_min > tamanho_max:
            messagebox.showwarning("Aviso", "O tamanho mínimo não pode ser maior que o máximo.")
            return
        
        gerar_wordlist(palavras_base, tamanho_min, tamanho_max, arquivo_saida, incluir_numeros, incluir_especiais)
    except ValueError:
        messagebox.showerror("Erro", "Os tamanhos devem ser números inteiros.")

def limpar_campos():
    entrada_palavras.delete(0, tk.END)
    entrada_min.delete(0, tk.END)
    entrada_max.delete(0, tk.END)
    entrada_arquivo.delete(0, tk.END)

def modo_cli():
    parser = argparse.ArgumentParser(description="Gerador de Wordlist por Permutação de Palavras")
    parser.add_argument("palavras", nargs='+', help="Palavras base para gerar a wordlist")
    parser.add_argument("-min", type=int, default=3, help="Tamanho mínimo das palavras geradas")
    parser.add_argument("-max", type=int, default=6, help="Tamanho máximo das palavras geradas")
    parser.add_argument("-o", "--output", default="wordlist.txt", help="Arquivo de saída")
    parser.add_argument("--numeros", action="store_true", help="Incluir números nas combinações")
    parser.add_argument("--especiais", action="store_true", help="Incluir caracteres especiais nas combinações")
    
    args = parser.parse_args()
    gerar_wordlist(args.palavras, args.min, args.max, args.output, args.numeros, args.especiais)

if __name__ == "__main__":
    import sys
    if len(sys.argv) > 1:
        modo_cli()
    else:
        root = tk.Tk()
        root.title("Gerador de Wordlist")
        root.geometry("750x550")
        root.configure(bg="#2E2E3A")

        style = ttk.Style()
        style.configure("TButton", font=("Arial", 10, "bold"), padding=10, relief="flat", background="#8F43EE", foreground="white")
        style.configure("TLabel", foreground="#000", font=("Arial", 12, "bold"))
        style.configure("TEntry", padding=10, relief="flat", font=("Arial", 11))

        frame_principal = ttk.Frame(root, padding=20)
        frame_principal.pack(fill=tk.BOTH, expand=True)

        ttk.Label(frame_principal, text="Palavras base (separadas por espaço):").pack(pady=5)
        entrada_palavras = ttk.Entry(frame_principal, width=80)
        entrada_palavras.pack(pady=5)

        frame_tamanhos = ttk.Frame(frame_principal)
        frame_tamanhos.pack(pady=10)
        ttk.Label(frame_tamanhos, text="Tamanho mínimo:").pack(side=tk.LEFT, padx=5)
        entrada_min = ttk.Entry(frame_tamanhos, width=10)
        entrada_min.pack(side=tk.LEFT)
        ttk.Label(frame_tamanhos, text="Tamanho máximo:").pack(side=tk.LEFT, padx=5)
        entrada_max = ttk.Entry(frame_tamanhos, width=10)
        entrada_max.pack(side=tk.LEFT)

        ttk.Label(frame_principal, text="Arquivo de saída:").pack(pady=5)
        frame_arquivo = ttk.Frame(frame_principal)
        frame_arquivo.pack(pady=5)
        entrada_arquivo = ttk.Entry(frame_arquivo, width=60)
        entrada_arquivo.pack(side=tk.LEFT, padx=5)
        ttk.Button(frame_arquivo, text="Selecionar", command=selecionar_arquivo).pack(side=tk.LEFT)

        frame_opcoes = ttk.Frame(frame_principal)
        frame_opcoes.pack(pady=10)
        var_numeros = tk.BooleanVar()
        var_especiais = tk.BooleanVar()
        ttk.Checkbutton(frame_opcoes, text="Incluir números", variable=var_numeros).pack(side=tk.LEFT, padx=10)
        ttk.Checkbutton(frame_opcoes, text="Incluir caracteres especiais", variable=var_especiais).pack(side=tk.LEFT, padx=10)

        frame_botoes = ttk.Frame(frame_principal)
        frame_botoes.pack(pady=20)
        ttk.Button(frame_botoes, text="Gerar Wordlist", command=iniciar_geracao).pack(side=tk.LEFT, padx=10)
        ttk.Button(frame_botoes, text="Limpar", command=limpar_campos).pack(side=tk.LEFT, padx=10)

        root.mainloop()
