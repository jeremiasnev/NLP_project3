import json
import matplotlib.pyplot as plt

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

q1_wordlist = [{} for _ in range(17)]
q2_wordlist = [{} for _ in range(17)]
q1_full_wordlist = {}
q2_full_wordlist = {}

# Extract data for Query 1
for item in data1:
    if "date" in item:
        year = int(item["date"].split("-")[0])
        if 2001 <= year <= 2017:
            idx = year - 2001
            if "stemmed" in item:
                content = item["stemmed"]

                # Add words to dictionaries
                for word in content:
                    w = word.lower()
                    if w not in stopwords and len(w) > 1:
                        if w in q1_wordlist[idx]:
                            q1_wordlist[idx][w] += 1
                        else:
                            q1_wordlist[idx][w] = 1
                        if w in q1_full_wordlist:
                            q1_full_wordlist[w]+=1
                        else:
                            q1_full_wordlist[w]=1

# Extract data for Query 2
for item in data2:
    if "date" in item:
        time = item["date"]
        year = int(item["date"].split("-")[0])
        if 2001 <= year <= 2017:
            idx = year - 2001
            if "stemmed" in item:
                content = item["stemmed"]

                # Add words to dictionaries
                for word in content:
                    w = word.lower()
                    if w not in stopwords and len(w) > 1:
                        if w in q2_wordlist[idx]:
                            q2_wordlist[idx][w] += 1
                        else:
                            q2_wordlist[idx][w] = 1
                        if w in q2_full_wordlist:
                            q2_full_wordlist[w]+=1
                        else:
                            q2_full_wordlist[w]=1

sorted_q1_wordlist = []
sorted_q2_wordlist = []

# Sort dictionaries
for year_dict in q1_wordlist:
    sorted_year = sorted(year_dict.items(), key=lambda item: item[1], reverse=True)
    sorted_q1_wordlist.append(sorted_year)
for year_dict in q2_wordlist:
    sorted_year = sorted(year_dict.items(), key=lambda item: item[1], reverse=True)
    sorted_q2_wordlist.append(sorted_year)

# Print 10 most common words per year
i = 2001
for year in sorted_q1_wordlist:
    print(i)
    for word in year[:10]:
        print(word)
    print("\nNext year\n")
    i+=1

i = 2001
for year in sorted_q2_wordlist:
    print(i)
    for word in year[:10]:
        print(word)
    print("\nNext year\n")
    i+=1

# Print 10 most common words across all years

print("\n-- Overall Top 10 Words Q1 --\n")
sorted_wordlist = sorted(q1_full_wordlist.items(), key=lambda item: item[1], reverse=True)
for word, count in sorted_wordlist[:10]:
    print(f"{word}: {count}")

print("\n-- Overall Top 10 Words Q2 --\n")
sorted_wordlist = sorted(q2_full_wordlist.items(), key=lambda item: item[1], reverse=True)
for word, count in sorted_wordlist[:10]:
    print(f"{word}: {count}")