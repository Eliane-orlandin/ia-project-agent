# LangChain Tutorial

Este diretório contém notebooks de estudo e tutoriais práticos focados no uso do framework **LangChain** para integração com modelos de linguagem.

## 📁 Conteúdo

O tutorial é estruturado nos seguintes tópicos:

*   **[1-models.ipynb](file:///Users/elianeorlandin/Documents/Desenvolvimento/IA-Project-Agent/tutorials/langchain/1-models.ipynb):** Introdução ao uso de LLMs com LangChain. Demonstração de invocação básica de modelos (ex: OpenAI GPT), execução síncrona e streaming de respostas.
*   **[2-prompt_template.ipynb](file:///Users/elianeorlandin/Documents/Desenvolvimento/IA-Project-Agent/tutorials/langchain/2-prompt_template.ipynb):** Utilização de `PromptTemplate` para parametrizar e estruturar prompts dinamicamente de forma eficiente e reutilizável.

---

## 🚀 Como Iniciar

1. Certifique-se de estar com o ambiente virtual ativado:
   ```bash
   source .venv/bin/activate
   ```
2. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```
3. Crie ou configure o arquivo `.env` na raiz do diretório do tutorial com a sua chave de API:
   ```env
   OPENAI_API_KEY=sua-chave-aqui
   ```
4. Abra e execute os notebooks usando sua IDE ou subindo o Jupyter:
   ```bash
   jupyter notebook
   ```
