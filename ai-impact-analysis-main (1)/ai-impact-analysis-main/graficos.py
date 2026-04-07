import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from criar_planilhas import criar_planilha

dados = criar_planilha()

analise1 = dados.groupby('Industry')[['AI Adoption Rate (%)']].mean()

fig1 = px.bar(analise1.reset_index(), 
             x='AI Adoption Rate (%)', 
             y='Industry',
             orientation='h',
             color_discrete_sequence=['skyblue'])

fig1.update_layout(
    xaxis_range=[0, 100],
    height=300,            
    width=600,
    title={
        'text': 'Média de Adoção de IA por Setor',
        'font_size': 16,
        'x': 0.5,
        'xanchor': 'center'
    },
    xaxis_title='Taxa de Adoção de IA (%)',
    yaxis_title='Setor',
    font=dict(
        color='white', 
        family='Arial',
        size=15
    ),
    plot_bgcolor='rgba(0, 0, 0, 0)',
    paper_bgcolor='rgba(20, 20, 30, 1)'
)


analise2 = dados.groupby('Industry')[['AI Adoption Rate (%)','Job Loss Due to AI (%)']].mean()

fig2 = go.Figure()

fig2.add_trace(go.Bar(
    x=analise2['AI Adoption Rate (%)'],
    y=analise2.index,
    orientation='h',
    name='Adoção de IA',
    marker_color='royalblue'
))

fig2.add_trace(go.Bar(
    x=analise2['Job Loss Due to AI (%)'],
    y=analise2.index,
    orientation='h',
    name='Perda de Empregos',
    marker_color='rgba(200, 50, 80, 1)'
))

fig2.update_layout(
    title={
        'text': 'Relação entre Adoção de IA e Perda de Empregos por Setor',
        'font_size': 16,
        'x': 0.5,
        'xanchor': 'center'
    },
    xaxis_title='Porcentagem (%)',
    yaxis_title='Setores',
    font=dict(
        color="white",
        family="Arial",
        size=10
    ),
    xaxis_range=[0, 100],
    height=300,            
    width=600,   
    barmode='group',
    plot_bgcolor='rgba(0, 0, 0, 0)',
    paper_bgcolor='rgba(20, 20, 30, 1)',
    legend=dict(
        orientation='h',
        y=-0.5,
        x=-0.1
    )
)


analise3 = dados.groupby('Country')[['AI Adoption Rate (%)']].mean()

fig3 = px.bar(
    x=analise3['AI Adoption Rate (%)'],
    y=analise3.index,
    orientation='h',
    title='Média de Adoção de IA por País',
    color_discrete_sequence=['orange']
)

fig3.update_layout(
    xaxis_range=[0,100],
    height=300,            
    width=600,            
    xaxis_title='Taxa de Adoção de IA (%)',
    yaxis_title='',
    font=dict(
        color="white", 
        family="Arial",
        size=13
    ),
    plot_bgcolor='rgba(0, 0, 0, 0)',
    paper_bgcolor='rgba(20, 20, 30, 1)'
)


analise4 = dados.groupby(['Year', 'Industry'])['Job Loss Due to AI (%)'].mean().reset_index()

serie_temporal1 = analise4.pivot(index='Year', columns='Industry', values='Job Loss Due to AI (%)')

def fig4(setores):
    grafico = go.Figure()
    if len(setores) < 1:
        setores = ['Healthcare']
    colors = ['red', 'lightcoral', 'darkred', 'firebrick', 'indianred']

    cont = 0
    for i in range(len(setores)):
        grafico.add_trace(go.Scatter(
            x=serie_temporal1.reset_index()['Year'],
            y=serie_temporal1[setores[cont]],
            name=setores[i],
            line=dict(color=colors[cont], width=4)
        )) 
        cont+=1

    grafico.update_layout(
        yaxis_range=[0,100],
        title={
            'text': 'Serie Temporal de Empregos Perdidos para IA por Setor',
            'x': 0.5,
            'xanchor': 'center'
        },
        height=300,            
        width=600,            
        font=dict(
            color="white", 
            family="Arial",
            size=13
        ),
        plot_bgcolor='rgba(0, 0, 0, 0)',
        paper_bgcolor='rgba(20, 20, 30, 1)',
        legend=dict(
            orientation='h',
            y=-0.5,
            x=0
        )
    )

    return grafico


serie_temporal2 = dados.groupby(['Country', 'Year'])[['AI Adoption Rate (%)', 'Revenue Increase Due to AI (%)', 'Market Share of AI Companies (%)']].mean()



