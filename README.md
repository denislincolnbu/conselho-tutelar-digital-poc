# 🛡️ Conselho Tutelar Digital - Prova de Conceito (PoC)

> **Projeto de Extensão Curricularizada em Tecnologia — UniFECAF (2026)**  
> **Tema:** Segurança, Infraestrutura e Confiabilidade para Instituições Sociais  
> **Instituição Parceira:** II Conselho Tutelar de Embu das Artes – SP  
> **Autor:** Denis Lincoln Cardoso Dias  

---

## 📌 Sobre o Projeto

Este repositório contém a Prova de Conceito (PoC) desenvolvida para demonstrar a modernização da gestão de prontuários e a mitigação de riscos de perda de dados no **II Conselho Tutelar de Embu das Artes**.

A solução propõe a substituição de um banco de dados local legado em Microsoft Access por uma arquitetura relacional centralizada em **SQLite** com interface web responsiva em **Streamlit**, permitindo buscas unificadas de assistidos em milissegundos e simulação de rotinas de backup e resiliência em nuvem.

> ⚠️ **Nota de Governança e LGPD/ECA:** Todos os nomes, prontuários e registros presentes neste código e base de dados são **100% fictícios**, criados estritamente para simulação acadêmica e validação de usabilidade, garantindo total conformidade com a Lei Geral de Proteção de Dados (LGPD) e o Estatuto da Criança e do Adolescente (ECA).

---

## 🛠️ Tecnologias Utilizadas

- **Linguagem:** Python 3.14+
- **Interface Web:** [Streamlit](https://streamlit.io/)
- **Manipulação de Dados:** [Pandas](https://pandas.pydata.org/)
- **Banco de Dados Relacional:** SQLite 3
- **Ambiente de Desenvolvimento:** Visual Studio Code (VS Code)

---

## 🚀 Funcionalidades Principais

1. **🔍 Busca Unificada de Assistidos:** Consulta instantânea por nome ou sobrenome com junção relacional (`LEFT JOIN`) entre menores e histórico de prontuários.
2. **💾 Módulo de Governança e Backup:** Simulação automatizada de exportação e sincronização da base de dados local para ambiente resiliente em nuvem.
3. **👤 Perfil Autenticado:** Painel lateral com identificação do conselheiro logado e selo de conformidade com criptografia/LGPD.

---

## ⚙️ Como Executar o Projeto Localmente

### Pré-requisitos
- Python instalado (versão 3.10 ou superior)
- Git instalado

### Passo a Passo

1. **Clone o repositório:**
   ```bash
   git clone https://github.com/denislincolnbu/conselho-tutelar-digital-poc