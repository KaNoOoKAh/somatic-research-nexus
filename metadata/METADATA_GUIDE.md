# Metadata Guide: Knowledge Integrity for the Somatic Research Nexus

## 1. Why Metadata Matters

Research involving physiology, cognition, perception, behavior, and health-related observations often generates large volumes of information across multiple repositories, experiments, and time periods.

Without standardized metadata, important context can become lost:
- Where did an observation originate?
- Which hypothesis does it support or challenge?
- What methodology was used?
- Is the information current, active, archived, or superseded?
- What related observations or datasets exist elsewhere?

Metadata preserves this context.

The metadata system transforms individual files from isolated documents into interconnected research records. Each record can be traced, evaluated, compared, and linked to broader patterns across the research ecosystem.

This approach supports:
- Scientific transparency
- Reproducibility
- Knowledge integration
- Long-term preservation
- Cross-repository intelligence

---

## 2. The Importance of Metadata

Metadata is often described as "data about data," but within the Somatic Research Nexus it serves a much larger purpose[cite: 1].

Metadata preserves the context surrounding information so that records remain understandable, traceable, and useful long after they were originally created[cite: 1].

A document may record an observation, experiment, idea, analysis, or personal experience[cite: 1]. Metadata records the circumstances surrounding that information, including when it was created, why it was created, how it was obtained, what evidence supports it, and how it relates to other knowledge[cite: 1].

Without metadata, information can become fragmented, misinterpreted, duplicated, or disconnected from its origin[cite: 1].

### Scientific Research

In scientific research, metadata helps preserve:
- Experimental conditions[cite: 1]
- Methodologies[cite: 1]
- Instrumentation[cite: 1]
- Evidence levels[cite: 1]
- Assumptions[cite: 1]
- Limitations[cite: 1]
- Review history[cite: 1]

Scientific metadata improves transparency, reproducibility, validation, and long-term research integrity[cite: 1]. It helps distinguish observations from interpretations, hypotheses from conclusions, and preliminary findings from verified evidence[cite: 1].

### Medical and Health-Related Records

In medical, physiological, and health-related observations, context is often as important as the observation itself[cite: 1].

Metadata helps record:
- Time and location[cite: 1]
- Environmental conditions[cite: 1]
- Observation methods[cite: 1]
- Relevant physiological context[cite: 1]
- Changes over time[cite: 1]
- Confidence and uncertainty[cite: 1]

This information helps prevent isolated observations from being separated from the circumstances under which they were recorded[cite: 1].

### Academic Knowledge

Academic work often builds upon previous knowledge[cite: 1].

Metadata supports:
- Citation tracking[cite: 1]
- Source attribution[cite: 1]
- Version history[cite: 1]
- Research lineage[cite: 1]
- Cross-referencing[cite: 1]
- Knowledge verification[cite: 1]

Proper metadata helps connect ideas across studies, disciplines, repositories, and generations of contributors[cite: 1].

### Personal Knowledge Management

Personal observations, journals, experiments, notes, and reflections may gain value over time when they can be rediscovered and connected to other information[cite: 1].

Metadata helps individuals:
- Track personal development[cite: 1]
- Identify patterns[cite: 1]
- Organize observations[cite: 1]
- Revisit earlier ideas[cite: 1]
- Preserve context and intent[cite: 1]
- Build long-term knowledge systems[cite: 1]

What may appear insignificant today may become meaningful when connected to future observations[cite: 1].

### Knowledge Preservation

Knowledge rarely exists in isolation[cite: 1].

Metadata allows information to remain connected through:
- Relationships[cite: 1]
- Dependencies[cite: 1]
- References[cite: 1]
- Sources[cite: 1]
- Shared concepts[cite: 1]
- Common evidence[cite: 1]

As repositories grow, metadata transforms individual files into a searchable and interconnected knowledge network[cite: 1].

### The Core Principle

Information explains *what* was recorded[cite: 1].

Metadata explains:
- Why it matters[cite: 1]
- Where it came from[cite: 1]
- How it was produced[cite: 1]
- What supports it[cite: 1]
- What limits it[cite: 1]
- How it connects to other knowledge[cite: 1]

The purpose of metadata within the Somatic Research Nexus is not simply organization[cite: 1].

Its purpose is to preserve context, support traceability, protect knowledge integrity, and ensure that observations, hypotheses, analyses, and discoveries remain connected to the evidence and circumstances that produced them[cite: 1].

---

## 3. Overview & Core Metadata Schema

This repository uses a structured metadata standard to maintain quality, traceability, and long-term usefulness across the Somatic Research Nexus.

Each file should include a YAML frontmatter block containing the core metadata for that record.

```yaml
---
record_id: "UNIQUE_IDENTIFIER"
title: "Clear, Descriptive Title"
repository: "repository-name"
schema_version: "1.0"

created_at: "YYYY-MM-DDTHH:MM:SS±HH:MM"
updated_at: "YYYY-MM-DDTHH:MM:SS±HH:MM"

domain: ["domain1", "domain2"]
objective: "What question does this record address?"
method: "What methodology was used?"

record_type: "observation | interpretation | hypothesis | analysis | conclusion | protocol | framework | reference"
evidence_level: "Level 0 | Level 1 | Level 2 | Level 3 | Level 4 | Level 5"
data_status: "raw | processed | analyzed | archived"
confidence_rating: 0.0

direct_observation: "What was directly recorded or measured?"
interpretation: "What might this observation mean?"
hypothesis: "What explanation is proposed?"
assumptions:
  - "assumption 1"
limitations:
  - "limitation 1"
uncertainties:
  - "uncertainty 1"
alternative_explanations:
  - "explanation 1"

location: "Geographic location"
ambient_conditions:
  temperature_c: 25.0
  humidity_pct: 60
  acoustic_noise_db: 45.0

sensor_rig: "Sensor array or instrument used"
data_quality_metrics: {}
source_record: "record_id of originating document"
related_records: ["record_id_1", "record_id_2"]

contributors: ["contributor1", "contributor2"]
review_status: "draft | submitted | under_review | reviewed | disputed | superseded"
license: "CC-BY-4.0"
access_level: "public | collaborative | private"

tags: ["tag1", "tag2", "tag3"]
change_log:
  - date: "YYYY-MM-DD"
    change: "Description of change"
    contributor: "Contributor name"
---
