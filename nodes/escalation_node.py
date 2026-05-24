from langchain_core.output_parsers import PydanticOutputParser
from services.llm_service import LLMService
from prompts.system_prompts import ESCALATION_PROMPT
from graph.state import EscalationOutput


class EscalationNode:

    def __init__(self):

        self.llm_service = LLMService()

        self.parser = (
            PydanticOutputParser(
                pydantic_object=EscalationOutput
            )
        )

    async def execute(self, state):

        prompt = f"""
        {ESCALATION_PROMPT}

        Customer Message:
        {state['user_input']}

        AI Response:
        {state['response']}

        Intent:
        {state['intent']}

        Lead Score:
        {state['lead_score']}

        Adherence Score:
        {state['adherence_score']}

        OUTPUT FORMAT (STRICT JSON)

        {self.parser.get_format_instructions()}
        """

        response = await self.llm_service.generate(
            prompt
        )

        parsed = self.parser.parse(
            response
        )

        state["escalation_required"] = (
            parsed.escalate
        )

        state["escalation_priority"] = (
            parsed.priority
        )

        state["escalation_reason"] = (
            parsed.reason
        )

        return state