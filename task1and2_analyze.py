import json

Q1_path = "Query1.json"
Q2_path = "Query2.json"

with open(Q1_path, encoding='utf-8') as f:
    data1 = json.load(f)
with open(Q2_path, encoding='utf-8') as f:
    data2 = json.load(f)

# Print amount of items from both Queries
print(f"Items in Query1: {len(data1)}")
print(f"Items in Query2: {len(data2)}")