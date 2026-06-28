# IA Project Agent

Este repositório é dedicado ao estudo, desenvolvimento e experimentação com agentes de Inteligência Artificial utilizando diferentes frameworks e bibliotecas.

## 📁 Estrutura do Repositório

A estrutura é dividida entre projetos de estudo/tutoriais e projetos práticos baseados em casos de uso.

```text
IA-Project-Agent/
├── projects/          # Agentes focados em casos de uso práticos e negócios
│   ├── agent_real_state/  # Agente para recomendação de imóveis
│   └── agent_travel/      # Agente para planejamento de viagens
└── tutorials/         # Estudos e tutoriais focados em frameworks específicos
    ├── crew_ai/           # Experimentos com CrewAI
    ├── langchain/         # Experimentos com LangChain
    └── llamaindex/        # Experimentos com LlamaIndex
```

---

## 🛠️ Tecnologias e Frameworks Utilizados

*   **LlamaIndex:** Framework para conectar fontes de dados privadas com LLMs e construir fluxos RAG e agentes.
*   **LangChain:** Ecossistema para orquestração e desenvolvimento de aplicações baseadas em modelos de linguagem.
*   **CrewAI:** Orquestração de agentes de IA autônomos e colaborativos.
*   **Python & Jupyter Notebooks:** Utilizados para experimentação rápida e visualização de dados.

---

## 🚀 Como Rodar os Projetos

Cada subdiretório possui seu próprio ambiente virtual independente para evitar conflito de dependências.

1. Navegue até o diretório do projeto desejado:
   ```bash
   cd tutorials/llamaindex
   ```

2. Ative o ambiente virtual correspondente:
   * **macOS/Linux:**
     ```bash
     source .venv/bin/activate
     ```
   * **Windows:**
     ```bash
     .venv\Scripts\activate
     ```

3. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```

4. Configure as variáveis de ambiente necessárias copiando o arquivo `.env.example` (ou configurando o `.env` existente com suas chaves de API, ex: `OPENAI_API_KEY`, `GEMINI_API_KEY`).
