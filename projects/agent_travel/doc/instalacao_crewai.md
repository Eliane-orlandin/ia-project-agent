# Guia de Instalação e Uso do CrewAI

Este guia mostra como instalar e configurar o CrewAI, uma ferramenta para criação de agentes de IA colaborativos.

---

## 1. Instalar o Python

### Requisitos de Versão

O **CrewAI** requer **Python >= 3.10 e < 3.13**.  
Para verificar sua versão:

```bash
python3 --version
```

---

## 2. Instalar o `uv`

Ferramenta utilizada para instalar o CrewAI.

### Usando `curl`:

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

### Ou usando `wget`:

```bash
wget -qO- https://astral.sh/uv/install.sh | sh
```

---

## 3. Instalar o CrewAI

Instale a CLI do CrewAI com:

```bash
uv tool install crewai
```

Verifique se foi instalado corretamente:

```bash
uv tool list
```

Saída esperada:

```text
crewai v0.102.0
- crewai
```

### Atualizar o CrewAI

```bash
uv tool install crewai --upgrade
```

---

## 4. Criar um Projeto CrewAI

Gere a estrutura do projeto com:

```bash
crewai create crew <your_project_name>
```

Estrutura gerada:

```
<your_project_name>/
├── .gitignore
├── knowledge/
├── pyproject.toml
├── README.md
├── .env
└── src/
    └── <your_project_name>/
        ├── __init__.py
        ├── main.py
        ├── crew.py
        ├── tools/
        │   ├── custom_tool.py
        │   └── __init__.py
        └── config/
            ├── agents.yaml
            └── tasks.yaml
```

---

## 5. Personalize Seu Projeto

### Arquivos Essenciais

| Arquivo       | Função                                                     |
| ------------- | ---------------------------------------------------------- |
| `agents.yaml` | Define os agentes e suas funções                           |
| `tasks.yaml`  | Define as tarefas e a ordem de execução                    |
| `.env`        | Armazena variáveis de ambiente e chaves de API             |
| `main.py`     | Ponto de entrada principal da aplicação                    |
| `crew.py`     | Lógica de orquestração da equipe                           |
| `tools/`      | Ferramentas auxiliares para os agentes                     |
| `knowledge/`  | Base de conhecimento do projeto (documentos, textos, etc.) |

> Mantenha chaves e informações confidenciais no arquivo `.env`

---

## 6. Executar o Projeto

Instale as dependências com:

```bash
crewai install
```

Execute sua equipe com:

```bash
crewai run
```

```


```
