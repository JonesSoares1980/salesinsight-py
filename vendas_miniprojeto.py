import csv
import random
import os
from datetime import datetime, timedelta

#RF01

def gerar_dataset_vendas(caminho_csv="vendas.csv", n_registros=200, seed=42):
    """Gera um dataset sintético de vendas com dados sujos e grava em CSV."""
    random.seed(seed)
    
    produtos = ["Notebook", "Smartphone", "Tablet", "Monitor", "Teclado", "Mouse", "Headset"]
    
    categorias = {
        "Notebook": "Computadores", "Smartphone": "Celulares",
        "Tablet": "Celulares", "Monitor": "Computadores",
        "Teclado": "Perifericos", "Mouse": "Perifericos",
        "Headset": "Perifericos"
    }
    
    precos = {
        "Notebook": 3500, "Smartphone": 2200, "Tablet": 1800,
        "Monitor": 1200, "Teclado": 250, "Mouse": 120, "Headset": 350
    }
    
    regioes = ["Sudeste", "Sul", "Nordeste", "Centro-Oeste", "Norte"]
    data_inicio = datetime(2025, 1, 1)
    
    colunas = ["id_venda", "data_venda", "cliente", "produto", "categoria", "regiao", "quantidade", "preco_unitario"]
    
    # Abrindo e criando o arquivo CSV
    with open(caminho_csv, "w", newline="", encoding="utf-8") as arquivo:
        escritor = csv.DictWriter(arquivo, fieldnames=colunas)
        escritor.writeheader()  # Escreve o cabeçalho com o nome das colunas
        
        for i in range(n_registros):
            produto = random.choice(produtos)
            categoria = categorias[produto]
            quantidade = random.randint(1, 10)
            
            # Calcula o preço com uma leve variação simulando descontos
            preco = round(precos[produto] * random.uniform(0.85, 1.15), 2)
            
            # Gera datas aleatórias ao longo de um ano
            data = data_inicio + timedelta(days=random.randint(0, 364))
            data_txt = data.strftime("%Y-%m-%d")
            
            cliente = f"Cliente_{random.randint(1, 50):03d}"
            
            # --- Inserção de "sujeira" proposital para a etapa de limpeza ---
            # 5% de chance de deixar a quantidade em branco
            if random.random() < 0.05:
                quantidade = ""
            
            # 4% de chance de deixar o preço em branco
            if random.random() < 0.04:
                preco = ""
                
            # 6% de chance de adicionar espaços extras no nome do produto
            if random.random() < 0.06:
                produto = "  " + produto + "   "
                
            # 3% de chance de avariar a data (torná-la inválida)
            if random.random() < 0.03:
                data_txt = "DATA INVALIDA"
                
            # 10% de chance de adicionar ruído ou caracteres especiais no nome do cliente
            if random.random() < 0.10:
                cliente = random.choice([
                    cliente.upper().replace("_", "-"),
                    cliente + "!!",
                    "#" + cliente,
                    cliente.replace("Cliente", "cliente#")
                ])
            
            # Escreve a linha no arquivo CSV (Correção aplicada aqui)
            escritor.writerow({
                "id_venda": i + 1,
                "data_venda": data_txt,
                "cliente": cliente,
                "produto": produto,
                "categoria": categoria,
                "regiao": random.choice(regioes),
                "quantidade": quantidade,
                "preco_unitario": preco
            })
            
    print(f"✅ Sucesso! Dataset gerado com {n_registros} registros em:\n📁 {caminho_csv}")

#RF02

# ==============================================================================
# BLOCO DE CONFIGURAÇÃO DE CAMINHOS (ONDE O ARQUIVO SERÁ SALVO)
# ==============================================================================

# 1. Descobre onde o script vendas_miniprojeto.py está rodando atualmente
caminho_atual = os.path.dirname(os.path.abspath(__file__))

# 2. Caminho definitivo para a pasta 'Miniprojeto1' dentro do curso
# Caso o script já esteja em Miniprojeto1, garantimos o salvamento na mesma pasta
caminho_final_csv = os.path.join(caminho_atual, "vendas.csv")

# 3. Executa a função geradora passando o caminho definitivo da pasta solicitada
gerar_dataset_vendas(caminho_csv=caminho_final_csv)

def carregar_dataset(caminho_csv):
    """Lê o arquivo CSV e retorna uma lista de dicionários (um por registro)."""
    registros = []
    # Abrimos o arquivo no modo leitura ("r" de read)
    with open(caminho_csv, "r", encoding="utf-8") as arquivo:
        leitor = csv.DictReader(arquivo)
        for linha in leitor:
            registros.append(linha)
    return registros

def inspecionar_dados(registros):
    """Exibe as informações estruturais da lista de registros no console."""
    total = len(registros)
    
    # Se a lista não estiver vazia, pegamos as chaves (colunas) do primeiro registro
    colunas = list(registros[0].keys()) if registros else []
    
    # Criamos um dicionário para contar os nulos, começando com zero para cada coluna
    nulos = {coluna: 0 for coluna in colunas}
    
    # Varremos cada linha e cada coluna procurando campos vazios
    for linha in registros:
        for coluna in colunas:
            # O .strip() remove espaços invisíveis. Se sobrar "", o campo está vazio
            if linha.get(coluna, "").strip() == "":
                nulos[coluna] += 1
                
    # Exibição bonita formatada no console conforme o manual do projeto
    print("\n" + "="*30)
    print("=== INSPEÇÃO INICIAL DO DATASET ===")
    print("="*30)
    print(f"Total de registros: {total}")
    print(f"\nColunas: {colunas}")
    print(f"\nValores ausentes por coluna:\n{nulos}")
    
    print("\nPrimeiros 3 registros para amostragem:")
    for linha in registros[:3]:
        print(linha)
    print("="*30)

# ==============================================================================
# DISPARO DO PIPELINE (RODANDO AS FUNÇÕES EM ORDEM)
# ==============================================================================

# 1. Carrega os dados que foram gerados no passo anterior
meus_dados = carregar_dataset(caminho_final_csv)

# 2. Executa a inspeção estrutural deles
inspecionar_dados(meus_dados)
