import json
import matplotlib.pyplot as plt

Q1_path = "Query1.json"
Q2_path = "Query2.json"

# Load datasets
with open(Q1_path, encoding='utf-8') as f:
    data1 = json.load(f)
with open(Q2_path, encoding='utf-8') as f:
    data2 = json.load(f)

q1_vocab = [set() for _ in range(17)]
q2_vocab = [set() for _ in range(17)]

# Extract data for Query 1
for item in data1:
    if "date" in item:
        time = item["date"]
        year = int(time.split("-")[0])
        if 2001 <= year <= 2017:
            idx = year - 2001
            if "stemmed" in item:
                content = item["stemmed"]
                for word in content:
                    q1_vocab[idx].update(word.lower())
            
# Extract data for Query 2
for item in data2:
    if "date" in item:
        time = item["date"]
        year = int(time.split("-")[0])
        if 2001 <= year <= 2017:
            idx = year - 2001
            if "stemmed" in item:
                content = item["stemmed"]
                for word in content:
                    q2_vocab[idx].update(word.lower())

q1_vocab_size = [0] * 17
q2_vocab_size = [0] * 17
years = list(range(2001, 2018))

q1_vocab_size = [len(vocab) for vocab in q1_vocab]
q2_vocab_size = [len(vocab) for vocab in q2_vocab]

# Plot the data
plt.figure(figsize=(10, 6))
plt.plot(years, q1_vocab_size, marker='o', color='b', linestyle='-', linewidth=2)

# Label the chart
plt.title("Yearly Evolution of Vocabulary Size Q1")
plt.xlabel("Year")
plt.ylabel("Average Vocabulary Size")

# Add grid and show plot
plt.grid(True)
plt.show()

# Plot the data
plt.figure(figsize=(10, 6))
plt.plot(years, q2_vocab_size, marker='o', color='r', linestyle='-', linewidth=2)

# Label the chart
plt.title("Yearly Evolution of Vocabulary Size Q2")
plt.xlabel("Year")
plt.ylabel("Average Vocabulary Size")

# Add grid and show plot
plt.grid(True)
plt.show()