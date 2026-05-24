class CRMService:

    async def log_interaction(
        self,
        state
    ):

        print(
            f'''
            CRM LOG

            Intent:
            {state["intent"]}

            Qualified:
            {state["qualified"]}

            Lead Score:
            {state["lead_score"]}
            '''
        )

        return True