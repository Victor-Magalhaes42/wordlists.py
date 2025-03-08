import itertools

def gerar_wordlist(base_palavras, tamanho_min=3, tamanho_max=6, arquivo_saida="wordlist.txt"):
    """Gera uma wordlist combinando palavras da base fornecida."""
    with open(arquivo_saida, "w") as f:
        for tamanho in range(tamanho_min, tamanho_max + 1):
            for combinacao in itertools.permutations(base_palavras, tamanho):
                palavra = "".join(combinacao)
                f.write(palavra + "\n")
    print(f"Wordlist gerada com sucesso e salva em {arquivo_saida}!")

if __name__ == "__main__":
    palavras_base = input("Digite palavras base separadas por espaço: ").split()
    tamanho_min = int(input("Tamanho mínimo das palavras: "))
    tamanho_max = int(input("Tamanho máximo das palavras: "))
    
    gerar_wordlist(palavras_base, tamanho_min, tamanho_max)