def fig5(pais):
    grafico = go.Figure()
    
    grafico.add_trace(go.Scatter(
        x=serie_temporal2.loc[pais].index,
        y=serie_temporal2.loc[pais]['AI Adoption Rate (%)'],
        name='Adoção de IA (%)',
        line=dict(color='royalblue', width=4)
    ))

    grafico.add_trace(go.Scatter(
        x=serie_temporal2.loc[pais].index,
        y=serie_temporal2.loc[pais]['Market Share of AI Companies (%)'],
        name='Participação de Empresas de IA no Mercado (%)',
        line=dict(color='red', width=4)
    ))

    grafico.add_trace(go.Scatter(
        x=serie_temporal2.loc[pais].index,
        y=serie_temporal2.loc[pais]['Revenue Increase Due to AI (%)'],
        name='Aumento de Receita por Conta da IA (%)',
        line=dict(color='orange', width=4)
    ))

    grafico.update_layout(
        yaxis_range=[0,100],
        title={
            'text': 'Série Temporal Relação Adoção de IA, Aumento de<br>Receita e Participação de Empresas de IA por País',
            'x': 0.5,
            'xanchor': 'center'
        },
        title_font_size=14, 
        height=300,            
        width=600,           
        font=dict(
            color='white', 
            family='Arial',
            size=11
        ),
        plot_bgcolor='rgba(0, 0, 0, 0)',
        paper_bgcolor='rgba(20, 20, 30, 1)',
        legend=dict(
            orientation='h',
            y=-0.5,
            x=0
        )
    )
    
    return grafico



serie_temporal3 = dados.groupby(['Industry', 'Year'])[['AI Adoption Rate (%)', 'Revenue Increase Due to AI (%)', 'Market Share of AI Companies (%)']].mean()

def fig6(setor):
    grafico = go.Figure()

    grafico.add_trace(go.Scatter(
        x=serie_temporal3.loc[setor].reset_index()['Year'],
        y=serie_temporal3.loc[setor]['AI Adoption Rate (%)'],
        name='Adoção de IA (%)',
        line=dict(color='royalblue', width=4)
    ))

    grafico.add_trace(go.Scatter(
        x=serie_temporal3.loc[setor].reset_index()['Year'],
        y=serie_temporal3.loc[setor]['Market Share of AI Companies (%)'],
        name='Participação de Empresas de IA no Mercado (%)',
        line=dict(color='red', width=4)
    ))

    grafico.add_trace(go.Scatter(
        x=serie_temporal3.loc[setor].reset_index()['Year'],
        y=serie_temporal3.loc[setor]['Revenue Increase Due to AI (%)'],
        name='Aumento de Receita por Conta da IA (%)',
        line=dict(color='orange', width=4)
    ))

    grafico.update_layout(
        yaxis_range=[0,100],
        title={
            'text': f'Série Temporal Relação Adoção de IA, Aumento de<br>Receita e Participação de Empresas de IA ({setor})',
            'x': 0.5,
            'xanchor': 'center'
        },
        title_font_size=14, 
        height=300,            
        width=600,            
        font=dict(
            color='white', 
            family='Arial',
            size=11
        ),
        plot_bgcolor='rgba(0, 0, 0, 0)',
        paper_bgcolor='rgba(20, 20, 30, 1)',
        legend=dict(
            orientation='h',
            y=-0.5,
            x=0
        )
    )

    return grafico

analise6 = dados.groupby('Country')[['Job Loss Due to AI (%)', 'Human-AI Collaboration Rate (%)']].mean()

fig7 = go.Figure()

fig7.add_trace(go.Bar(
    x=analise6.index,
    y=analise6['Human-AI Collaboration Rate (%)'],
    orientation='v',
    name='Colaboração Humano-IA',
    marker_color='lightgreen'
))

fig7.add_trace(go.Bar(
    x=analise6.index,
    y=analise6['Job Loss Due to AI (%)'],
    orientation='v',
    name='Perca de Emprego para IA',
    marker_color='indianred'
))

fig7.update_layout(
    title='Relação Colaboração Humano-IA com Perca de Empregos por País',
    title_font_size=14.5,
    yaxis_range=[0,100],
    yaxis_title='Porcentagem (%)',
    height=300,            
    width=600,            
    font=dict(
        color="white", 
        family="Arial",
        size=11
    ),
    legend=dict(
        orientation='h',
        y=-0.5,
        x=0
    ),
    plot_bgcolor='rgba(0, 0, 0, 0)',
    paper_bgcolor='rgba(20, 20, 30, 1)'
)


analise7 = dados.groupby(['Country', 'Year'])[['Job Loss Due to AI (%)']].mean().reset_index()

serie_temporal4 = analise7.pivot(index='Year', columns='Country', values='Job Loss Due to AI (%)')

def fig8(paises):
    grafico = go.Figure()

    if len(paises) < 1:
        paises = ['UK']

    colors = ['red', 'lightcoral', 'darkred', 'firebrick', 'indianred']

    cont = 0
    for i in range(len(paises)):
        grafico.add_trace(go.Scatter(
            x=serie_temporal4.reset_index()['Year'],
            y=serie_temporal4[paises[cont]],
            name=paises[i],
            line=dict(color=colors[cont], width=4)
        )) 
        cont+=1

    grafico.update_layout(
        yaxis_range=[0,100],
        title={
            'text': 'Serie Temporal de Empregos Perdidos para IA por País',
            'x': 0.5,
            'xanchor': 'center'
        },
        height=300,            
        width=600,            
        font=dict(
            color="white", 
            family="Arial",
            size=13
        ),
        plot_bgcolor='rgba(0, 0, 0, 0)',
        paper_bgcolor='rgba(20, 20, 30, 1)',
        legend=dict(
            orientation='h',
            y=-0.5,
            x=0
        )
    )

    return grafico