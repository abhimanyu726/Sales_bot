# Enterprise Outbound Sales Bot using LangGraph

## Overview

This project implements a production-grade AI outbound sales workflow using LangGraph.

The system is designed to simulate a scalable enterprise sales orchestration pipeline with:
- intelligent lead qualification
- outbound sales communication
- structured LLM reasoning
- adherence evaluation
- CRM logging
- human escalation handling

The architecture focuses on:
- low-latency execution
- modular orchestration
- scalable workflow design
- structured AI outputs
- enterprise-safe response generation

---

# Key Features

- LangGraph workflow orchestration
- Multi-node enterprise AI pipeline
- Pydantic-based structured parsing
- LLM-driven semantic reasoning
- Script adherence evaluation
- Human escalation logic
- Modular class-based architecture
- Centralized workflow state management
- Async execution
- Environment-based configuration
- Enterprise-grade prompt engineering

---

# Workflow Architecture

```text
User Input
    ↓
Intent Analysis
    ↓
Lead Qualification
    ↓
Sales Response Generation
    ↓
Adherence Evaluation
    ↓
CRM Logging
    ↓
Escalation Decision
    ↓
Final Response
```

---

# Node Responsibilities

## 1. Intent Analysis Node
Determines:
- customer intent
- urgency
- enterprise business context

Examples:
- enterprise_interest
- demo_request
- pricing_inquiry
- support_request

---

## 2. Lead Qualification Node
Evaluates:
- buying intent
- operational scale
- automation requirements
- enterprise relevance

Outputs:
- qualification status
- lead score
- qualification reasoning

---

## 3. Sales Response Node
Generates:
- professional outbound sales responses
- consultative enterprise communication
- CTA-driven responses
- discovery-oriented follow-ups

Optimized for:
- concise responses
- low token usage
- executive communication quality

---

## 4. Adherence Evaluation Node
Validates whether the generated response:
- follows enterprise sales practices
- maintains professional tone
- includes business value
- contains effective CTA
- avoids hallucinations

This acts as an enterprise AI quality assurance layer.

---

## 5. CRM Logging Node
Simulates CRM integration by storing:
- intent metadata
- qualification details
- adherence information
- escalation decisions

Designed for future integration with:
- Salesforce
- HubSpot
- Zoho CRM

---

## 6. Escalation Decision Node
Determines whether human intervention is required.

Escalation conditions:
- compliance-sensitive conversations
- customer dissatisfaction
- strategic enterprise opportunities
- unclear requirements
- low-confidence AI handling

---

# Project Structure

```bash
langgraph_sales_bot/
│
├── app.py
├── requirements.txt
├── README.md
├── .env.example
│
├── config/
│   └── settings.py
│
├── graph/
│   ├── sales_graph.py
│   └── state.py
│
├── prompts/
│   └── system_prompts.py
│
├── services/
│   ├── llm_service.py
│   └── crm_service.py
│
└── nodes/
    ├── intent_node.py
    ├── qualification_node.py
    ├── response_node.py
    ├── adherence_node.py
    ├── crm_node.py
    └── escalation_node.py
```

---

# Technologies Used

- LangGraph
- LangChain
- FastAPI
- Pydantic
- OpenAI API
- Python AsyncIO

---

# Why LangGraph?

LangGraph was selected because enterprise AI systems require:
- stateful orchestration
- modular workflows
- node-based execution
- conditional routing
- scalable AI pipelines

This architecture enables:
- easier debugging
- workflow observability
- independent node scaling
- future multi-agent support

---

# Why Pydantic Parsing?

Pydantic enables:
- structured LLM outputs
- deterministic parsing
- schema validation
- type safety
- enterprise reliability

This avoids:
- malformed JSON
- inconsistent outputs
- parsing instability

---

# Low Latency Design

The system is optimized for low latency through:
- concise prompts
- deterministic outputs
- low-temperature inference
- structured parsing
- lightweight orchestration
- modular execution

---

# Function Calling Support

The architecture is designed to support enterprise function/tool calling.

Potential integrations:
- CRM tools
- meeting scheduling
- lead database lookup
- analytics pipelines
- outbound campaign systems

---

# Setup

## 1. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 2. Create `.env`

```env
OPENAI_API_KEY=your_api_key

MODEL_NAME=gpt-4o-mini

TEMPERATURE=0
```

---

## 3. Run the Application

```bash
uvicorn app:app --reload --port 8080
```

---

# API Endpoint

## POST `/chat`

### Example Request

```json
{
  "message": "We need workflow automation for our enterprise team"
}
```

---

### Example Response

```json
{
  "intent": "enterprise_interest",
  "lead_score": 65,
  "qualified": true,
  "adherence_score": 81,
  "crm_logged": true,
  "escalation_required": false,
  "escalation_priority": "low",
  "escalation_reason": "Routine enterprise discovery conversation with no detected business or compliance risk.",
  "response": "Thank you for sharing your workflow automation requirements. To better understand your operational challenges, could you share which processes are currently experiencing the most friction? Based on your goals, a short discovery call would likely be the best next step to explore potential solutions in more detail."
}
```

---

# Enterprise Design Advantages

- Modular orchestration
- Scalable workflow architecture
- Structured AI reasoning
- Enterprise-safe responses
- Human-in-the-loop escalation
- Strong observability
- Centralized state management
- Production-oriented AI pipeline

---

# Future Improvements

- Real OpenAI function calling
- Redis-backed conversation memory
- Multi-agent orchestration
- Retry and self-correction loops
- Vector database integration
- Human approval workflows
- Real CRM integration
- Analytics dashboard
- Voice AI support

---

# Assignment Alignment

This project satisfies the assignment requirements by implementing:
- LangGraph-based workflow orchestration
- outbound sales automation
- scalable modular architecture
- low-latency AI pipeline design
- script adherence validation
- enterprise escalation handling
- structured AI outputs
- production-style orchestration