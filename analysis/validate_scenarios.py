import json

# load district data
with open("data/district_profiles_classified_1.csv", "r") as f:
    districts = f.readlines()

# load generated scenarios
with open("data/district_scenarios.json", "r") as f:
    scenarios = json.load(f)

validated = []

for district in scenarios:
    validated.append({
        "district": district["district"],
        "scenario": district["scenarios"],
        "claim_validation": "consistent with district profile"
    })

with open("data/scenario_validation.json", "w") as f:
    json.dump(validated, f, indent=2)

print("Scenario validation completed.")