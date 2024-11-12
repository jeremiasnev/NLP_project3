import json
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score

# Load data
Q1_path = "Query1.json"
Q2_path = "Query2.json"

with open(Q1_path, encoding='utf-8') as f:
    data1 = json.load(f)
with open(Q2_path, encoding='utf-8') as f:
    data2 = json.load(f)

# Initialize data storage for vocabulary and word counts
q1_vocab = [set() for _ in range(17)]
q2_vocab = [set() for _ in range(17)]
q1_wordcount = [0] * 17
q2_wordcount = [0] * 17

# Extract data for Query 1
for item in data1:
    if "date" in item:
        year = int(item["date"].split("-")[0])
        if 2001 <= year <= 2017:
            idx = year - 2001
            if "stemmed" in item:
                content = item["stemmed"]
                q1_wordcount[idx] += len(content)
                q1_vocab[idx].update(content)

# Extract data for Query 2
for item in data2:
    if "date" in item:
        year = int(item["date"].split("-")[0])
        if 2001 <= year <= 2017:
            idx = year - 2001
            if "stemmed" in item:
                content = item["stemmed"]
                q2_wordcount[idx] += len(content)
                q2_vocab[idx].update(content)

q1_vocab_size = [len(vocab) for vocab in q1_vocab]
q2_vocab_size = [len(vocab) for vocab in q2_vocab]

# Define a function to test Heap's Law using a log-log transformation
def test_heaps_law(word_counts, vocab_sizes, query_name):
    word_counts_log = np.log(word_counts)
    vocab_sizes_log = np.log(vocab_sizes)
    model = LinearRegression().fit(word_counts_log.reshape(-1, 1), vocab_sizes_log)
    predicted_log_vocab = model.predict(word_counts_log.reshape(-1, 1))

    # Calculate R-squared and adjusted R-squared
    r_squared = r2_score(vocab_sizes_log, predicted_log_vocab)
    n = len(word_counts)
    p = 2
    adj_r_squared = 1 - (1 - r_squared) * (n - 1) / (n - p - 1)

    # Plot results
    plt.figure(figsize=(10, 6))
    plt.scatter(word_counts_log, vocab_sizes_log, color='orange', label='Actual Data')
    plt.plot(word_counts_log, predicted_log_vocab, color='blue', label='Fitted Line')
    plt.xlabel('Log of Word Count')
    plt.ylabel('Log of Vocabulary Size')
    plt.title(f"Heap's Law for {query_name} - Log-Log Plot")
    plt.legend()
    plt.show()

    print(f"Heap's Law results for {query_name}:")
    print(f"R-squared: {r_squared:.4f}")
    print(f"Adjusted R-squared: {adj_r_squared:.4f}\n")

# Test Heap's Law for Query 1 and Query 2
test_heaps_law(q1_wordcount, q1_vocab_size, "Query 1")
test_heaps_law(q2_wordcount, q2_vocab_size, "Query 2")
