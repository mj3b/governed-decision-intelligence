# Limitations and Threats to Validity

GDI is a decision-record architecture. Its current evidence supports schema behavior, deterministic reference rules, and local interoperability tests. The repository has not established improved institutional outcomes, legal conformity, or meaningful human control in deployed settings.

## Records can preserve weak governance

A complete GDR can document a process in which the human reviewer had little time, incomplete evidence, high override costs, or no practical power to change the result. Record completeness and substantive judgment are different constructs.

Human Influence Telemetry addresses this gap by testing evidence access, independent reasoning, intervention capability, appeal ownership, repair responsibility, and system-change authority. GDI supplies the record structure. HIT tests whether the recorded human role retained practical force.

## Hashes prove integrity within a bounded profile

A record hash can detect later modification to fields included in the hash profile. It cannot establish that the original record was accurate, complete, timely, or honestly produced. Integrity depends on canonicalization, field selection, key custody where signatures are used, and protection of the record-generation path.

## Confidence scores require calibration

The reference implementation accepts confidence values between 0 and 1 and compares them with institutional thresholds. These values may represent different quantities across models and tasks. Some systems provide no meaningful confidence estimate. Deployment requires domain-specific calibration, error-cost analysis, drift monitoring, and a rule for absent or invalid confidence.

## Framework mappings are interpretive

Mappings to NIST AI RMF, ISO/IEC 42001, the European Union Artificial Intelligence Act, and OECD principles identify potentially relevant evidence. They do not establish applicability, conformity, certification, or legal sufficiency. ISO clause-level conclusions require access to the licensed standard. Legal conclusions require qualified review.

## Examples have limited external validity

The included insurance and agent-tool examples are synthetic. They test representation and control logic. They do not establish effects in healthcare, employment, public benefits, finance, biopharma, public administration, or national-security settings.

## The governance layer can be bypassed

GDI assumes that relevant actions and evidence reach the governance layer. Hidden channels, compromised telemetry, collusive agents, prompt injection, tampered inputs, or an unobserved execution path can produce an incomplete or false record.

## A record is not an explanation by itself

A decision record may support explanation, audit, or appeal. Audience needs, legal duties, trade secrets, privacy, accessibility, and procedural rights determine what explanation must be provided and to whom.

## Privacy and data minimization remain deployment obligations

Decision records can contain personal data, sensitive evidence, model inputs, and employee identifiers. Implementers must define minimization, access controls, retention, redaction, subject rights, and lawful processing outside the core schema.

## Independent validation remains pending

The reference implementation and mappings were developed by the project author. External review, replication, adversarial testing, and comparative deployment studies remain open research needs.

## Update condition

These limitations must be revised whenever the schema, hash profile, framework mappings, reference implementation, or empirical evidence changes.