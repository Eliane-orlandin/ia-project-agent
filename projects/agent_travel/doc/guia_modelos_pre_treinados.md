# Acessando Modelos Pré-Treinados

## Usando a OpenAI

### Passo a passo para configurar sua conta e obter uma chave de API:

1. **Criar uma conta na OpenAI**
   Acesse: [https://platform.openai.com/docs/overview](https://platform.openai.com/docs/overview)

2. **Configurar o faturamento (Billing):**
   Vá até **Settings > Organization > Billing** e adicione um valor (mínimo de **US\$5**).

3. **Gerar uma chave de API:**

   - Acesse **API Keys**
   - Clique em **+ Create new secret key**
   - Preencha os campos:

     - **Owned by**: (You)
     - **Name**: `<nome_do_projeto>`
     - **Project**: (default project)
     - **Permissions**: All

   - Clique em **Create secret key**
   - **Importante:** Copie e salve a chave em um local seguro (ex: Bloco de Notas).
     Você **não poderá visualizá-la novamente**. Se perder, será necessário criar uma nova.

---

## Usando Modelos Pré-Treinados Localmente (Ollama)

### Instalar e rodar modelos com o [Ollama](https://ollama.com/)

1. **Baixar o Ollama**
   Acesse: [https://ollama.com/](https://ollama.com/)
   Faça o download e a instalação.

2. **Escolher e baixar um modelo**
   Exemplo: `llama3:2b`
   No terminal, execute:

   ```bash
   ollama run llama3:2b
   ```

3. **Comandos úteis no terminal:**

#### Comandos gerais

```
/?               Exibe ajuda geral
/help            Ajuda para comandos
/bye             Sair da sessão
/clear           Limpa o contexto da sessão
/set             Define variáveis de sessão
/show            Mostra informações do modelo
/load <modelo>   Carrega modelo ou sessão
/save <modelo>   Salva a sessão atual
```

#### Comandos para exibir informações

```
/show info           Detalhes do modelo
/show license        Licença do modelo
/show modelfile      Modelfile usado
/show parameters     Parâmetros do modelo
/show system         Mensagem do sistema
/show template       Template do prompt
```

#### Comandos Ollama

```
ollama serve       Inicia o servidor Ollama
ollama create      Cria um modelo a partir de um Modelfile
ollama show        Mostra informações de um modelo
ollama run         Executa um modelo
ollama stop        Interrompe um modelo em execução
ollama pull        Baixa um modelo do repositório
ollama push        Envia um modelo para o repositório
ollama list        Lista os modelos disponíveis
ollama ps          Mostra modelos em execução
ollama cp          Copia um modelo
ollama rm          Remove um modelo
ollama help        Ajuda sobre comandos
```

4. **Parar a execução do modelo (importante!)**

```bash
ollama stop llama3:2b
```
