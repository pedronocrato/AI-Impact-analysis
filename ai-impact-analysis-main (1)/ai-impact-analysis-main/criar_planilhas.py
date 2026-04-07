import pandas as pd
import os

def criar_planilha():
    
    dados = pd.read_csv("Global_AI_Content_Impact_Dataset.csv")
    # dados.to_excel("Global_AI_Content_Impact_Dataset.xlsx", index=False)
    
    df = pd.DataFrame(dados)

    return df

tabela = criar_planilha()




