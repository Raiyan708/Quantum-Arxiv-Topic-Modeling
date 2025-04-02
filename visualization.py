import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the DataFrame with topics
print("Loading quantum_papers_with_topics.csv...")
df = pd.read_csv('quantum_papers_with_topics.csv')

# Recreate topic trends (in case you run this script independently)
topic_trends = df.groupby(['year', 'dominant_topic']).size().unstack(fill_value=0)

# Plot trends
print("Creating topic trends plot...")
plt.figure(figsize=(12, 6))
for topic in topic_trends.columns:
    if topic != -1:  # Skip invalid topics
        plt.plot(topic_trends.index, topic_trends[topic], label=f'Topic {topic}')
plt.xlabel('Year')
plt.ylabel('Number of Papers')
plt.title('Topic Trends in Quantum Machine Learning Papers')
plt.legend()
plt.savefig('topic_trends.png')
plt.show()
print("Plot saved as topic_trends.png.")