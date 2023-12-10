import argparse
import pandas as pd
import matplotlib.pyplot as plt

def visualize_coded_topics(input_file):
    # Load the annotated data from the CSV file
    df = pd.read_csv(input_file)

    # Assuming 'Coded_Topics' column contains the annotated topics
    coded_topics = df['Coded Topic']

    # Count the occurrences of each coded topic
    topic_counts = coded_topics.value_counts()

    # Plot a pie chart
    plt.figure(figsize=(8, 8))
    plt.pie(topic_counts, labels=topic_counts.index, autopct='%1.1f%%', startangle=140)
    plt.legend(title='Coded Topics', loc='upper right', bbox_to_anchor=(1.2, 1))
    plt.title('Distribution of Coded Topics')
    plt.show()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Visualize the distribution of coded topics using a pie chart.")
    parser.add_argument("-i", "--input", help="Input CSV file path", required=True)
    args = parser.parse_args()

    # Call the function with the provided input file path
    visualize_coded_topics(args.input)

