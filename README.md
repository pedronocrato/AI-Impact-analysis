# 📊 Análise dos Impactos da IA no Mercado Global

Dashboard interativo desenvolvido em Streamlit para explorar como a Inteligência 
Artificial está transformando o mercado de trabalho global, com foco em adoção, perda de empregos e relação entre variáveis por setor e país.

## Visão Geral

| Aba | Conteúdo |
|---|---|
| Por Setor | média de adoção de IA, relação com perda de empregos e séries temporais de empregos perdidos e relação adoção/receita por setor |
| Por País | taxa de adoção, série temporal de receita, empregos perdidos e relação colaboração/perda de empregos por país |

## Principais Insights

- Setores automotivo e de manufatura lideram a perda de empregos por adoção de IA
- Reino Unido apresenta a maior taxa de adoção, mesmo com regulações predominantemente restritas
- Cruzamento entre adoção de IA, receita e participação de mercado ao longo do tempo (2020–2025)

## Estrutura do Projeto
```
├── graficos/           # gráficos gerados com pandas/matplotlib
├── analises.ipynb      # exploração e análise dos dados
├── criar_planilhas.py  # extração e transformação dos dados
├── graficos.py         # geração dos gráficos
├── interface.py        # dashboard Streamlit com filtros interativos
├── Global_AI_Content_Impact_Dataset.csv
└── Global_AI_Content_Impact_Dataset.xlsx
```

## Tecnologias

| Ferramenta | Uso |
|---|---|
| Python | manipulação e análise dos dados |
| Pandas | transformação e estruturação |
| Plotly | visualização estática dos dados |
| Streamlit | interface interativa do dashboard |
| Jupyter Notebook | exploração e prototipagem das análises |

## Como executar
```bash
pip install -r requirements.txt
streamlit run interface.py
```

## Prévia

**Dashboard Streamlit**
![Streamlit](assets/previa_streamlit.png)

**Análise Excel**
![Excel](assets/previa_excel.jpg)

👨‍💻 Autores
Artur Da Ponte

Pedro Roberto
