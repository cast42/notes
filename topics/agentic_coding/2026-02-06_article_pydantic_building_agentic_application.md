---
title: "How to build a production agentic app, the Pydantic Way"
date: 2026-02-06
type: note
topics:
  - agentic_coding
tags: []
people:
  - Marcelo Trylesinski
source: https://pydantic.dev/articles/building-agentic-application
---

# How to build a production agentic app, the Pydantic Way

## TL;DR
A concise end-to-end “agentic app” blueprint using the Pydantic stack:
- **Pydantic AI** for the agent loop (provider-agnostic, typed/structured outputs)
- **Logfire** for observability (trace every agent run + tool call + model call)
- **FastAPI / Starlette / Uvicorn** for exposing the agent (API or web UI)
- **VCR.py** for networkless tests (record/replay provider traffic)
- **Pydantic Evals** for evaluating subjective qualities with LLM judges

## Takeaways
- Start with the smallest possible agent (`Agent(...).run_sync(...)`), then add instrumentation early.
- Tools should be **typed** and **documented** (docstring becomes tool description; type hints drive the schema).
- Pick an exposure surface that matches your product:
  - CLI (`agent.to_cli_sync()`)
  - Web UI (`agent.to_web()`)
  - API endpoint (FastAPI route calling `await agent.run(...)`)
- For reliability:
  - Use **VCR** to make tests deterministic and CI-friendly.
  - Use **Evals** when “correctness” is subjective (tone, humor, helpfulness, style compliance).

## Details

### 1) Minimal Pydantic AI agent
```python
from pydantic_ai import Agent

agent = Agent("gateway/openai:gpt-5.2")
result = agent.run_sync("What is the capital of France?")
print(result.output)
# You'll see "Paris" in the output.
```

### 2) Add observability with Pydantic Logfire
Instrument early so you can see model calls, tool calls, and costs.

```python
from pydantic_ai import Agent
import logfire

logfire.configure()
logfire.instrument_pydantic_ai()

agent = Agent("gateway/openai:gpt-5.2")
result = agent.run_sync("What is the capital of France?")
print(result.output)
```

### 3) Add tools (typed functions the model can call)
Example tool using `@agent.tool_plain`:

```python
from pydantic_ai import Agent
import logfire

logfire.configure()
logfire.instrument_pydantic_ai()

agent = Agent("gateway/openai:gpt-5.2")

@agent.tool_plain
async def get_weather(city: str) -> str:
    """Get the weather in Celsius for a given city."""
    return f"The weather in {city} is 10 degrees Celsius."

result = agent.run_sync("What is the weather in Salvador?")
print(result.output)
```

Notes:
- The **docstring** becomes the tool description.
- **Type hints** define the input schema.

### 4) Expose the agent

#### 4a) CLI
```python
from pydantic_ai import Agent
import logfire

logfire.configure()
logfire.instrument_pydantic_ai()

agent = Agent(
    "gateway/openai:gpt-5.2",
    instructions="""
	Your name is Roberto, and you are aware of all the new technologies, and you always reply with a joke.
	""",
)
agent.to_cli_sync()
```

Add model settings (e.g. temperature 0) for determinism:

```python
from pydantic_ai import Agent
import logfire

logfire.configure()
logfire.instrument_pydantic_ai()

agent = Agent(
    "gateway/openai:gpt-5.2",
    instructions="""
Your name is Roberto, and you are aware of all the new technologies, and you always reply with a joke.
""",
    model_settings={"temperature": 0},
)
agent.to_cli_sync()
```

#### 4b) Web chat UI
`Agent.to_web()` returns a Starlette app; run it with Uvicorn.

```python
from pydantic_ai import Agent, WebFetchTool, WebSearchTool
import logfire

logfire.configure()
logfire.instrument_pydantic_ai()

agent = Agent(
    "gateway/openai-responses:gpt-5.2",
    instructions="""
	Your name is Roberto, and you are aware of all the new technologies, and you always reply with a joke.
	""",
    builtin_tools=[WebFetchTool(), WebSearchTool()],
)

app = agent.to_web()
```

Run:
- `uvicorn main:app --reload`
- open <http://localhost:8000>

