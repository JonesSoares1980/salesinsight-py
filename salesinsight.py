import csv
import os
import re
from datetime import datetime
from collections import defaultdict

def carregar_dataset(caminho_csv):
    """RF01 - Carrega o dataset de vendas a partir de um arquivo CSV."""
    registros = []
    with open(caminho_csv, mode="r", encoding="utf-8") as arquivo:
        leitor = csv.DictReader(arquivo)
        for linha in leitor:
            registros.append(linha)
    return registros

def inspecionar_dados(registros):
    """RF02 - Inspeciona a estrutura dos dados e exibe estatísticas no console."""
    total_registros = len(registros)
    colunas = list(registros[0].keys()) if registros else []
    nulos = {coluna: 0 for coluna in colunas}
    
    for linha in registros:
        for coluna in colunas:
            if linha.get(coluna, "").strip() == "":
                nulos[coluna] += 1
                
    print("\n" + "="*40)
    print("=== INSPEÇÃO INICIAL DO DATASET ===")
    print("="*40)
    print(f"Total de registros: {total_registros}")
    print(f"\nColunas encontradas:\n{colunas}")
    print(f"\nValores ausentes por coluna:\n{nulos}")
    print("="*40 + "\n")

def limpar_dados(registros):
    """RF03 - Limpa e trata a lista de registros de vendas."""
    registros_limpos = []
    total_iniciais = len(registros)
    removidos_data = 0
    removidos_nulos = 0
    
    for linha in registros:
        for chave in ("cliente", "produto", "categoria", "regiao"):
            if linha[chave]:
                linha[chave] = linha[chave].strip()
                
        try:
            datetime.strptime(linha["data_venda"], "%Y-%m-%d")
        except ValueError:
            removidos_data += 1
            continue
            
        if linha["quantidade"] == "" or linha["preco_unitario"] == "":
            removidos_nulos += 1
            continue
            
        try:
            linha["quantidade"] = int(float(linha["quantidade"]))
            linha["preco_unitario"] = float(linha["preco_unitario"])
        except ValueError:
            removidos_nulos += 1
            continue
            
        nome_limpo = re.sub(r"[^A-Za-z0-9_]", "", linha["cliente"])
        linha["cliente"] = nome_limpo
        registros_limpos.append(linha)
        
    print("="*40)
    print("=== RELATÓRIO DE LIMPEZA DE DADOS (RF03) ===")
    print("="*40)
    print(f"Registros recebidos: {total_iniciais}")
    print(f"❌ Removidos por data inválida: {removidos_data}")
    print(f"❌ Removidos por valores nulos/vazios: {removidos_nulos}")
    print(f"✅ Registros limpos e mantidos: {len(registros_limpos)}")
    print("="*40 + "\n")
    
    return registros_limpos

def criar_colunas_derivadas(registros):
    """RF04 - Cria colunas derivadas (receita_total, mes, mes_nome, ano, trimestre)."""
    meses_pt = {
        1: "Janeiro", 2: "Fevereiro", 3: "Março", 4: "Abril",
        5: "Maio", 6: "Junho", 7: "Julho", 8: "Agosto",
        9: "Setembro", 10: "Outubro", 11: "Novembro", 12: "Dezembro"
    }
    
    for linha in registros:
        linha["receita_total"] = round(linha["quantidade"] * linha["preco_unitario"], 2)
        data_obj = datetime.strptime(linha["data_venda"], "%Y-%m-%d")
        linha["mes"] = data_obj.month
        linha["ano"] = data_obj.year
        linha["mes_nome"] = meses_pt[data_obj.month]
        
        if data_obj.month <= 3:
            linha["trimestre"] = "Q1"
        elif data_obj.month <= 6:
            linha["trimestre"] = "Q2"
        elif data_obj.month <= 9:
            linha["trimestre"] = "Q3"
        else:
            linha["trimestre"] = "Q4"
            
    print("✨ Novas colunas calculadas e adicionadas com sucesso (RF04)!\n")
    return registros

