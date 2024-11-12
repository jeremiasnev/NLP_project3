import json
import matplotlib.pyplot as plt
from wordcloud import WordCloud
import time

Q1_path = "Query1.json"
Q2_path = "Query2.json"
stopword_path = "stopwords.txt"

# Load stopwords
with open(stopword_path, encoding='utf-8') as f:
    stopwords = set(f.read().splitlines())

# Load datasets
with open(Q1_path, encoding='utf-8') as f:
    data1 = json.load(f)

with open(Q2_path, encoding='utf-8') as f:
    data2 = json.load(f)

q1_titles = [[] for _ in range(17)]
q2_titles = [[] for _ in range(17)]

# Function for extracting titles
def extract_titles(data, year_list):
    for item in data:
        if "date" in item and "title" in item:
            year = int(item["date"].split("-")[0])
            if 2001 <= year <= 2017:
                idx = year - 2001
                title = item["title"]
                cleaned_title = ' '.join([word.lower() for word in title.split() if len(word) > 1])
                year_list[idx].append(cleaned_title)

extract_titles(data1, q1_titles)
extract_titles(data2, q2_titles)

# Function for generating WordCloud
def generate_wordcloud(titles, query_number):
    for i, year_titles in enumerate(titles):
        year_text = ' '.join(year_titles) 
        wordcloud = WordCloud(stopwords=stopwords, width=800, height=400, background_color='white').generate(year_text)
        filename = f"graphs/task8_q{query_number}_y{2001+i}.png"
        wordcloud.to_file(filename)
        plt.figure(figsize=(8, 4))
        plt.imshow(wordcloud, interpolation='bilinear')
        plt.axis("off")
        plt.title(f"Query {query_number} - Year {2001 + i}")
        plt.tight_layout()
        plt.show()

generate_wordcloud(q1_titles, 1)
generate_wordcloud(q2_titles, 2)
