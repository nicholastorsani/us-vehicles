# us-vehicles
# Análise dos dados da revenda de veículos usados nos EUA (2018-2019)

Este projeto explora a análise de um conjunto de dados de veículos usados nos Estados Unidos a partir da geração de histogramas e gráficos de dispersão das seguintes variáveis presentes na base de dados: Preço, Milhagem, Marca, Ano do carro, Condição, tipo de combustível, número de cilindros, tração, transmissão e categoria do automóvel. A aplicação foi desenvolvida com **Python**, **Pandas**, **Plotly Express** e **Streamlit**, e está hospedada para testes no Render, conforme link: https://us-vehicles.onrender.com/

## Estrutura do Projeto:

```bash
us-vehicles/
│
├── app.py               # aplicação principal com interface Streamlit
├── vehicles.csv         # base de dados dos veículos
├── requirement.txt      # dependências do projeto
├── README.md            # este Arquivo
├── .gitignore           # lista de arquivos a serem ignorados pelo git
└── /notebooks           # pasta com as análises exploratórias
    └── eda.ipynb        # notebook com exploração inicial dos dados
└── /streamlit           # pasta com as configurações da biblioteca Streamlit
    └── config.toml      # configurações da biblioteca
```
## Como executar:
1º - Clone o repositório:
    git clone https://github.com/nicholastorsani/us-vehicles
    cd us-vehicles

2º - Instale os requisitos:
    pip install -r requirements.txt

3º - Rode o app:
    streamlit run app.py

## Funcionalidades:
- Seleção de variáveis para análise personalizada.
- Geração de histogramas e gráficos de dispersão.
- Visualização intuitiva com Plotly.
- Interface interativa com Streamlit.

## Tecnologias usadas:
- Python
- Bibliotecas: Pandas, Plotly Express e Streamlit
- Jupyter Notebook

## Autor
- Nicholas Torsani
- email: nicholas.torsani@gmail.com
