from langchain_core.output_parsers import PydanticOutputParser
from services.llm_service import LLMService
from prompts.system_prompts import LEAD_QUALIFICATION_PROMPT
from graph.state import QualificationOutput


class QualificationNode:

    def __init__(self):

        self.llm_service = LLMService()

        self.parser = (
            PydanticOutputParser(
                pydantic_object=QualificationOutput
            )
        )

    async def execute(self, state):

        prompt = f'''
        {LEAD_QUALIFICATION_PROMPT}

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

        state["qualified"] = parsed.qualified

        state["lead_score"] = parsed.lead_score

        return state