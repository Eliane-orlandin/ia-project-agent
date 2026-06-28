# 🧠 Análise Automatizada de Mercado com CrewAI

Este projeto utiliza a biblioteca [CrewAI](https://github.com/joaomdmoura/crewAI) para simular uma equipe de agentes autônomos que colaboram para realizar uma análise de mercado completa, automatizada e personalizada com base em um setor específico.

## 📌 Objetivo

Automatizar a **coleta**, **análise** e **elaboração de relatórios** de mercado sobre um setor definido pelo usuário.
O projeto cria uma equipe com três agentes que trabalham em sequência:

1. **Pesquisador de Mercado:** Coleta dados atualizados sobre o setor.
2. **Analista de Tendências:** Analisa os dados coletados e identifica padrões, oportunidades e ameaças.
3. **Redator de Relatórios:** Gera um relatório final estruturado, com resumo executivo e recomendações.

## 🛠️ Tecnologias Utilizadas

- Python 3.10+
- [CrewAI](https://pypi.org/project/crewai/)
- [python-dotenv](https://pypi.org/project/python-dotenv/)
- [IPython (para exibição em Jupyter Notebook)](https://pypi.org/project/ipython/)
- [Markdown](https://pypi.org/project/Markdown/) (opcional, para salvar em HTML)
- [pdfkit](https://pypi.org/project/pdfkit/) (opcional, para conversão posterior)

## 📁 Estrutura do Projeto

```text
IA-Project-Agent/
│
├── crew_ai/                    # Diretório principal do projeto
│   └── main.py                 # Script principal com definição dos agentes e tarefas
│   └── README.md               # Este arquivo
│   └── requirements.txt        # Lista de dependências
```

## 📦 Instalação

Clone o repositório e instale as dependências:

```bash
git clone https://github.com/Eliane-orlandin/IA-Project-Agent.git
cd IA-Project-Agent/crew_ai
pip install -r ../requirements.txt
```

Crie um arquivo `.env` com suas variáveis (como chaves de API, se necessário):

```env
# Exemplo
OPENAI_API_KEY=sua_chave_aqui
```

## 🚀 Como Usar

> ⚠️ **Importante:** Recomendamos **executar o código em um Jupyter Notebook**, pois no VS Code o resultado pode ser truncado.

### 1. Execute a análise:

```python
resultado = crew.kickoff(inputs={"sector": "Inteligência Artificial"})
```

### 2. Exiba o relatório no Jupyter:

```python
from IPython.display import display, Markdown
display(Markdown(str(resultado)))
```

---

## 💾 Exportar o relatório

### ➤ Gerar um arquivo HTML

```python
import markdown

html = markdown.markdown(str(resultado))
with open("relatório.html", "w", encoding="utf-8") as file:
    file.write(html)
```

### ➤ Gerar um arquivo Markdown

```python
with open("relatório.md", "w", encoding="utf-8") as file:
    file.write(str(resultado))
```

> 💡 Você pode posteriormente converter o arquivo `.md` em PDF usando ferramentas como `pdfkit` ou `pandoc`.

---

## ✅ Exemplo de Saída

```markdown
# Relatório de Análise de Mercado: Inteligência Artificial

## Resumo Executivo

A Inteligência Artificial está em crescimento acelerado com aplicações em saúde, finanças, segurança e muito mais...

## Principais Tendências

- Adoção crescente de IA generativa
- Investimentos em IA explicável (XAI)
- Expansão de aplicações em edge computing

## Oportunidades e Recomendações

- Investir em soluções personalizadas por setor
- Explorar parcerias com startups de IA
```

---

## 📫 Contato

**Desenvolvido por:** Eliane Orlandin
**Repositório:** [IA-Project-Agent](https://github.com/Eliane-orlandin/IA-Project-Agent)
**LinkIn:**[Eliane Orlandin](https://www.linkedin.com/in/eliane-orlandin-do-carmo-551b92246/)
