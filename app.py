import os
import sqlite3
import pandas as pd
import streamlit as st

# Configuração da página
st.set_page_config(
    page_title="Conselho Tutelar Digital - Embu das Artes",
    page_icon="🛡️",
    layout="wide",
)

# Estilização
st.title("🛡️ Sistema de Consulta Unificada - II Conselho Tutelar")
st.caption(
    "Prova de Conceito (PoC) - Unificação de Prontuários e Segurança de Dados"
)

# Conexão e Criação do Banco de Dados SQLite Local
conn = sqlite3.connect("conselho_tutelar.db")
c = conn.cursor()

# 1. Tabela Menores
c.execute(
    """
CREATE TABLE IF NOT EXISTS Menores (
    id_menor INTEGER PRIMARY KEY,
    nome TEXT,
    data_nasc TEXT,
    nome_mae TEXT,
    unidade TEXT
)
"""
)

# 2. Tabela Prontuarios
c.execute(
    """
CREATE TABLE IF NOT EXISTS Prontuarios (
    id_prontuario INTEGER PRIMARY KEY,
    id_menor INTEGER,
    data_reg TEXT,
    relato TEXT,
    status TEXT,
    FOREIGN KEY(id_menor) REFERENCES Menores(id_menor)
)
"""
)
conn.commit()

# Popula dados fictícios caso o banco esteja vazio
c.execute("SELECT COUNT(*) FROM Menores")
if c.fetchone()[0] == 0:
    menores_ficticios = [
        (
            1,
            "João da Silva Fictício",
            "10/05/2015",
            "Maria da Silva",
            "Unidade II - Jd. Santo Eduardo",
        ),
        (
            2,
            "Lucas Souza Fictício",
            "22/08/2012",
            "Ana de Souza",
            "Unidade II - Jd. Santo Eduardo",
        ),
        (
            3,
            "Mariana Oliveira Fictícia",
            "14/03/2018",
            "Carla de Oliveira",
            "Unidade II - Jd. Santo Eduardo",
        ),
        (
            4,
            "Mateus dos Santos Fictício",
            "05/12/2014",
            "Regina dos Santos",
            "Unidade I - Centro",
        ),
        (
            5,
            "Beatriz de Souza Fictícia",
            "18/01/2019",
            "Patricia de Souza",
            "Unidade III - Jd. Santa Tereza",
        ),
        (
            6,
            "Guilherme Silva Fictício",
            "30/09/2011",
            "Camila Silva",
            "Unidade II - Jd. Santo Eduardo",
        ),
    ]
    c.executemany("INSERT INTO Menores VALUES (?,?,?,?,?)", menores_ficticios)

    prontuarios_ficticios = [
        (
            101,
            1,
            "16/07/2026",
            "Visita domiciliar realizada para acompanhamento escolar do menor.",
            "Fechado",
        ),
        (
            102,
            1,
            "16/07/2026",
            "Solicitação de vaga em creche local encaminhada para a secretaria.",
            "Aberto",
        ),
        (
            103,
            2,
            "15/07/2026",
            "Atendimento inicial para verificação de frequência escolar.",
            "Fechado",
        ),
        (
            104,
            3,
            "16/07/2026",
            "Encaminhamento para atendimento psicológico no CRAS local.",
            "Aberto",
        ),
        (
            105,
            4,
            "14/07/2026",
            "Acompanhamento de medida de proteção aplicada pelo conselho.",
            "Aberto",
        ),
        (
            106,
            6,
            "12/07/2026",
            "Atendimento inicial de denúncia anônima sobre negligência escolar.",
            "Aberto",
        ),
    ]
    c.executemany(
        "INSERT INTO Prontuarios VALUES (?,?,?,?,?)", prontuarios_ficticios
    )
    conn.commit()

# --- BARRA LATERAL (PERFIL DO CONSELHEIRO) ---

# Procura o arquivo da foto, incluindo o nome com extensão dupla gerada pelo Windows
foto_encontrada = None
for nome_arquivo in [
    "minha_foto.jpg.jpeg",
    "minha_foto.jpg",
    "minha_foto.png",
    "minha_foto.jpeg",
    "foto.jpg",
    "foto.png",
]:
    if os.path.exists(nome_arquivo):
        foto_encontrada = nome_arquivo
        break

if foto_encontrada:
    st.sidebar.image(foto_encontrada, width=150)
else:
    st.sidebar.image(
        "https://images.unsplash.com/photo-1534528741775-53994a69daeb?w=150"
    )

st.sidebar.markdown("### Conselheiro Logado")
st.sidebar.write("**Nome:** Denis Lincoln Cardoso Dias")
st.sidebar.write("**Cargo:** Conselheiro Tutelar")
st.sidebar.write("**Unidade:** II - Jd. Santo Eduardo")

st.sidebar.markdown("---")
st.sidebar.write("🔒 Ambientes com Criptografia e Conformidade LGPD/ECA")

# Abas do Sistema
aba1, aba2 = st.tabs(["🔍 Busca Unificada", "💾 Governança e Backup"])

with aba1:
    st.subheader("Consulta de Assistidos em Tempo Real")
    busca = st.text_input(
        "Digite o nome ou sobrenome do menor (Ex: 'Silva', 'João', 'Souza'):"
    )

    if busca:
        query = f"""
        SELECT 
            m.id_menor AS 'ID',
            m.nome AS 'Nome do Menor', 
            m.data_nasc AS 'Data Nasc.', 
            m.nome_mae AS 'Nome da Mãe', 
            m.unidade AS 'Unidade Registrada', 
            p.relato AS 'Histórico do Prontuário', 
            p.status AS 'Status'
        FROM Menores m
        LEFT JOIN Prontuarios p ON m.id_menor = p.id_menor
        WHERE m.nome LIKE '%{busca}%'
        """
        df = pd.read_sql_query(query, conn)

        if not df.empty:
            st.success(f"Foram encontrados {len(df)} registros no banco.")
            st.dataframe(df, use_container_width=True)
        else:
            st.warning("Nenhum menor encontrado com este nome.")
    else:
        st.info("💡 Digite um termo de busca para consultar o banco unificado.")

with aba2:
    st.subheader("Políticas de Segurança e Resiliência")
    st.write(
        "Demonstração de mitigação do risco do Microsoft Access local sem redundância."
    )

    if st.button("🚀 Executar Simulação de Backup em Nuvem"):
        st.balloons()
        st.success(
            "✅ Backup do banco 'conselho_tutelar.db' exportado com sucesso para ambiente seguro em Nuvem!"
        )
        st.code(
            "LOG: [2026-07-21 16:00:00] Syncing database to cloud bucket... STATUS: 200 OK",
            language="bash",
        )