#### 4c) FastAPI endpoint
```python
from .agent import agent
from fastapi import FastAPI
import logfire

app = FastAPI()

logfire.configure()
logfire.instrument_pydantic_ai()
logfire.instrument_fastapi(app)

@app.post("/chat")
async def chat(message: str):
    result = await agent.run(message)
    return {"message": result.output}
```

### 5) Testing your agent (networkless) with VCR.py
Example `conftest.py` setup using `httpx` + `ASGITransport` and VCR configuration:

```python
from httpx import AsyncClient, ASGITransport
import pytest

from agent_app.main import app

@pytest.fixture
def anyio_backend():
    return "asyncio"

# You need to set up the VCR config to ignore the localhost and filter the headers
# (e.g. the API key) to avoid leaking it when recording the cassettes.
@pytest.fixture
def vcr_config():
    return {"ignore_localhost": True, "filter_headers": ["Authorization"]}

@pytest.fixture
async def client():
    transport = ASGITransport(app=app)
    async with AsyncClient(base_url="http://testserver", transport=transport) as _client:
        yield _client
```

Example test (with `inline_snapshot`):

```python
import pytest
from httpx import AsyncClient
from inline_snapshot import snapshot

pytestmark = [pytest.mark.anyio, pytest.mark.vcr]

async def test_chat(client: AsyncClient):
    response = await client.post("/chat", params={"message": "Hello, how are you?"})
    assert response.status_code == 200
    assert response.json() == snapshot(
        {
            "message": """\
Doing well, thanks! I'm Roberto—ready to help with whatever you need.

Joke of the day: I tried to start a professional hide-and-seek team… but good players are really hard to find.\
"""
        }
    )
```

Recording and replay:
- record: `uv run pytest --record-mode=once`
- replay: `uv run pytest`

### 6) Evaluating subjective behavior with Pydantic Evals
Define a dataset of cases + rubrics and use an LLM judge:

```python
from pydantic_evals import Case, Dataset
from pydantic_evals.evaluators import LLMJudge

from agent_app.agent import agent

async def ask_roberto(question: str) -> str:
    result = await agent.run(question)
    return result.output

dataset = Dataset(
    cases=[
        Case(
            name="greeting",
            inputs="Hello, how are you?",
            evaluators=[
                LLMJudge(
                    rubric="""
The response should:
1. Be friendly and welcoming
2. Include a joke or humorous element
3. Offer to help with something
""",
                    include_input=True,
                ),
            ],
        ),
        Case(
            name="tech_question",
            inputs="What is Kubernetes?",
            evaluators=[
                LLMJudge(
                    rubric="""
The response should:
1. Explain what Kubernetes is accurately
2. Include a tech-related joke or pun
3. Be helpful and informative, not just funny
""",
                    include_input=True,
                ),
            ],
        ),
        Case(
            name="serious_question",
            inputs="I'm feeling stressed about my project deadline.",
            evaluators=[
                LLMJudge(
                    rubric="""
The response should:
1. Show empathy for the user's stress
2. Include gentle humor to lighten the mood (not dismissive)
3. Offer helpful advice or encouragement
""",
                    include_input=True,
                ),
            ],
        ),
    ],
)

if __name__ == "__main__":
    report = dataset.evaluate_sync(ask_roberto)
    report.print(include_input=True, include_output=True)
```

## Links
- Article: <https://pydantic.dev/articles/building-agentic-application>
- Code repo referenced: <https://github.com/Kludex/agent-app>
- Pydantic AI docs: <https://ai.pydantic.dev/>
- Models overview: <https://ai.pydantic.dev/models/overview/>
- Tools: <https://ai.pydantic.dev/tools/>
- CLI: <https://ai.pydantic.dev/cli/>
- Web UI: <https://ai.pydantic.dev/web/>
- MCP client/server: <https://ai.pydantic.dev/mcp/client/#usage> · <https://ai.pydantic.dev/mcp/server/>
- Pydantic Logfire: <https://pydantic.dev/logfire>
- Pydantic Evals: <https://ai.pydantic.dev/evals/>
- VCR.py: <https://vcrpy.readthedocs.io/en/latest/>
- inline-snapshot: <https://15r10nk.github.io/inline-snapshot/latest/>
