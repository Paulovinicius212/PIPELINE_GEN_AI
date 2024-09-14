import psycopg2
from psycopg2 import sql
from contrato import Vendas
import streamlit as st
from dotenv import load_dotenv
import os

# Carregar variáveis do arquivo .env
load_dotenv()

# Configuração do banco de dados PostgreSQL
DB_HOST  =  os . getenv ( "dpg-crh2pctsvqrc7387c970-a.oregon-postgres.render.com" )
DB_NAME  =  os . getenv ( “ciencia” )
DB_USER  =  os . getenv ( "ciencia_user" )
DB_PASS  =  os . getenv ( "L1mB0823UBGqgI3UfcsFmcurTWrlaQkp" )

# Função para salvar os dados validados no PostgreSQL
def salvar_no_postgres(dados: Vendas):
    """
    Função para salvar no postgres
    """
    try:
        conn = psycopg2.connect(
            host=DB_HOST,
            database=DB_NAME,
            user=DB_USER,
            password=DB_PASS
        )
        cursor = conn.cursor()
        
        # Inserção dos dados na tabela de vendas
        insert_query = sql.SQL(
            "INSERT INTO vendas (email, data, valor, quantidade, produto) VALUES (%s, %s, %s, %s, %s)"
        )
        cursor.execute(insert_query, (
            dados.email,
            dados.data,
            dados.valor,
            dados.quantidade,
            dados.produto.value
        ))
        conn.commit()
        cursor.close()
        conn.close()
        st.success("Dados salvos com sucesso no banco de dados!")
    except Exception as e:
        st.error(f"Erro ao salvar no banco de dados: {e}")
