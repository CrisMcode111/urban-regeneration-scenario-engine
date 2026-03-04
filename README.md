# Urban Regeneration Scenario Engine

AI-assisted MVP developed for the **World Wide Webs Hackathon** (Smart Cities & Infrastructure track).

The goal of this project is to explore **district-level urban regeneration scenarios** for the City of Montgomery using publicly available municipal datasets.

Instead of only analyzing districts, the system generates **practical regeneration scenarios** adapted to the local urban profile of each district.

---

## Problem

Cities often have access to many datasets, but it can be difficult to quickly translate those signals into **actionable regeneration ideas** for underperforming districts.

Urban planners and decision-makers need tools that help them **explore possible transformation paths**, not just static analytics.

---

## Approach

This MVP builds a lightweight **scenario engine** that:

1. Aggregates municipal datasets at the **district level**
2. Estimates two simple indicators:
   - **Business Activity** (based on Business Licenses)
   - **Urban Stress** (based on Code Violations)
3. Classifies districts into **urban typologies**
4. Generates **three possible regeneration scenarios** for each district
5. Assigns a **Scenario Fit Score** indicating how well each scenario matches the district profile

---

## Data Sources

Data used in this prototype comes from the **City of Montgomery Open Data Portal**.

Example datasets:

- Business Licenses
- Code Violations

These datasets are aggregated to create a **district-level urban profile**.

---

## Tools Used

This MVP leverages several tools introduced during the hackathon:

- **Google Stitch** – UI and demo interface
- **Antigravity** – logic flow and AI orchestration
- **OmniGuide** – project structuring support
- **AppClaimsEvaluator** – validation of project claims
- **Bright Data Integration Helper** – contextual enrichment

---

## MVP Scope

This is a **prototype**, not a full urban planning system.

The goal is to demonstrate how **AI-assisted scenario exploration** could support city-level regeneration thinking using existing public datasets.

---

## Team

Hackathon Team – World Wide Webs Hackathon  
Smart Cities & Infrastructure Track
