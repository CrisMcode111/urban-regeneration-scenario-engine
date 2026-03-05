import csv
import json
import os

data_dir = "data"

# Read fit_matrix.csv
fit_matrix = {}
with open(os.path.join(data_dir, "fit_matrix.csv"), 'r', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    for row in reader:
        dt = row['District_Type']
        fit_matrix[dt] = {
            "Stabilization": int(row["Stabilization"]),
            "Economic_Activation": int(row["Economic_Activation"]),
            "Public_Space_Climate": int(row["Public_Space_Climate"])
        }

# Read scenario_library.json
with open(os.path.join(data_dir, "scenario_library.json"), 'r', encoding='utf-8') as f:
    scenario_library = json.load(f)

# Read district_profiles_classified_1.csv
output = []
with open(os.path.join(data_dir, "district_profiles_classified_1.csv"), 'r', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    for row in reader:
        district_id = row['District']
        district_type = row['District_Type']
        
        if not district_id or not district_type:
            continue
            
        scenarios_for_type = scenario_library["district_types"].get(district_type, [])
        
        scenarios_out = []
        for s in scenarios_for_type:
            s_type = s["scenario_type"]
            fit_score = fit_matrix.get(district_type, {}).get(s_type, 0)
            scenarios_out.append({
                "scenario_type": s_type,
                "title": s["title"],
                "fit_score": fit_score,
                "actions": s["actions"][:3] # Ensure exactly 3 actions
            })
            
        # Ensure exactly 3 scenarios (assume JSON has 3 per type)
        scenarios_out = scenarios_out[:3]
        
        output.append({
            "district": district_id,
            "district_type": district_type,
            "scenarios": scenarios_out
        })

# Write output
with open(os.path.join(data_dir, "district_scenarios.json"), 'w', encoding='utf-8') as f:
    json.dump(output, f, indent=2)

print("Created data/district_scenarios.json successfully.")
