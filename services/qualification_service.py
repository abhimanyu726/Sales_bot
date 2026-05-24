class QualificationService:

    ENTERPRISE_KEYWORDS = [
        "team",
        "enterprise",
        "automation",
        "workflow"
    ]

    def evaluate(self, text: str):

        score = sum(
            keyword in text.lower()
            for keyword in self.ENTERPRISE_KEYWORDS
        )

        return {
            "lead_score": score,
            "qualified": score >= 2
        }
