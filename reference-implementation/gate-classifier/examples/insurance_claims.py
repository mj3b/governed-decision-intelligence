"""
examples/insurance_claims.py

Worked example: insurance claims processing agent across all four gates.

Demonstrates gate classification behavior using AGT's actual architecture.

The MockPolicyInterceptor mirrors AGT's PolicyInterceptor.intercept() interface
from packages/agent-os/src/agent_os/integrations/base.py. Replace with the
real BaseIntegration subclass when AGT is installed.

Run standalone (no AGT install required):
    python examples/insurance_claims.py

Run with AGT installed, replace MockPolicyInterceptor with:
    from agent_os.integrations.base import (
        GovernancePolicy, PolicyInterceptor, ExecutionContext, ToolCallRequest
    )

Author: Mark Julius (mj3b)
License: Apache 2.0
"""

import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from gate_classifier import (
    GateClassifier,
    GateRecord,
    Gate,
    EscalationRequired,
    FileRecordWriter,
)


# ---------------------------------------------------------------------------
# Mock AGT interfaces for standalone demonstration
# When AGT is installed, replace these with:
#   from agent_os.integrations.base import (
#       GovernancePolicy, PolicyInterceptor, ExecutionContext, ToolCallRequest
#   )
# ---------------------------------------------------------------------------

class MockGovernancePolicy:
    """Mirrors GovernancePolicy from integrations/base.py"""
    def __init__(self, confidence_threshold=0.8, allowed_tools=None, require_human_approval=False):
        self.confidence_threshold = confidence_threshold
        self.allowed_tools = allowed_tools or []
        self.require_human_approval = require_human_approval
        self.max_tool_calls = 10


class MockExecutionContext:
    """Mirrors ExecutionContext from integrations/base.py"""
    def __init__(self, agent_id, policy):
        self.agent_id = agent_id
        self.policy = policy
        self.session_id = "demo-session-001"
        self.call_count = 0


class MockToolCallRequest:
    """Mirrors ToolCallRequest from integrations/base.py"""
    def __init__(self, tool_name, arguments, agent_id=""):
        self.tool_name = tool_name
        self.arguments = arguments
        self.agent_id = agent_id


class MockPolicyInterceptor:
    """
    Mirrors PolicyInterceptor.intercept() from integrations/base.py.

    Returns (allowed, reason) matching AGT's pre_execute() return signature.
    """
    DENIED_TOOLS = {"shell_exec", "drop_table", "bulk_delete"}

    def __init__(self, policy: MockGovernancePolicy):
        self.policy = policy

    def intercept(self, request: MockToolCallRequest):
        """Mirror AGT's PolicyInterceptor.intercept() logic."""
        if self.policy.require_human_approval:
            return False, f"Tool '{request.tool_name}' requires human approval"
        if self.policy.allowed_tools and request.tool_name not in self.policy.allowed_tools:
            return False, f"Tool '{request.tool_name}' not in allowed list"
        if request.tool_name in self.DENIED_TOOLS:
            return False, f"Tool '{request.tool_name}' matches blocked action class"
        return True, None


# ---------------------------------------------------------------------------
# Helper: print record summary
# ---------------------------------------------------------------------------

def print_record(record: GateRecord, scenario: str) -> None:
    gate_labels = {
        Gate.ROUTINE: "GATE 1 — Routine Execution",
        Gate.DOCUMENTED_DELEGATION: "GATE 2 — Documented Delegation",
        Gate.ELEVATED_REVIEW: "GATE 3 — Elevated Review",
        Gate.HARD_ESCALATION: "GATE 4 — Hard Escalation",
    }
    print(f"\n{'='*60}")
    print(f"SCENARIO: {scenario}")
    print(f"{'='*60}")
    print(f"  Agent:            {record.agent_id}")
    print(f"  Tool:             {record.tool_name}")
    print(f"  AGT policy:       {'ALLOWED' if record.policy_allowed else 'DENIED'}")
    print(f"  Gate:             {gate_labels[record.gate]}")
    print(f"  Rationale:        {record.gate_rationale}")
    print(f"  Confidence:       {record.confidence_score}")
    print(f"  Policy threshold: {record.policy_confidence_threshold}")
    print(f"  Alternatives:     {record.alternatives_considered}")
    print(f"  Escalation:       {record.escalation_required}")
    if record.escalation_trigger:
        print(f"  Trigger:          {record.escalation_trigger}")
    if record.delegation_reference:
        print(f"  Delegation:       {record.delegation_reference}")
    print(f"  Classified at:    {record.classified_at}")
    print(f"  Record ID:        {record.record_id}")
    print(f"  Integrity:        {'VALID' if record.verify_integrity() else 'COMPROMISED'}")
    print()


# ---------------------------------------------------------------------------
# Scenarios
# ---------------------------------------------------------------------------

