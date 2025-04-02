import pandas as pd
from gensim import corpora
from gensim.models import LdaModel

# Load cleaned data
print("Loading quantum_papers_cleaned.csv...")
df = pd.read_csv('quantum_papers_cleaned.csv')
texts = [text.split() for text in df['clean_abstract'].dropna()]
print(f"Loaded {len(texts)} abstracts for topic modeling.")

# Create dictionary and corpus
print("Creating dictionary and corpus...")
dictionary = corpora.Dictionary(texts)
corpus = [dictionary.doc2bow(text) for text in texts]

# Train LDA model (5 topics)
print("Training LDA model...")
lda_model = LdaModel(corpus=corpus, id2word=dictionary, num_topics=5, passes=10, random_state=42)

# Print topics
print("Topics found:")
for idx, topic in lda_model.print_topics(-1):
    print(f"Topic {idx}: {topic}")

# Assign dominant topic to each paper
print("Assigning dominant topics to papers...")
df['dominant_topic'] = [max(lda_model[corpus[i]], key=lambda x: x[1])[0] if i < len(corpus) else -1 for i in range(len(df))]

# Extract year from update_date
print("Extracting years...")
df['year'] = pd.to_datetime(df['update_date']).dt.year

# Group by year and topic
print("Analyzing topic trends over time...")
topic_trends = df.groupby(['year', 'dominant_topic']).size().unstack(fill_value=0)
print("Topic trends by year:")
print(topic_trends)

# Save the updated DataFrame with topics
df.to_csv('quantum_papers_with_topics.csv', index=False)
print("Saved DataFrame with topics to quantum_papers_with_topics.csv.")