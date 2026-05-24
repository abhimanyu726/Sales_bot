from langchain_core.output_parsers import (
    PydanticOutputParser
)

from services.llm_service import (
    LLMService
)

from prompts.system_prompts import (
    INTENT_ANALYSIS_PROMPT
)

from graph.state import (
    IntentOutput
)


class IntentNode:

    def __init__(self):

        self.llm_service = LLMService()

        self.parser = (
            PydanticOutputParser(
                pydantic_object=IntentOutput
            )
        )

    async def execute(self, state):

        prompt = f'''
        {INTENT_ANALYSIS_PROMPT}

        Customer Message:
        {state["user_input"]}

        OUTPUT FORMAT (STRICT JSON)

        {self.parser.get_format_instructions()}
        '''

        response = await self.llm_service.generate(
            prompt
        )

        parsed = self.parser.parse(
            response
        )

        state["intent"] = parsed.intent

        return state