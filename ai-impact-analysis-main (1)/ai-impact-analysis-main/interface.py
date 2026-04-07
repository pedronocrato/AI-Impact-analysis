import streamlit as st
import graficos

st.header('Análise dos Impactos da IA no mercado global')

tab1, tab2 = st.tabs(['Por Setor', 'Por País'])
        
with tab1:
    col1, col2 = st.columns(2)
    col3, col4 = st.columns(2)
    col5, col6 = st.columns(2)

    with col1:
        graficos.fig1
    with col2:
        graficos.fig2
    with col5:
        setores = st.multiselect(label='Setores', options=graficos.dados['Industry'].unique(), max_selections=5, default='Healthcare')
    with col3:
        st.plotly_chart(graficos.fig4(setores))
    with col6:
        setor = st.selectbox(label='Setor', options=graficos.dados['Industry'].unique())
    with col4:
        st.plotly_chart(graficos.fig6(setor))

with tab2:
    col1, col2, col3 = st.columns(3)
    col4, col5, col6 = st.columns(3)

    with col1:
        graficos.fig3
    with col3:
        pais = st.selectbox(label='País', options=graficos.dados['Country'].unique())
    with col2:
        st.plotly_chart(graficos.fig5(pais))
    with col4:
        graficos.fig7
    with col6:
        paises = st.multiselect(label='Países', options=graficos.dados['Country'].unique(), max_selections=5, default='UK')
    with col5:
        st.plotly_chart(graficos.fig8(paises))