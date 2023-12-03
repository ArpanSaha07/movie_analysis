import csv
import json
import argparse

def json_to_csv(json_data, csv_file):
    # Open the CSV file in write mode
    with open(csv_file, 'w', newline='', encoding='utf-8') as csvfile:
        # Create a CSV writer object
        csv_writer = csv.writer(csvfile)

        # Write the header row
        csv_writer.writerow(["Source Name", "Author", "Title", "Description", "URL", "Published At", "Content"])

        # Iterate through articles in the JSON data and write each row
        for article in json_data['articles']:
            source_name = article['source']['name'] if article['source'] and 'name' in article['source'] else ''
            author = article['author'] if 'author' in article else ''
            title = article['title'] if 'title' in article else ''
            description = article['description'] if 'description' in article else ''
            url = article['url'] if 'url' in article else ''
            published_at = article['publishedAt'] if 'publishedAt' in article else ''
            content = article['content'] if 'content' in article else ''

            # Write the row to the CSV file
            csv_writer.writerow([source_name, author, title, description, url, published_at, content])

if __name__ == "__main__":
    # Set up command-line argument parsing
    parser = argparse.ArgumentParser(description='Convert JSON to CSV.')
    parser.add_argument('-i', '--input', required=True, help='Path to the input JSON file')
    parser.add_argument('-o', '--output', required=True, help='Path to the output CSV file')
    args = parser.parse_args()

    # Load JSON data from the input file
    with open(args.input, 'r', encoding='utf-8') as json_file:
        data = json.load(json_file)

    # Call the function to convert JSON to CSV
    json_to_csv(data, args.output)

    print(f"CSV file '{args.output}' has been created.")
