import json
import pandas as pd
import re
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer

# Download NLTK data
import nltk
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')

# Load and filter in chunks
print("Starting to load and filter the JSON file...")
filtered_data = []
max_papers_to_process = 50000  # Adjust as needed
count = 0

with open('arxiv-metadata-oai-snapshot.json', 'r') as f:
    for line in f:
        if count >= max_papers_to_process:
            break
        try:
            entry = json.loads(line)
            count += 1
            if count % 10000 == 0:
                print(f"Processed {count} papers...")
            title = str(entry.get('title', '')).lower()
            abstract = str(entry.get('abstract', '')).lower()
            if 'quantum' in title or 'quantum' in abstract:
                filtered_data.append(entry)
        except Exception as e:
            print(f"Error processing entry: {e}")
            continue

print(f"Processed {count} papers in total.")
print(f"Found {len(filtered_data)} quantum-related papers after filtering.")

# Save to a DataFrame and then CSV
if filtered_data:
    print("Saving filtered data to CSV...")
    df = pd.DataFrame(filtered_data)[['id', 'title', 'abstract', 'update_date']]
    df.to_csv('quantum_papers.csv', index=False)
    print(f"Saved {len(df)} quantum-related papers to quantum_papers.csv.")
else:
    print("No quantum-related papers found. CSV not created.")

# Preprocess the text
print("Loading quantum_papers.csv...")
df = pd.read_csv('quantum_papers.csv')
print(f"Loaded {len(df)} papers.")

# Set up stopwords and lemmatizer
stop_words = set(stopwords.words('english'))
lemmatizer = WordNetLemmatizer()

# Define cleaning function
def clean_text(text):
    if pd.isna(text):
        return ''
    text = re.sub(r'[^a-zA-Z\s]', '', text.lower())
    tokens = word_tokenize(text)
    tokens = [lemmatizer.lemmatize(word) for word in tokens if word not in stop_words and len(word) > 2]
    return ' '.join(tokens)

# Apply to abstracts
print("Cleaning abstracts...")
df['clean_abstract'] = df['abstract'].apply(clean_text)
df.to_csv('quantum_papers_cleaned.csv', index=False)
print("Text cleaning done! Saved to quantum_papers_cleaned.csv.")