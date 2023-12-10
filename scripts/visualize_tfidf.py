import argparse
import pandas as pd
import matplotlib.pyplot as plt

def visualize_tfidf_scores(input_file):
    # Load the TF-IDF data from the CSV file
    df = pd.read_csv(input_file)

    # Assuming the CSV file has columns like 'Category1_words', 'Category1_tfidf', 'Category2_words', 'Category2_tfidf', etc.
    # Extract columns related to words and TF-IDF scores
    words_columns = [col for col in df.columns if '_words' in col]
    tfidf_columns = [col for col in df.columns if '_tfidf' in col]

    # Plot bar charts for each category
    for words_col, tfidf_col in zip(words_columns, tfidf_columns):
        category_name = words_col.split('_')[0]  # Extract category name from column name

        # Sort the data by TF-IDF score
        sorted_data = df[[words_col, tfidf_col]].sort_values(by=tfidf_col, ascending=False)

        # Plot a bar chart
        plt.figure(figsize=(10, 6))
        plt.bar(sorted_data[words_col], sorted_data[tfidf_col], color='skyblue')
        plt.xlabel('Words')
        plt.ylabel('TF-IDF Score')
        plt.title(f'Top TF-IDF Scores for {category_name}')
        plt.xticks(rotation=45, ha='right')
        plt.tight_layout()
        plt.show()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Visualize TF-IDF scores using bar charts.")
    parser.add_argument("-i", "--input", help="Input CSV file path", required=True)
    args = parser.parse_args()

    # Call the function with the provided input file path
    visualize_tfidf_scores(args.input)
