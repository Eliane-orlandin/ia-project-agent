#  Projeto `llamaindex_agents`

Este projeto demonstra a criação e uso de **agentes inteligentes** com a biblioteca [LlamaIndex](https://llamaindex.ai), integrando modelos LLM (como o LLaMA 3.3 da Groq) para executar tarefas de:

- Cálculo de imposto de renda
- Consulta a artigos científicos (arXiv e Tavily)
- Leitura e indexação de documentos PDF locais
- Busca semântica com agentes especializados

> 🔗 Repositório no GitHub:  
> [github.com/Eliane-orlandin/IA-Project-Agent](https://github.com/Eliane-orlandin/IA-Project-Agent.git/)

---

##  Estrutura do Projeto

```
llamaindex_agents/
├── agent_functions.ipynb     # Código principal com todos os exemplos didáticos
├── requirements.txt          # Dependências do projeto
├── .gitignore                # Arquivos ignorados pelo Git
└── files/
    ├── LLM.pdf               # Documento sobre LLMs
    └── LLM_2.pdf             # Tutorial ou aplicação prática com LLMs
```

---

##  Funcionalidades Demonstradas

###  Cálculo de Imposto de Renda com Agente
Função Python transformada em ferramenta para um agente interativo.

###  Busca de Artigos Científicos
- `arXiv`: via biblioteca `arxiv`
- `Tavily`: via API externa para resultados atualizados

###  Indexação e Consulta de Documentos PDF
Os arquivos `LLM.pdf` e `LLM_2.pdf` são carregados, vetorizados com embeddings HuggingFace e usados em agentes de busca com perguntas naturais.

###  Agentes LLM Inteligentes
- `FunctionCallingAgentWorker`: para execução de funções específicas
- `ReActAgent`: para raciocínio e uso contextual de ferramentas

---

##  ▶Como Executar

### 1. Clone o repositório
```bash
git clone https://github.com/Eliane-orlandin/IA-Project-Agent.git
cd IA-Project-Agent/llamaindex_agents
```

### 2. Crie e ative um ambiente virtual (recomendado)
```bash
python -m venv venv
source venv/bin/activate  # no Linux/Mac
venv\Scripts\activate     # no Windows
```

### 3. Instale as dependências
```bash
pip install -r requirements.txt
```

### 4. Configure suas chaves de API
Crie um arquivo `.env` com:

```env
GROQ_API_KEY=YOUR_GROQ_KEY
TAVILY_API_KEY=YOUR_TAVILY_KEY
```

>  Recomendado usar `python-dotenv` para carregar automaticamente as variáveis de ambiente.

---

## Requisitos Técnicos

- Python v3.12.4
- API Key da [Groq](https://console.groq.com/)
- API Key da [Tavily](https://www.tavily.com/)
- Dependências do `requirements.txt`

---

## Créditos

Projeto desenvolvido por **Eliane Orlandin**  
Curso : [Crie Rápido Agentes de IA Do Zero ao Avançado - AI Agents](https://www.udemy.com/share/10cMTx3@tVP1o3FZyfERIEE68ee_fWFcC7M5ksmipwiGa9Gpti8w09Xkr2fwd_dXJSj_sfligA==/)

GitHub: [@Eliane-orlandin](https://github.com/Eliane-orlandin)

LinkdIn [@Eliane-orlandin](https://www.linkedin.com/in/eliane-orlandin-do-carmo-551b92246/)