def run_scenarios():
    policy = MockGovernancePolicy(confidence_threshold=0.8)
    ctx = MockExecutionContext(agent_id="claims-agent-001", policy=policy)
    interceptor = MockPolicyInterceptor(policy=policy)
    classifier = GateClassifier(
        record_writer=FileRecordWriter("gate_records_insurance_claims.ndjson")
    )

    print("\nINSURANCE CLAIMS PROCESSING — GATE CLASSIFICATION DEMONSTRATION")
    print("=" * 60)
    print("Scenario: An AI agent processes incoming insurance claims.")
    print("AGT handles policy enforcement. Gate classifier handles")
    print("decision-layer accountability.\n")

    # ------------------------------------------------------------------
    # Scenario 1: Gate 1 — Routine Execution
    # ------------------------------------------------------------------
    request_1 = MockToolCallRequest("file_read", {"path": "/claims/CLM-2024-00441.json"}, ctx.agent_id)
    policy_allowed, policy_reason = interceptor.intercept(request_1)

    record_1 = classifier.evaluate(
        policy_allowed=policy_allowed,
        policy_reason=policy_reason,
        policy_confidence_threshold=policy.confidence_threshold,
        agent_id=ctx.agent_id,
        tool_name=request_1.tool_name,
        tool_args=request_1.arguments,
        confidence_score=0.97,
        alternatives_considered=["database_read"],
        declared_task="retrieve claim file for initial triage review",
        conditions_at_decision={"task": "retrieve_claim_for_review", "claim_id": "CLM-2024-00441"},
    )
    print_record(record_1, "Retrieve claim file for initial review")
    print(f"  Reconstruction:   {record_1.reasoning_reconstruction[:120]}...")

    # ------------------------------------------------------------------
    # Scenario 2: Gate 2 — Documented Delegation
    # ------------------------------------------------------------------
    request_2 = MockToolCallRequest("web_search", {"query": "ICD-10 code M54.5 treatment protocols"}, ctx.agent_id)
    policy_allowed, policy_reason = interceptor.intercept(request_2)

    record_2 = classifier.evaluate(
        policy_allowed=policy_allowed,
        policy_reason=policy_reason,
        policy_confidence_threshold=policy.confidence_threshold,
        agent_id=ctx.agent_id,
        tool_name=request_2.tool_name,
        tool_args=request_2.arguments,
        confidence_score=0.88,
        alternatives_considered=["database_read", "file_read"],
        confidence_distribution={"web_search": 0.88, "database_read": 0.72, "file_read": 0.61},
        declared_task="verify ICD-10 coding for claim CLM-2024-00441 medical necessity",
        conditions_at_decision={"task": "verify_medical_coding", "claim_value": 1200.00},
        delegation_reference="AUTO-APPROVAL-POLICY-v2.3-VP-CLAIMS-2024-01-15",
    )
    print_record(record_2, "Verify medical coding under pre-authorized auto-approval policy")
    print(f"  Reconstruction:   {record_2.reasoning_reconstruction[:120]}...")

    # ------------------------------------------------------------------
    # Scenario 3: Gate 3 — Elevated Review
    # ------------------------------------------------------------------
    request_3 = MockToolCallRequest(
        "database_write",
        {"table": "claims_decisions", "record": {"claim_id": "CLM-2024-00441", "decision": "approved"}},
        ctx.agent_id
    )
    policy_allowed, policy_reason = interceptor.intercept(request_3)

    record_3 = classifier.evaluate(
        policy_allowed=policy_allowed,
        policy_reason=policy_reason,
        policy_confidence_threshold=policy.confidence_threshold,
        agent_id=ctx.agent_id,
        tool_name=request_3.tool_name,
        tool_args=request_3.arguments,
        confidence_score=0.85,
        alternatives_considered=["flag_for_manual_review", "request_additional_documentation"],
        confidence_distribution={"database_write": 0.85, "flag_for_manual_review": 0.72, "request_additional_documentation": 0.61},
        declared_task="record approved claim decision for CLM-2024-00441 value $1200",
        conditions_at_decision={"task": "record_claim_decision", "claim_value": 1200.00},
    )
    print_record(record_3, "Write claim approval decision to database")
    print(f"  Reconstruction:   {record_3.reasoning_reconstruction[:120]}...")

    # ------------------------------------------------------------------
    # Scenario 4: Gate 4 — Hard Escalation (policy denied by AGT)
    # ------------------------------------------------------------------
    print("Attempting bulk_delete — AGT policy denies, Gate 4 fires...\n")
    request_4 = MockToolCallRequest(
        "bulk_delete",
        {"table": "claims_queue", "condition": "status = 'processed' AND age_days > 90"},
        ctx.agent_id
    )
    policy_allowed, policy_reason = interceptor.intercept(request_4)

    record_4 = classifier.evaluate(
        policy_allowed=policy_allowed,
        policy_reason=policy_reason,
        policy_confidence_threshold=policy.confidence_threshold,
        agent_id=ctx.agent_id,
        tool_name=request_4.tool_name,
        tool_args=request_4.arguments,
        confidence_score=0.91,
        alternatives_considered=["archive_records", "flag_for_review"],
        conditions_at_decision={"task": "purge_processed_claims", "records_affected": 847},
    )
    print_record(record_4, "Bulk delete processed claims — ESCALATION")

    if record_4.escalation_required:
        try:
            raise EscalationRequired(record_4)
        except EscalationRequired as e:
            print(f"  >>> EXECUTION HALTED <<<")
            print(f"  {e}")
            print(f"\n  Human authority required before this action can proceed.")
            print(f"  Record written to audit log before halt.")
            print(f"  AGT policy reason: {record_4.policy_reason}")

    print("\n" + "="*60)
    print("DEMONSTRATION COMPLETE")
    print("Gate records: gate_records_insurance_claims.ndjson")
    print("Each record is SHA-256 hashed and written before execution.")
    print("AGT governs the action layer. The gate classifier governs")
    print("the decision layer. Both are necessary.")
    print("="*60 + "\n")


if __name__ == "__main__":
    run_scenarios()
