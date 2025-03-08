# Gerador de Wordlist📄

## Descrição
Este é um gerador de wordlist desenvolvido em Python, que permite a criação de listas de palavras combinando palavras base fornecidas pelo usuário. O programa conta com uma interface gráfica (GUI) usando Tkinter e também pode ser executado via linha de comando (CLI).

## Funcionalidades
- Gera combinações de palavras com base em entradas fornecidas pelo usuário.
- Define o tamanho mínimo e máximo das palavras geradas.
- Permite incluir números e caracteres especiais nas combinações.
- Interface gráfica intuitiva para facilitar a interação.
- Possibilidade de execução via linha de comando.

## Requisitos
- Python 3.x
- Bibliotecas:
  - `tkinter`
  - `itertools`
  - `argparse`
  - `tqdm`

## Como Usar

### Interface Gráfica (GUI)
1. Execute o arquivo Python:
   ```bash
   python wordlist-generator.py
   ```
2. Insira as palavras base no campo correspondente.
3. Defina o tamanho mínimo e máximo das palavras.
4. Escolha se deseja incluir números e caracteres especiais.
5. Selecione o arquivo de saída.
6. Clique em "Gerar Wordlist".

### Linha de Comando (CLI)
Execute o comando abaixo:
```bash
python wordlist-generator.py palavra1 palavra2 -min 3 -max 6 -o wordlist.txt --numeros --especiais
```

Parâmetros:
- `palavra1 palavra2 ...` - Lista de palavras base.
- `-min` - Tamanho mínimo das palavras geradas.
- `-max` - Tamanho máximo das palavras geradas.
- `-o` ou `--output` - Nome do arquivo de saída.
- `--numeros` - Incluir números nas combinações.
- `--especiais` - Incluir caracteres especiais.

## Exemplo de Uso
```bash
python nome_do_arquivo.py senha admin -min 4 -max 8 -o wordlist.txt --numeros
```
Isso gerará uma wordlist baseada nas palavras "senha" e "admin", com tamanho entre 4 e 8 caracteres, incluindo números.

## Contribuição
Sinta-se à vontade para contribuir com melhorias! Basta fazer um fork do repositório, modificar e enviar um pull request.

## Licença
Este projeto está sob a licença MIT.

