import streamlit as st
import pandas as pd
import plotly.express as px

# importação da base de dados como dataframe
vehicles = pd.read_csv('vehicles.csv')

# pré-processamento dos dados, tal qual explicado no notebook
vehicles['brand'] = vehicles['model'].str.extract(r'^(\w+)')
vehicles['date_posted'] = pd.to_datetime(vehicles['date_posted'], format='%Y-%m-%d')
vehicles['year_posted'] = vehicles['date_posted'].dt.year
vehicles['month_posted'] = vehicles['date_posted'].dt.month
vehicles['day_posted'] = vehicles['date_posted'].dt.day
vehicles['day_of_week_posted'] = vehicles['date_posted'].dt.day_of_week
vehicles['is_4wd'] = vehicles['is_4wd'].fillna(0)
vehicles['is_4wd'] = vehicles['is_4wd'].replace({1: 'sim', 0: 'não'})

# inserir cabeçalho e informações
st.header("Explorador de Dados Automotivos") 
st.markdown("""
Este painel interativo permite explorar dados de veículos usados listados à venda nos Estados Unidos por meio de histogramas e gráficos de dispersão.

**Como usar:**
- Selecione o tipo de gráfico desejado (Histograma ou Dispersão).
- Escolha as variáveis que deseja visualizar (ex: Preço, Milhagem, Marca).
- Clique em **"Fazer gráfico"** para gerar a visualização.

Use os gráficos para comparar distribuições, identificar padrões e obter insights sobre os dados de veículos.

Para conferir todo o projeto acesse: https://github.com/nicholastorsani/us-vehicles
""")

# inserir instruções de uso:
st.write("**Selecione o tipo de gráfico desejado:**")

# checkbox para criar histograma
build_histogram = st.checkbox("Histograma", 
            label_visibility="visible")
# criar grafico de dispersao
build_scatter = st.checkbox("Dispersão", 
            label_visibility="visible")

# caixa de texto para seleção dos elementos do gráfico:
st.write("**Selecione**:\n - **Um elemento para histograma.**\n - **Ou dois elementos para gráfico de dispersão.**")

# checkboxes de seleção de variáveis
price = st.checkbox('Preço')
odometer = st.checkbox('Milhagem (Odômetro)')
brand = st.checkbox('Marca')
model_year = st.checkbox('Ano do carro')
condition = st.checkbox('Condição do carro')
fuel = st.checkbox('Tipo de Combustível')
is_4wd = st.checkbox('É 4x4?')
transmission = st.checkbox('Transmissão')
cylinders = st.checkbox('Número de cilindros')
type = st.checkbox('Categoria do carro')

# condição para plotagem dos gráficos ao apertar o botão
if st.button('Fazer gráfico'):
    # coleta as variáveis selecionadas nas checkboxes e coloca na lista selected_vars
    selected_vars = []
    if price:
        selected_vars.append("price")
    if odometer:
        selected_vars.append("odometer")
    if brand:
        selected_vars.append("brand")
    if model_year:
        selected_vars.append("model_year")
    if condition:
        selected_vars.append("condition")
    if fuel:
        selected_vars.append("fuel")
    if is_4wd:
        selected_vars.append("is_4wd")
    if transmission:
        selected_vars.append("transmission")
    if cylinders:
        selected_vars.append("cylinders")
    if type:
        selected_vars.append("type")

    # labels para as colunas
    label_map = {
        "price": "Preço do carro (Dólares)",
        "odometer": "Milhas percorridas (Odômetro)",
        "brand": "Marca",
        "model_year": "Ano do carro",
        'condition':'Condição do carro',
        'fuel':'Tipo de Combustível',
        'is_4wd':'É 4x4?',
        'transmission':'Transmissão',
        'cylinders':'Número de cilindros',
        'type':'Categoria do carro'
    }

    # histograma (só pode ter 1 variável)
    if build_histogram:
        if len(selected_vars) == 1:
            # variável x usada é a primeira da lista selecionada nas checkboxes
            x_var = selected_vars[0]
            # plotagem usando plotly express
            fig = px.histogram(vehicles, 
                               x=x_var, 
                               color=x_var if x_var == 'brand' else None,
                               labels={x_var: label_map[x_var]})
            st.plotly_chart(fig, use_container_width=True)
        # condição caso requisitos não sejam cumpridos
        else:
            st.markdown('<span style="color: red;">**Erro:** selecione **apenas uma variável** para o histograma.</span>', unsafe_allow_html=True)

    # gráfico de dispersão (precisa de 2 variáveis)
    elif build_scatter:
        if len(selected_vars) == 2:
            # condição para variável price estar no eixo y e variável model_year no eixo x
            var1, var2 = selected_vars[0], selected_vars[1]

            if 'price' in selected_vars:
                y_var = 'price'
                x_var = var2 if var1 == 'price' else var1
            elif 'model_year' in selected_vars:
                x_var = 'model_year'
                y_var = var2 if var1 == 'model_year' else var1
            else:
                x_var, y_var = var1, var2
            # plotagem usando plotly express
            fig = px.scatter(vehicles, 
                             x=x_var, 
                             y=y_var,
                             color='brand' if 'brand' in selected_vars else None,
                             labels={x_var: label_map.get(x_var, x_var), y_var: label_map.get(y_var, y_var)})
            st.plotly_chart(fig, use_container_width=True)
        # condição caso requisitos não sejam cumpridos
        else: 
            st.markdown('<span style="color: red;">**Erro:** selecione **duas variáveis** para o gráfico de dispersão.</span>', unsafe_allow_html=True)