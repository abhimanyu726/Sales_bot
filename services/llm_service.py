from langchain_openai import ChatOpenAI
from config.settings import Settings


class LLMService:

    def __init__(self):

        self.llm = ChatOpenAI(
            api_key=Settings.OPENAI_API_KEY,
            model=Settings.MODEL_NAME,
        )

    async def generate(
        self,
        prompt: str
    ):

        response = await self.llm.ainvoke(
            prompt
        )

        return response.content