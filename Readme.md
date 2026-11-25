# SalesInsight PY — Análise de Dados de Vendas

Este projeto consiste em um pipeline de análise de dados desenvolvido inteiramente em **Python puro**, utilizando exclusivamente a biblioteca padrão do sistema (nativa). O sistema carrega, inspeciona, limpa, transforma e agrega uma base de dados de varejo, gerando relatórios consolidados em formatos CSV e JSON.

## Objetivo do Projeto
Atuar como um analisador automatizado de dados de vendas para responder a perguntas estratégicas de negócios da diretoria, tais como o faturamento mensal, volume de vendas, desempenho regional e identificação de clientes de alto valor.

## Tecnologias e Conceitos Aplicados
*   **Lógica de Programação:** Estruturas de repetição (`for`, `while`), condicionais (`if/elif/else`) e tipos de dados nativos (`list`, `dict`).
*   **Tratamento de Arquivos:** Leitura e escrita automatizada com os módulos nativos `csv` e `json`.
*   **Manipulação de Datas:** Módulo `datetime` para extração e validação de períodos temporais.
*   **Expressões Regulares:** Módulo `re` para limpeza e padronização de strings.
*   **Paradigma Funcional:** Uso de funções com parâmetros, retornos, `docstrings` documentadas e funções de ordem superior (*Higher-Order Functions*) combinadas com expressões `lambda`.
*   **Controle de Versão:** Versionamento estruturado utilizando Git e convenção de commits (*Conventional Commits*).

## Estrutura do Projeto
```text
Miniprojeto1/
├── salesinsight.py         # Arquivo principal do pipeline de dados
├── vendas.csv              # Base de dados original (gerada para testes)
├── README.md               # Documentação técnica do projeto (este arquivo)
├── tarefas-kanban.md       # Histórico de gerenciamento ágil do projeto
└── outputs/                # Relatórios exportados automaticamente pelo script
    ├── metricas_por_mes.csv
    ├── segmentacao_clientes.csv
    └── estatisticas_gerais.json
```

## Instruções de Instalação e Execução
Como o projeto utiliza apenas a biblioteca padrão do Python, não há dependências externas a serem instaladas.

1.  Certifique-se de ter o Python 3.10 ou superior instalado na máquina.
2.  Abra o terminal na pasta do projeto e execute o comando:
    ```bash
    python salesinsight.py
    ```
3.  Os resultados analíticos serão impressos diretamente no console e os arquivos de relatório serão atualizados na pasta `outputs/`.

## Decisões Técnicas Justificadas
*   **Remoção de registros inválidos (Data e Nulos):** Optou-se pela exclusão estrita de linhas com datas corrompidas ou ausência de quantidade/preço por se tratarem de dados críticos. Em cenários preditivos ou de fechamento contábil, inventar ou imputar valores arbitrários (como média ou zero) sem regras de negócio consolidadas traria distorções severas nas métricas financeiras.
*   **Uso de `defaultdict`:** A estrutura de agregação foi otimizada utilizando `collections.defaultdict`. Isso elimina a necessidade de checar manualmente se uma chave (como o nome do mês) já existe no dicionário antes de somar os valores, reduzindo a complexidade do código de O(N²) para O(N) e deixando o script mais performático.
