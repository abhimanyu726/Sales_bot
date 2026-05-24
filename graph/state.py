from typing import TypedDict, List, Optional
from pydantic import BaseModel


class SalesState(TypedDict):

    user_input: str
    conversation_history: List[str]
    intent: Optional[str]
    lead_score: Optional[int]
    qualified: Optional[bool]
    adherence_score: Optional[int]
    crm_logged: Optional[bool]
    escalation_required: Optional[bool]
    escalation_priority: Optional[str]
    escalation_reason: Optional[str]
    response: Optional[str]


class IntentOutput(BaseModel):

    intent: str
    urgency: str
    business_context: str


class QualificationOutput(BaseModel):

    qualified: bool
    lead_score: int
    reason: str


class AdherenceOutput(BaseModel):

    score: int
    passed: bool
    reason: str


class EscalationOutput(BaseModel):

    escalate: bool
    priority: str
    reason: str