import json
import myxmlparser as parser
import os

# Directory containing the .vrt files
directory_path = 'suomi24-2001-2017-vrt-v1-1/vrt'

path_to_database = "Query1.json"
path_to_database2 = "Query2.json"

# Keywords for queries
synonyms_climate_change = ["lmastonmuu", "lmastonvai", "lmastomuu", "lmastovai"] #Q1
synonyms_climate_resilience = ["lmastonvak", "lmastonsäil", "lmastonsuo", "lmastosuo", "lmastokes"] #Q2

# Load the databases
db1 = parser.load_db(path_to_database)
db2 = parser.load_db(path_to_database2)


chunk_size = 10000  # Define how many lines to process in each chunk

def add_db(data, content, stemmed, database, path):
    new_entry = {**data, "content": content, "stemmed": stemmed}
    database.append(new_entry)

    # Write the updated data back to the JSON file
    with open(path, 'w', encoding='utf-8') as f:
        json.dump(database, f, ensure_ascii=False, indent=4)

def process_chunk(lines):
    content = []
    stemmed = []
    data = {}
    Q1detected = False
    Q2detected = False
    readNextLine = False

    # Iterate through each line in the input
    for line in lines:
        if readNextLine:
            if line.startswith("</sen"):
                readNextLine = False
                
                # If keywords for Q1 or Q2 was detected, add data to respective database
                if Q1detected:
                    add_db(data, content, stemmed, db1, path_to_database)
                    Q1detected = False
                if Q2detected:
                    add_db(data, content, stemmed, db2, path_to_database2)
                    Q2detected = False
                
                content = []
                stemmed = []
            else:
                # Split the current line into words and stems
                ln = line.split()
                word = ln[0].lower()
                stem = ln[2].lower()

                if any(synonym in word for synonym in synonyms_climate_change) or \
                   any(synonym in stem for synonym in synonyms_climate_change):
                    Q1detected = True

                if any(synonym in word for synonym in synonyms_climate_resilience) or \
                   any(synonym in stem for synonym in synonyms_climate_resilience):
                    Q2detected = True
                
                content.append(word)
                stemmed.append(stem)
        elif line.startswith("<sen"):
            readNextLine = True
        elif line.startswith("<tex"):
            data = parser.parse_line(line)


# Loop through all .vrt files in the specified directory
for filename in os.listdir(directory_path):
    if filename.startswith("s24_20") and filename.endswith(".vrt"):
        year = int(filename[4:8])  # Extract the year from the filename
        if 2001 <= year <= 2017: # Go trough only wanted years if needed
            file_path = os.path.join(directory_path, filename)
            print(f"Processing file: {filename}")

            with open(file_path, 'r', encoding='utf-8') as file:
                chunk = []
                for i, line in enumerate(file):
                    chunk.append(line)
                    # Process each chunk once it reaches the specified chunk size
                    if (i + 1) % chunk_size == 0:
                        process_chunk(chunk)
                        chunk = []  # Clear the chunk from memory
                        print(f"Processed {i + 1} lines in {filename}")

                # Process any remaining lines in the final chunk
                if chunk:
                    process_chunk(chunk)
                    print(f"Processed {i + 1} lines in {filename}")

            print(f"Finished processing file: {filename}")