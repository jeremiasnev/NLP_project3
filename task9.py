import json
from collections import Counter
import matplotlib.pyplot as plt
import pandas as pd

# Load sentiment data from the TSV file
sentiment_filepath = "SELF-FEIL-main/SELF.tsv"
sentiment_df = pd.read_csv(sentiment_filepath, sep="\t")
sentiment_dict = {}
for index, row in sentiment_df.iterrows():
    word = row['word'].lower() 
    sentiment_scores = {'positive': row['positive'], 'negative': row['negative']}
    sentiment_dict[word] = sentiment_scores

# Load the JSON data for Query 1 and Query 2
Q1_path = "Query1.json"
Q2_path = "Query2.json"

# Load datasets
with open(Q1_path, encoding='utf-8') as f:
    data1 = json.load(f)
with open(Q2_path, encoding='utf-8') as f:
    data2 = json.load(f)

# Function to process sentiment data for a given query data
def process_sentiment(data, sentiment_dict):
    positives = [[] for _ in range(17)]
    negatives = [[] for _ in range(17)]

    for item in data:
        if "date" in item:
            year = int(item["date"].split("-")[0])
            if 2001 <= year <= 2017:
                idx = year - 2001
                if "content" in item and "stemmed" in item:
                    content = item["content"]
                    stemmed = item["stemmed"]
                    pos_ = []
                    neg_ = []

                    for i, word in enumerate(content):
                        word_stemmed = stemmed[i].lower()
                        word = word.lower()

                        # Check both original and stemmed word in sentiment dictionary
                        if word in sentiment_dict:
                            word_scores = sentiment_dict[word]
                            pos_.append(word_scores["positive"])
                            neg_.append(word_scores["negative"])
                        elif word_stemmed in sentiment_dict:
                            word_scores = sentiment_dict[word_stemmed]
                            pos_.append(word_scores["positive"])
                            neg_.append(word_scores["negative"])

                    positives[idx].append(sum(pos_))
                    negatives[idx].append(sum(neg_))

    # Calculate total and average sentiment for each year
    positives_total = [sum(year) for year in positives]
    negatives_total = [sum(year) for year in negatives]
    pos_avg = [0] * 17
    neg_avg = [0] * 17

    for i in range(17):
        total_score = positives_total[i] + negatives_total[i]
        if total_score > 0:
            pos_avg[i] = positives_total[i] / total_score
            neg_avg[i] = negatives_total[i] / total_score

    return pos_avg, neg_avg

# Process sentiment for both Query 1 and Query 2
q1_pos_avg, q1_neg_avg = process_sentiment(data1, sentiment_dict)
q2_pos_avg, q2_neg_avg = process_sentiment(data2, sentiment_dict)

years = list(range(2001, 2018))
mid_marker = [0.5] * 17

# Plot the results for Query 1
plt.figure(figsize=(10, 6))
plt.plot(years, q1_pos_avg, marker='o', color='b', linestyle='-', linewidth=2, label='Positive Sentiment (Q1)')
# Plots negative sentiment scores also, easier to visualize without plotting vvv
#plt.plot(years, q1_neg_avg, marker='o', color='r', linestyle='-', linewidth=2, label='Negative Sentiment (Q1)')
plt.plot(years, mid_marker, color='g', linestyle='-', linewidth=2, label='Mid-point (0.5)')
plt.title("Yearly Evolution of Sentiment Scores for Query 1")
plt.xlabel("Year")
plt.ylabel("Normalized Sentiment Score")
plt.grid(True)
plt.legend()
plt.show()

# Plot the results for Query 2
plt.figure(figsize=(10, 6))
plt.plot(years, q2_pos_avg, marker='o', color='b', linestyle='-', linewidth=2, label='Positive Sentiment (Q2)')
plt.plot(years, mid_marker, color='g', linestyle='-', linewidth=2, label='Mid-point (0.5)')
plt.title("Yearly Evolution of Sentiment Scores for Query 2")
plt.xlabel("Year")
plt.ylabel("Normalized Sentiment Score")
plt.grid(True)
plt.legend()
plt.show()
