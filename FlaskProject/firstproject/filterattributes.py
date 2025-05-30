import json

# Input and output file paths
input_path = "FlaskProject/firstproject/attr.json"
output_path = "filtered_attributes.json"

# Set of valid hierarchy codes
valid_codes = {
    "R220203000000", "R190704000000", "R190605000000", "R190308000000",
    "R220404000000", "R220104000000", "R040203000000", "R170200000000",
    "R040303000000", "R040209000000", "R190701000000", "R190703000000",
    "R220108000000", "R180201040000", "R220406000000", "R190107030000",
    "R190107020000", "R190802000000", "R040105000000", "R190107010000",
    "R190102070000", "R040208000000", "R180404000000", "R190103020000"
}

# Read JSON from file
with open(input_path, 'r', encoding='utf-8') as f:
    data = json.load(f)

# Filter attributes by hierarchy_code
filtered_attributes = [
    attr for attr in data.get("attributes", [])
    if attr.get("hierarchy_code") in valid_codes
]

# Create output JSON
output = {"attributes": filtered_attributes}

# Write filtered JSON to output file with pretty print
with open(output_path, 'w', encoding='utf-8') as f:
    json.dump(output, f, indent=2, ensure_ascii=False)

print(f"Filtered JSON saved to: {output_path}")
