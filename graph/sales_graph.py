from langgraph.graph import StateGraph,END
from graph.state import SalesState

from nodes.intent_node import IntentNode
from nodes.qualification_node import QualificationNode
from nodes.response_node import ResponseNode
from nodes.adherence_node import AdherenceNode
from nodes.crm_node import CRMNode
from nodes.escalation_node import EscalationNode


class SalesGraph:

    def __init__(self):

        self.workflow = StateGraph(SalesState)
        self.build()

    def build(self):

        intent_node = IntentNode()
        qualification_node = QualificationNode()
        response_node = ResponseNode()
        adherence_node = AdherenceNode()
        crm_node = CRMNode()
        escalation_node = EscalationNode()

        self.workflow.add_node("intent_analysis", intent_node.execute)
        self.workflow.add_node("lead_qualification", qualification_node.execute)
        self.workflow.add_node("response_generation", response_node.execute)
        self.workflow.add_node("adherence_validation", adherence_node.execute)
        self.workflow.add_node("crm_logging", crm_node.execute)
        self.workflow.add_node("escalation_check", escalation_node.execute)

        self.workflow.set_entry_point("intent_analysis")

        self.workflow.add_edge("intent_analysis", "lead_qualification")
        self.workflow.add_edge("lead_qualification", "response_generation")
        self.workflow.add_edge("response_generation", "adherence_validation")
        self.workflow.add_edge("adherence_validation", "crm_logging")
        self.workflow.add_edge("crm_logging", "escalation_check")
        self.workflow.add_edge("escalation_check", END)

    def compile(self):

        return self.workflow.compile()