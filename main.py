import streamlit as st
import pandas as pd

st.set_page_config(page_title="Finanças", page_icon="💰")

st.markdown("""
#  Boas Vindas!
            
## Nosso APP Financeiro!  

Espero que você curta a experiencia da nossa solução para organização financeira pessoal!
                                  
""")

file_upload = st.file_uploader(label="Faça o upload dos dados aqui", type=["csv", "xlsx", "xls"])

# Verifica se existe um arquivo carregado
if file_upload:

    df = pd.read_csv(file_upload)
    df["Data"] = pd.to_datetime(df["Data"], format="%d/%m/%Y").dt.date

    # Exibição dos dados
    expl = st.expander("Veja os dados brutos carregados")
    columns_fmt = {"Valor": st.column_config.NumberColumn("Valor", format="R$ %f")}
    expl.dataframe(df, hide_index=True, column_config=columns_fmt)

    exp2 = st.expander("Instituições")
    df_instituicao = df.pivot_table(index="Data", columns="Instituição", values="Valor")

    # abas para diferentes visualizações
    tab_data, tab_history, tab_share = exp2.tabs(["Dados", "Histórico", "Distribuição"])       

    with tab_data:
        st.dataframe(df_instituicao)
    
    with tab_history:
        st.line_chart(df_instituicao)
    
    with tab_share:

        date = st.selectbox("Filtro de data", options=df_instituicao.index) 
             
        # obtem a ultimda data de graficos
        st.bar_chart(df_instituicao.loc[date])  