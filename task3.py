import json
import matplotlib.pyplot as plt

Q1_path = "Query1.json"
Q2_path = "Query2.json"

# Load datasets
with open(Q1_path, encoding='utf-8') as f:
    data1 = json.load(f)
with open(Q2_path, encoding='utf-8') as f:
    data2 = json.load(f)

q1_number_vs_threads = [0] * 17
q2_number_vs_threads = [0] * 17

# Extract data for Query 1
for item in data1:
    if "date" in item:
        year = int(item["date"].split("-")[0])
        if 2001 <= year <= 2017:
            idx = year - 2001
            q1_number_vs_threads[idx]+=1

# Extract data for Query 2
for item in data2:
    if "date" in item:
        year = int(item["date"].split("-")[0])
        if 2001 <= year <= 2017:
            idx = year - 2001
            q2_number_vs_threads[idx]+=1

years = list(range(2001, 2018))

# Create subplots
fig, axs = plt.subplots(1, 2, figsize=(15, 6))

# Plot the number of threads for Q1
axs[0].plot(years, q1_number_vs_threads, marker='o', color='b', linestyle='-', linewidth=2)
axs[0].set_title("Yearly Evolution of Number of Threads Q1")
axs[0].set_xlabel("Year")
axs[0].set_ylabel("Number of Threads")
axs[0].grid(True)

# Plot the number of threads for Q2
axs[1].plot(years, q2_number_vs_threads, marker='o', color='r', linestyle='-', linewidth=2)
axs[1].set_title("Yearly Evolution of Number of Threads Q2")
axs[1].set_xlabel("Year")
axs[1].set_ylabel("Vocabulary Size")
axs[1].grid(True)

# Adjust layout and show the plots
plt.tight_layout()
plt.show()

# Calculate number of threads together
q_number_vs_threads = [0] * 17
for i, value in enumerate(q1_number_vs_threads):
    q_number_vs_threads[i] = value + q2_number_vs_threads[i]

# Plot the data
plt.figure(figsize=(10, 6))
plt.plot(years, q_number_vs_threads, marker='o', color='b', linestyle='-', linewidth=2)

# Label the chart
plt.title("Yearly Evolution of Number of Threads from both Queries")
plt.xlabel("Year")
plt.ylabel("Number of Threads")

# Add grid and show plot
plt.grid(True)
plt.show()