def calcular_metricas(registros):
    """RF05 - Calcula métricas agregadas por Mês."""
    metricas_por_mes = defaultdict(lambda: {"receita_total": 0.0, "quantidade_vendida": 0, "n_vendas": 0})
    
    for linha in registros:
        mes = linha["mes_nome"]
        metricas_por_mes[mes]["receita_total"] += linha["receita_total"]
        metricas_por_mes[mes]["quantidade_vendida"] += linha["quantidade"]
        metricas_por_mes[mes]["n_vendas"] += 1
        
    print("="*55)
    print("=== MÉTRICAS AGREGADAS POR MÊS (RF05) ===")
    print("="*55)
    print(f"{'Mês':<15} | {'Faturamento':<12} | {'Qtd Vendida':<11} | {'Nº Vendas'}")
    print("-"*55)
    for mes, valores in metricas_por_mes.items():
        faturamento_formatado = f"R$ {valores['receita_total']:.2f}"
        print(f"{mes:<15} | {faturamento_formatado:<12} | {valores['quantidade_vendida']:<11} | {valores['n_vendas']}")
    print("="*55 + "\n")
    
    return metricas_por_mes

def segmentar_clientes(registros):
    """RF06 - Agrupa o gasto total por cliente e os classifica usando lambda."""
    total_por_cliente = {}
    for linha in registros:
        cliente = linha["cliente"]
        total_por_cliente[cliente] = total_por_cliente.get(cliente, 0.0) + linha["receita_total"]

    classificar = lambda total: "Ouro" if total > 15000 else "Prata" if total >= 5000 else "Bronze"

    clientes_segmentados = []
    contagem_segmentos = {"Bronze": 0, "Prata": 0, "Ouro": 0}
    
    for nome, total in total_por_cliente.items():
        segmento = classificar(total)
        contagem_segmentos[segmento] += 1
        clientes_segmentados.append({
            "cliente": nome,
            "total_gasto": round(total, 2),
            "segmento": segmento
        })

    clientes_ordenados = sorted(clientes_segmentados, key=lambda x: x["total_gasto"], reverse=True)

    print("="*50)
    print("=== TOP 10 CLIENTES POR VALOR DE GASTO (RF06) ===")
    print("="*50)
    print(f"{'Posição':<7} | {'Cliente':<15} | {'Total Gasto':<14} | {'Segmento'}")
    print("-"*50)
    for i, c in enumerate(clientes_ordenados[:10], 1):
        gasto_formatado = f"R$ {c['total_gasto']:.2f}"
        print(f"{i:<7} | {c['cliente']:<15} | {gasto_formatado:<14} | {c['segmento']}")
    print("-"*50)
    print(f"📊 Distribuição Geral dos Segmentos:\n{contagem_segmentos}")
    print("="*50 + "\n")

    return clientes_ordenados

def main():
    print("="*60)
    print("        SALESINSIGHT PY - Análise de Dados de Vendas        ")
    print("="*60)
    
    pasta_atual = os.path.dirname(os.path.abspath(__file__))
    caminho_csv = os.path.join(pasta_atual, "vendas.csv")
    
    if not os.path.exists(caminho_csv):
        print(f"❌ Erro: O arquivo '{caminho_csv}' não foi encontrado!")
        return

    dados_brutos = carregar_dataset(caminho_csv)
    inspecionar_dados(dados_brutos)
    
    dados_processados = limpar_dados(dados_brutos)
    dados_transformados = criar_colunas_derivadas(dados_processados)
    
    print("📈 Calculando métricas de fechamento mensal...")
    dados_agregados = calcular_metricas(dados_transformados)
    
    print("👥 Iniciando a segmentação e análise de clientes...")
    clientes_processados = segmentar_clientes(dados_transformados)
    
    print("🎉 Pipeline executado com sucesso até a classificação de clientes!")

if __name__ == "__main__":
    main()
