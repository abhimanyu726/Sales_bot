class AdherenceService:

    REQUIRED_COMPONENTS = [
        "business",
        "solution",
        "demo"
    ]

    def validate(self, response: str):

        score = sum(
            component in response.lower()
            for component in self.REQUIRED_COMPONENTS
        ) * 30

        return min(score, 100)
