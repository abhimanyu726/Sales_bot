from langchain_core.output_parsers import (
    PydanticOutputParser
)

from services.llm_service import (
    LLMService
)

from prompts.system_prompts import (
    ADHERENCE_EVALUATION_PROMPT
)

from graph.state import (
    AdherenceOutput
)


class AdherenceNode:

    def __init__(self):

        self.llm_service = LLMService()

        self.parser = (
            PydanticOutputParser(
                pydantic_object=AdherenceOutput
            )
        )

    async def execute(self, state):

        prompt = f'''
        {ADHERENCE_EVALUATION_PROMPT}

        AI Response:
        {state["response"]}

        OUTPUT FORMAT (STRICT JSON)

        {self.parser.get_format_instructions()}
        '''

        response = await self.llm_service.generate(
            prompt
        )

        parsed = self.parser.parse(
            response
        )

        state["adherence_score"] = parsed.score

        return state