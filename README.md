# Urban Regeneration Scenario Engine

AI-assisted MVP developed for the **World Wide Webs Hackathon**  
(Smart Cities & Infrastructure track).

The goal of this project is to explore **district-level urban regeneration scenarios** for the City of Montgomery using publicly available municipal datasets.

Instead of only analyzing districts, the system generates **practical regeneration scenarios** adapted to the local urban profile of each district.

---

# Problem

Cities often have access to many datasets, but it can be difficult to quickly translate those signals into **actionable regeneration ideas** for underperforming districts.

Urban planners and decision-makers need tools that help them **explore possible transformation paths**, not just static analytics.

---

# Approach

This MVP builds a lightweight **scenario engine** that:

1. Aggregates municipal datasets at the **district level**
2. Estimates two simple indicators:
   - **Business Activity** (based on Business Licenses)
   - **Urban Stress** (based on Code Violations)
3. Classifies districts into **urban typologies**
4. Generates **three regeneration scenarios** for each district
5. Assigns a **Scenario Fit Score** indicating how well each scenario matches the district profile

---

# Data Sources

Data used in this prototype comes from the **City of Montgomery Open Data Portal**.

Example datasets:

- Business Licenses
- Code Violations

These datasets are aggregated to create a **district-level urban profile**.

---

# District Classification Method

To understand the urban dynamics of Montgomery districts, we created a simple rule-based classification using two indicators:

- **Business activity** – number of active business licenses per district  
- **Urban stress** – number of code violations per district  

Both datasets were aggregated by **Council District**.

## Step 1 – Calculate city averages

We compute the average number of business licenses and violations across all districts.

## Step 2 – Assign High / Low levels

Each district is compared to the city average.

Business level:

- Above average → **High**
- Below average → **Low**

Stress level:

- Above average violations → **High stress**
- Below average violations → **Low stress**

## Step 3 – District typology

Combining the two dimensions produces four district types:

| Business | Stress | Type |
|---|---|---|
| High | Low | HB_LS |
| High | High | HB_HS |
| Low | High | LB_HS |
| Low | Low | LB_LS |

This typology allows the system to generate **targeted urban regeneration scenarios**.

---

# Scenario Generation

For each district type, the system generates:

- **3 regeneration scenarios**
- a **Scenario Fit Score**

Scenarios are selected from a structured **scenario library** and matched to the district typology using a rule-based fit matrix.

## Example District Output

Example analysis for a Montgomery district:

District: 4  
Business Activity: Low  
Urban Stress: High  
District Type: LB_HS  

Generated Regeneration Scenarios:

1. **Local Retail Corridor**
   - encourage small businesses
   - improve street-level commercial activity

2. **Community Services Hub**
   - increase access to public services
   - activate underused urban spaces

3. **Mixed-Use Redevelopment**
   - combine housing and small retail
   - support gradual district revitalization

Scenario Fit Scores:

| Scenario | Fit Score |
|--------|--------|
| Local Retail Corridor | 0.82 |
| Community Services Hub | 0.76 |
| Mixed-Use Redevelopment | 0.68 |---

# Scenario Validation

Generated scenarios are validated to ensure they remain **consistent with the district profile**.

The validation step checks whether the proposed regeneration strategy logically matches the district typology.

---

# Project Pipeline
Municipal Open Data
↓
District Aggregation
↓
Urban Stress Indicators
↓
District Classification
↓
Scenario Generation
↓
Scenario Validation
↓
Interactive Map Demo


---

# Tools Used

This MVP leverages several tools introduced during the hackathon:

- **Google Stitch** – UI and demo interface
- **Antigravity** – logic flow and AI orchestration
- **OmniGuide** – project structuring support
- **AppClaimsEvaluator** – validation of project claims
- **Bright Data Integration Helper** – contextual enrichment

---

# Repository Structure
analysis/
generate_scenarios.py
validate_scenarios.py

data/
district_profiles_classified_1.csv
SDE_Code_Violations.csv
scenario_library.json
district_scenarios.json
scenario_validation.json
brightdata_montgomery_sample.csv
fit_matrix.csv

demo/
UI demo assets

docs/
additional notes


---

# MVP Scope

This project is a **prototype**, not a full urban planning system.

The goal is to demonstrate how **AI-assisted scenario exploration** could support city-level regeneration thinking using existing public datasets.

## Potential Use Case

This type of lightweight scenario engine could help cities quickly explore
possible regeneration strategies for different districts.

Instead of relying only on static dashboards, urban planners could use a tool
like this to test **alternative transformation paths** based on real municipal signals.

Possible applications include:

- identifying underperforming districts
- exploring regeneration strategies before policy design
- supporting strategic planning discussions
---

## Future Improvements

Possible extensions of this prototype include:

- integration of additional municipal datasets
- more advanced scoring models
- real-time business activity indicators
- richer scenario libraries
- deeper spatial analysis at the neighborhood level

## Limitations & Assumptions

This project is a lightweight prototype developed during a hackathon.

Several simplifying assumptions were made:

- district indicators are based on aggregated datasets
- the classification model uses simple High/Low thresholds
- regeneration scenarios are generated from a predefined scenario library
- spatial analysis is performed at the district level rather than at parcel level

The goal of the prototype is to demonstrate how municipal data signals
can support **AI-assisted exploration of urban regeneration strategies**.

# Team

World Wide Webs Hackathon  
Smart Cities & Infrastructure Track
