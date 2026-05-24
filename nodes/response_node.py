from services.llm_service import (
    LLMService
)

from prompts.system_prompts import (
    SALES_RESPONSE_PROMPT
)


class ResponseNode:

    def __init__(self):

        self.llm_service = LLMService()

    async def execute(self, state):

        prompt = f'''
        {SALES_RESPONSE_PROMPT}

        Customer Message:
        {state["user_input"]}

        Intent:
        {state["intent"]}

        Qualified Lead:
        {state["qualified"]}
        '''

        response = await self.llm_service.generate(
            prompt
        )

        state["response"] = response

        return state