import csv
import os

def carregar_dataset(caminho_csv):
    """
    RF01 - Carrega o dataset de vendas a partir de um arquivo CSV.
    
    Argumentos:
        caminho_csv (str): O caminho completo do arquivo a ser lido.
        
    Retorna:
        list: Uma lista de dicionários contendo os registros do arquivo.
    """
    registros = []
    # Abrindo o arquivo em modo de leitura com a codificação correta
    with open(caminho_csv, mode="r", encoding="utf-8") as arquivo:
        leitor = csv.DictReader(arquivo)
        for linha in leitor:
            registros.append(linha)
            
    return registros

def inspecionar_dados(registros):
    """
    RF02 - Inspeciona a estrutura dos dados e exibe estatísticas no console.
    
    Argumentos:
        registros (list): Lista de dicionários com os dados de vendas.
    """
    total_registros = len(registros)
    
    # Extrai as colunas a partir do primeiro registro (se houver dados)
    colunas = list(registros[0].keys()) if registros else []
    
    # Inicializa o dicionário de contagem de valores ausentes (nulos)
    nulos = {coluna: 0 for coluna in colunas}
    
    # Varre os dados para contar campos em branco ou vazios
    for linha in registros:
        for coluna in colunas:
            if linha.get(coluna, "").strip() == "":
                nulos[coluna] += 1
                
    # Exibição formatada no console conforme esperado pelo manual
    print("\n" + "="*40)
    print("=== INSPEÇÃO INICIAL DO DATASET ===")
    print("="*40)
    print(f"Total de registros: {total_registros}")
    print(f"\nColunas encontradas:\n{colunas}")
    print(f"\nValores ausentes por coluna:\n{nulos}")
    print("\nPrimeiros 3 registros para amostragem:")
    for linha in registros[:3]:
        print(linha)
    print("="*40 + "\n")

def main():
    """
    Função principal que coordena o fluxo (pipeline) do projeto.
    """
    print("="*60)
    print("        SALESINSIGHT PY - Análise de Dados de Vendas        ")
    print("="*60)
    
    # Define o caminho do arquivo vendas.csv baseado na pasta atual do script
    pasta_atual = os.path.dirname(os.path.abspath(__file__))
    caminho_csv = os.path.join(pasta_atual, "vendas.csv")
    
    # Etapa 0: Validar se o arquivo de dados existe antes de tentar carregar
    if not os.path.exists(caminho_csv):
        print(f"❌ Erro: O arquivo '{caminho_csv}' não foi encontrado!")
        print("Por favor, rode o script gerador de dados primeiro.")
        return

    # Execução das Etapas 1 e 2
    print("📂 Carregando base de dados...")
    dados_brutos = carregar_dataset(caminho_csv)
    
    print("🔍 Iniciando inspeção estrutural...")
    inspecionar_dados(dados_brutos)

# Ponto de entrada oficial exigido no Requisito RF09 do manual
if __name__ == "__main__":
    main()
