from agents import WebSearchTool, Agent, ModelSettings, TResponseInputItem, Runner, RunConfig, trace
from pydantic import BaseModel

# Tool definitions
web_search_preview = WebSearchTool(
  user_location={
    "type": "approximate",
    "country": "BR",
    "region": None,
    "city": None,
    "timezone": None
  },
  search_context_size="medium"
)
pesquisa = Agent(
  name="Pesquisa",
  instructions="""Você é um assistente de IA que responde com base em pesquisas feitas na internet.

Seu trabalho principal é trazer informações sobre o São Paulo Futebol Clube""",
  model="gpt-4.1",
  tools=[
    web_search_preview
  ],
  model_settings=ModelSettings(
    temperature=1,
    top_p=1,
    max_tokens=2048,
    store=True
  )
)


class WorkflowInput(BaseModel):
  input_as_text: str


# Main code entrypoint
async def run_workflow(workflow_input: WorkflowInput):
  with trace("Agente de Pesquisa"):
    state = {

    }
    workflow = workflow_input.model_dump()
    conversation_history: list[TResponseInputItem] = [
      {
        "role": "user",
        "content": [
          {
            "type": "input_text",
            "text": workflow["input_as_text"]
          }
        ]
      }
    ]
    pesquisa_result_temp = await Runner.run(
      pesquisa,
      input=[
        *conversation_history
      ],
      run_config=RunConfig(trace_metadata={
        "__trace_source__": "agent-builder",
        "workflow_id": "wf_6957007f97dc8190a05237195eabe0000f6c57cbd011bb17"
      })
    )

    conversation_history.extend([item.to_input_item() for item in pesquisa_result_temp.new_items])

    pesquisa_result = {
      "output_text": pesquisa_result_temp.final_output_as(str)
    }
