# Quadro de Planejamento de Tarefas (Kanban)

Histórico de organização ágil das entregas do Mini-Projeto SalesInsight.

## A Fazer (To Do)
*   [ ] Gravar vídeo de demonstração técnica (máximo 5 minutos).
*   [ ] Enviar os links finais na plataforma do AVA (Prazo: 28/09/2026).

## Em Andamento (Doing)
*   [ ] Realizar o envio final (*push*) dos commits para o repositório do GitHub.

## Concluído (Done)
*   **[X] Configuração do Ambiente:** Instalação do Git, configuração de identidade (`user.name`/`user.email`) e inicialização do repositório (`git init`).
*   **[X] RF01 & RF02 (Carga e Inspeção):** Construção da função `carregar_dataset` e mapeamento estrutural dos dados em branco.
*   **[X] RF03 (Limpeza de Dados):** Implementação de remoção por `try/except` de datas e limpeza de nomes com `re.sub()`.
*   **[X] RF04 (Colunas Derivadas):** Cálculo da receita por linha e extração condicional de meses e trimestres (Q1-Q4).
*   **[X] RF05 (Métricas de Fechamento):** Agrupamento de faturamento e volume mensal usando `defaultdict`.
*   **[X] RF06 (Segmentação de Clientes):** Classificação em faixas de gasto Bronze, Prata e Ouro utilizando função `lambda`.
*   **[X] RF07 (Ordem Superior):** Implementação da função `processar_coluna` recebendo assinaturas funcionais externas.
*   **[X] RF08 (Exportação dos Relatórios):** Escrita automatizada de arquivos CSV e JSON estruturados na pasta `outputs/`.
*   **[X] RF09 (Função Controladora):** Integração de todas as etapas de ponta a ponta na função `main()`.
