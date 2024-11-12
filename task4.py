import json
import matplotlib.pyplot as plt

Q1_path = "Query1.json"
Q2_path = "Query2.json"

# Load datasets
with open(Q1_path, encoding='utf-8') as f:
    data1 = json.load(f)
with open(Q2_path, encoding='utf-8') as f:
    data2 = json.load(f)

q1_number_vs_tokens = [[] for _ in range(17)]
q2_number_vs_tokens = [[] for _ in range(17)]

# Extract data for Query 1
for item in data1:
    if "date" in item:
        year = int(item["date"].split("-")[0])
        if 2001 <= year <= 2017:
            idx = year - 2001
            if "content" in item:
                content = item["content"]
                tokens_count = len(content)
                q1_number_vs_tokens[idx].append(tokens_count)

# Extract data for Query 2
for item in data2:
    if "date" in item:
        year = int(item["date"].split("-")[0])
        if 2001 <= year <= 2017:
            idx = year - 2001
            if "content" in item:
                content = item["content"]
                tokens_count = len(content)
                q2_number_vs_tokens[idx].append(tokens_count)


# Define the years (2001 to 2017)
years = list(range(2001, 2018))

q1_number_vs_tokens_avg = [0] * 17
q2_number_vs_tokens_avg = [0] * 17
for i, year in enumerate(years):
    q1_number_vs_tokens_avg[i] = sum(q1_number_vs_tokens[i]) / len(q1_number_vs_tokens[i])
    q2_number_vs_tokens_avg[i] = sum(q2_number_vs_tokens[i]) / len(q2_number_vs_tokens[i])

# Plot the data
plt.figure(figsize=(10, 6))
plt.plot(years, q1_number_vs_tokens_avg, marker='o', color='b', linestyle='-', linewidth=2)

# Label the chart
plt.title("Yearly Evolution of Average Length of Threads Q1")
plt.xlabel("Year")
plt.ylabel("Average Length of Threads")

# Add grid and show plot
plt.grid(True)
plt.show()

# Plot the data
plt.figure(figsize=(10, 6))
plt.plot(years, q2_number_vs_tokens_avg, marker='o', color='r', linestyle='-', linewidth=2)

# Label the chart
plt.title("Yearly Evolution of Average Length of Threads Q2")
plt.xlabel("Year")
plt.ylabel("Average Length of Threads")

# Add grid and show plot
plt.grid(True)
plt.show()