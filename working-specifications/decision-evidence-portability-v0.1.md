# Decision Evidence Portability Specification

**Status:** Working specification  
**Version:** 0.1.0  
**Date:** 2026-07-15  
**Author:** Mark Julius Banasihan  
**ORCID:** 0009-0001-8121-2878

## Bounded thesis

A recurring set of decision-evidence objects can support AI assurance across multiple regulatory and standards regimes. Each regime assigns its own legal meaning, thresholds, obligations, and consequences to those objects.

This specification does not claim that governance regimes are equivalent. It tests which decision evidence can travel across regimes, which evidence requires a jurisdiction-specific overlay, and where apparent equivalence fails.

## Problem

AI governance crosswalks usually compare terms, controls, or framework categories. Those mappings can conceal differences in legal force, regulated actor, assurance burden, and enforcement consequence.

The missing layer is a machine-readable account of the decision evidence itself: who held authority, what evidence was available, how AI influenced the decision, where intervention remained possible, what reasons were recorded, and who owned appeal, repair, and system change.

## Relationship to existing work

This working specification extends Governed Decision Intelligence.

- Governed Decision Intelligence structures the governed decision record.
- Human Influence Telemetry tests whether formal human authority retained causal force.
- Decision Evidence Portability maps reusable decision evidence to external governance obligations while preserving jurisdiction-specific differences.

## Initial ontology

The v0.1 ontology contains ten top-level objects:

1. actor
2. institutional_role
3. decision_authority
4. ai_influence
5. evidence_access
6. intervention_capability
7. recorded_reasoning
8. approval_conditions
9. monitoring_and_incident_record
10. appeal_repair_and_system_change_authority

Each object must resolve into observable artifacts, validation rules, failure signs, and provenance.

## Mapping record

Each cross-regime mapping must record:

- source authority
- source type
- legal or normative force
- regulated actor
- governed object
- required evidence
- assurance test
- jurisdiction-specific condition
- point of non-equivalence
- mapping confidence

## Initial scope

Version 0.1 will test one agentic workflow in which an AI system retrieves evidence, recommends a decision, prepares an action, and requires human authorization before execution.

The initial comparison set is:

- NIST AI Risk Management Framework
- ISO/IEC 42001 and selected supporting standards
- European Union Artificial Intelligence Act
- selected Chinese agent-governance requirements as a comparative annex

## Acceptance conditions

The working specification will advance beyond v0.1 only when:

1. every mapping links to an authoritative source;
2. each regime contains at least one explicit point of non-equivalence;
3. one core decision record validates under at least two jurisdictional overlays without changing historical facts;
4. each overlay can require additional local evidence;
5. missing authority, intervention, or logging evidence produces a defined failure;
6. policy obligations map to identifiable enforcement points in the agent workflow;
7. outputs state evidence sufficiency and never declare legal compliance;
8. the draft receives legal or standards review and technical assurance review.

## Current status

This document establishes authorship, scope, terminology, and the initial research claim. The ontology, schema extension, mappings, test workflow, and case studies remain in development.

## Citation

Banasihan, Mark Julius. “Decision Evidence Portability Specification.” Working specification, version 0.1.0, July 15, 2026.
