# Quantum Machine Learning Topic Trends Analysis
Analyzes arXiv papers to uncover topics and trends in quantum machine learning.

## Methodology
- Filtered arXiv dataset for "quantum" keywords (processed 50,000 papers).
- Cleaned abstracts with NLTK (tokenization, lemmatization, stopword removal).
- Applied LDA with Gensim to identify 5 topics.
- Visualized topic trends over time with Matplotlib.

## Results
Identified topics like quantum states and algorithms, with growth trends from 2015-2025. See `topic_trends.png` for the visualization.

## How to Run
1. Install requirements: `pip install pandas nltk gensim matplotlib seaborn`
2. Run `data_processing.py`, then `topic_modeling.py`, then `visualization.py`.

## Outputs
- `quantum_papers.csv`: Filtered papers
- `quantum_papers_cleaned.csv`: Cleaned abstracts
- `quantum_papers_with_topics.csv`: Papers with assigned topics
- `topic_trends.png`: Trend graph