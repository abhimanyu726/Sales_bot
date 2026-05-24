from services.crm_service import (
    CRMService
)


class CRMNode:

    def __init__(self):

        self.crm_service = CRMService()

    async def execute(self, state):

        state["crm_logged"] = (
            await self.crm_service
            .log_interaction(state)
        )

        return state