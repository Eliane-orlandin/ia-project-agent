# Consultoria Imobiliária com Agentes de IA

Este projeto simula uma **consultoria imobiliária automatizada** baseada em agentes autônomos que colaboram entre si para entregar uma análise completa ao cliente, considerando imóveis disponíveis, tendências de mercado, notícias econômicas e opções de financiamento.

>  Projeto desenvolvido para fins de aprendizado utilizando **Python**, **LangChain** e **CrewAI**.

---

##  Objetivo Geral

Oferecer uma experiência simulada de consultoria imobiliária inteligente, com recomendações personalizadas de imóveis, análise de tendências e sugestões financeiras com base no perfil do cliente.

---

##  Arquitetura de Agentes (Crew)

O sistema é organizado por um **Crew** de agentes, onde cada agente desempenha uma função específica:

### 1.  Corretor de Imóveis
- Obtém as preferências do cliente (tipo, cidade, preço).
- Filtra imóveis compatíveis usando o arquivo `imoveis.csv` com a ferramenta `CSVSearchTool`.

### 2.  Analista de Mercado Imobiliário
- Analisa a tendência de preços (valorização, queda ou estabilidade) com a `TendenciaPrecosImoveisTool`.

### 3.  Analista de Notícias Imobiliárias
- Busca notícias econômicas recentes sobre o setor imobiliário com `DuckDuckGoSearchResults`.

### 4.  Consultor Financeiro
- Analisa a renda do cliente e sugere opções de financiamento adequadas (sem uso de APIs externas).

### 5.  Redator de Relatórios
- Gera um relatório final estruturado e persuasivo com base nas análises dos demais agentes.

---

### Formato da Entrada
A aplicação espera um JSON com as seguintes chaves:
```
{
  "cidade": "Rio de Janeiro",
  "tipo_imovel": "Apartamento",
  "faixa_preco": "500000-700000"
}
```
- cidade: Nome da cidade (ex: "Rio de Janeiro")
- tipo_imovel: Tipo do imóvel (ex: "Apartamento", "Casa")
- faixa_preco: Intervalo de valores no formato "minimo-maximo" (ex: "500000-700000")

---

##  Tecnologias Utilizadas

* Python 3.12.4
* LangChain
* Jupyter Notebook
* Ferramentas customizadas (`CSVSearchTool`, `TendenciaPrecosImoveisTool`, `DuckDuckGoSearchResults`)
* Dados simulados em arquivo `.csv`

---

##  Estrutura do Projeto

```
Agent_Real_State/
├── files/
    └──imoveis.csv
├── .gitignore
├── imoveis.csv
├── recomendacao_imoveis.ipynb
├── requirements.txt
└── README.md
```

---

##  Como Executar Localmente

### 1. Clone o repositório

```bash
git clone https://github.com/Eliane-orlandin/IA-Project-Agent.git
cd IA-Project-Agent/agent_real_state
```

### 2. Crie um ambiente virtual e ative

```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows
```

### 3. Instale as dependências

```bash
pip install -r requirements.txt
```

### 4. Execute o projeto

```bash
jupyter notebook
```

Abra o arquivo `recomendacao_imoveis.ipynb` em um Jupyter Notebook e siga as instruções para iniciar a simulação dos agentes.

---

##  Observações

* O projeto é **didático e simulado**, com dados fictícios.
* Não há integração real com APIs de instituições financeiras ou imobiliárias.
* Pode ser adaptado para fins reais, conectando com APIs externas e fontes de dados públicas.

---

##  Licença

Este projeto é disponibilizado sob a licença MIT. Sinta-se livre para estudar, modificar e reutilizar para fins educacionais ou pessoais.

---

Feito por [Eliane Orlandin](https://github.com/Eliane-orlandin)
          [LinkedIn](https://www.linkedin.com/in/eliane-orlandin-do-carmo-551b92246/)
