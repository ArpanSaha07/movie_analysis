import argparse
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer

def compute_top_words(input_file, output_file):
    # Load the annotated data from the CSV file
    df = pd.read_csv(input_file)

    # Assuming 'Content' column contains the article text and 'Coded_Topics' column contains the annotated topics
    content_data = df['Content'].astype(str)
    coded_topics = df['Coded Topic']

    # Initialize TfidfVectorizer
    tfidf_vectorizer = TfidfVectorizer(stop_words='english')

    # Transform the content data to a TF-IDF matrix
    tfidf_matrix = tfidf_vectorizer.fit_transform(content_data)

    # Get the feature names (words) from the TF-IDF matrix
    feature_names = tfidf_vectorizer.get_feature_names_out()

    # Create a DataFrame to store the top 10 words for each category
    top_words_df = pd.DataFrame(index=range(10))

    # Iterate through each unique category in 'Coded_Topics'
    for category in coded_topics.unique():
        # Filter the data for the specific category
        category_indices = coded_topics[coded_topics == category].index
        category_tfidf_matrix = tfidf_matrix[category_indices, :]

        # Check if the category_tfidf_matrix is not empty
        if category_tfidf_matrix.shape[0] != 0:
            # Calculate the average TF-IDF scores for each word in the category
            avg_tfidf_scores = category_tfidf_matrix.mean(axis=0).A1

            # Get the indices of the top 10 words
            top_word_indices = avg_tfidf_scores.argsort()[-10:][::-1]

            # Get the actual words from the feature names
            top_words = [feature_names[idx] for idx in top_word_indices]

            # Add the top words to the DataFrame with the category as the column name
            top_words_df[category] = top_words

    # Save the top words DataFrame to a CSV file
    top_words_df.to_csv(output_file, index=False)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Compute top words using TF-IDF scores.")
    parser.add_argument("-i", "--input", help="Input CSV file path", required=True)
    parser.add_argument("-o", "--output", help="Output CSV file path", required=True)
    args = parser.parse_args()

    # Call the function with provided input and output file paths
    compute_top_words(args.input, args.output)
