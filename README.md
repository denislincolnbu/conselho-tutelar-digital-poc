# 🛡️ Conselho Tutelar Digital - Prova de Conceito (PoC)

> **Projeto de Extensão Curricularizada em Tecnologia — UniFECAF (2026)**  
> **Tema:** Segurança, Infraestrutura e Confiabilidade para Instituições Sociais  
> **Instituição Parceira:** II Conselho Tutelar de Embu das Artes – SP  
> **Autores:** Denis Lincoln Cardoso Dias & Jean Carlos Dos Santos Assunção  

---

## 📌 Sobre o Projeto

Este repositório contém o código-fonte da Prova de Conceito (PoC) desenvolvida para demonstrar a modernização da gestão de prontuários e a mitigação dos riscos de perda de dados no **II Conselho Tutelar de Embu das Artes**.

A solução substitui um banco de dados local obsoleto e sem redundância em **Microsoft Access** por uma arquitetura relacional centralizada em **SQLite** com interface web interativa em **Streamlit**. O sistema permite buscas unificadas por assistidos em milissegundos, simulação de backup resiliente em nuvem e alternância de perfis de conselheiros autorizados.

> ⚠️ **Nota de Governança, LGPD e ECA:** Todos os dados, prontuários e históricos cadastrados no código e na base de dados são **100% fictícios**, gerados estritamente para simulação e validação acadêmica. Nenhuma informação real de assistidos ou menores foi manipulada ou exposta, respeitando integralmente a Lei Geral de Proteção de Dados (LGPD) e o Estatuto da Criança e do Adolescente (ECA).

---

## 🛠️ Tecnologias Utilizadas

- **Linguagem:** Python 3.10+
- **Interface Web:** [Streamlit](https://streamlit.io/)
- **Manipulação e Análise de Dados:** [Pandas](https://pandas.pydata.org/)
- **Banco de Dados Relacional:** SQLite 3
- **Ambiente de Desenvolvimento:** Visual Studio Code (VS Code)
- **Versionamento:** Git / GitHub

---

## 🚀 Funcionalidades Demonstradas

1. **🔍 Busca Unificada em Tempo Real:** Consulta relacional (`LEFT JOIN`) por nome ou sobrenome com resposta em milissegundos.
2. **👤 Controle de Acesso Multi-Usuário:** Alternância dinâmica de perfil entre os conselheiros autorizados (Denis Lincoln e Jean Carlos).
3. **💾 Módulo de Governança e Resiliência (Backup):** Simulação de exportação e sincronização periódica do banco de dados relacional para ambiente seguro em nuvem.

---

## ⚙️ Como Executar o Projeto Localmente

### Pré-requisitos
- Python 3.10+ instalado
- Git instalado

### Passo a Passo

1. **Clone este repositório:**
   ```bash
   git clone [https://github.com/denislincolnbu/conselho-tutelar-digital-poc.git](https://github.com/denislincolnbu/conselho-tutelar-digital-poc.git)
   cd conselho-tutelar-digital-poc