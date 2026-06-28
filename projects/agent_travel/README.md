# Planejador de Viagens com CrewAI

Este projeto utiliza a biblioteca [CrewAI](https://docs.crewai.com/) para simular uma equipe autônoma de agentes de IA que colaboram para **planejar uma viagem completa pela Europa**, incluindo um roteiro diário e uma estimativa detalhada de orçamento.

## Visão Geral

O sistema é composto por dois agentes com papéis distintos:

- **Planejador de Viagem**: Responsável por montar um roteiro personalizado com base em destinos, transporte, hospedagem e atividades turísticas.
- **Orçamentista**: Estima os custos da viagem considerando todos os aspectos financeiros.

Esses agentes trabalham em sequência, coordenados por uma `Crew` com processo sequencial.

---

## Agentes Criados

### Planejador de Viagem

- **Função**: Criar roteiros detalhados com base em preferências e destinos.
- **Output esperado**: Lista de cidades, atividades, tipos de transporte e hospedagem.

### Orçamentista

- **Função**: Calcular o custo total da viagem com base no roteiro gerado.
- **Output esperado**: Estimativa de custos para cada item (transporte, hospedagem, atividades).

---

## Como usar

### Pré-requisitos

- Python 3.8+
- Biblioteca `crewai`
- Biblioteca `python-dotenv`
- Biblioteca `ipykernel`

### Instalação

```bash
pip install crewai python-dotenv ipykernel
```

### Executar

1. Crie um arquivo `.env` se necessário (dependendo da configuração da sua CrewAI).
2. Rode o script:

```bash
python agent_travel.py
```

O resultado será exibido no terminal com o roteiro e o orçamento estimado.

---

## Estrutura do Projeto

```bash
📁 agent_travel/
├── main.py   # Script principal com a definição dos agentes e tarefas
├── doc
├── .env
├── requirements.txt                # (Opcional) Chaves de API e configurações
├── README.md
            # Este arquivo
```

---

## Exemplo de Saída

```txt
Planejador de Viagem:
- Dia 1: Paris — Visita à Torre Eiffel, passeio no Sena
- Dia 2: Trem para Amsterdã — Museu Van Gogh e Bairro da Luz Vermelha
...

Orçamentista:
- Transporte: €250
- Hospedagem: €600
- Atividades: €200
- Total estimado: €1050
```

---

## Referências

- [CrewAI Docs](https://docs.crewai.com/)
- [OpenAI](https://platform.openai.com/)
- [dotenv (PyPI)](https://pypi.org/project/python-dotenv/)
- [Ollma](https://ollama.com/)

---

## Autor

Projeto criado para fins de aprendizado em agentes com a biblioteca CrewAI.
