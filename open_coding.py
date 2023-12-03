import pandas as pd
from nltk.tokenize import word_tokenize

def open_coding(csv_input, csv_output):
    # Read the CSV file
    df = pd.read_csv(csv_input)

    # Create an empty list to store coded topics
    coded_topics = []

    # Iterate through the articles for open coding
    for index, article in df.iterrows():
        # Print the title and opening for context
        print(f"Title: {article['Title']}")
        print(f"Opening: {article['Description']}")
        
        # Input for the coded topic
        coded_topic = input("Enter the coded topic (Press Enter to skip): ")

        # Append the coded topic to the list
        coded_topics.append(coded_topic)

        print("\n" + "=" * 50 + "\n")  # Separate articles for clarity

    # Add a new column with coded topics to the DataFrame
    df['Coded Topic'] = coded_topics

    # Save the DataFrame to a new CSV file
    df.to_csv(csv_output, index=False)

    print(f"CSV file '{csv_output}' has been created with coded topics.")

if __name__ == "__main__":
    import argparse

    # Set up command-line argument parsing
    parser = argparse.ArgumentParser(description='Perform open coding for topic identification.')
    parser.add_argument('-i', '--input', required=True, help='Path to the input CSV file')
    parser.add_argument('-o', '--output', required=True, help='Path to the output CSV file with coded topics')
    args = parser.parse_args()

    # Call the open_coding function
    open_coding(args.input, args.output)
