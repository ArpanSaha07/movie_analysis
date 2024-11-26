import json
import argparse

def remove_duplicates(json_data):
    seen_titles = set()
    unique_articles = []

    for article in json_data["articles"]:
        title = article["title"]
        if title not in seen_titles:
            seen_titles.add(title)
            unique_articles.append(article)

    json_data["articles"] = unique_articles
    return json_data

def main():
    # Set up argparse to get the input file as a command-line argument
    parser = argparse.ArgumentParser(description='Remove duplicate entries from a JSON file.')
    parser.add_argument('input_file', help='Path to the input JSON file')
    args = parser.parse_args()

    # Read the JSON file
    with open(args.input_file, 'r') as file:
        json_data = json.load(file)

    # Remove duplicates
    updated_json_data = remove_duplicates(json_data)

    # Print the total number of entries
    total_entries = len(updated_json_data["articles"])
    print(f"Total number of entries: {total_entries}")

    # Optionally, you can write the updated JSON data back to the file
    output_file = 'updated_' + args.input_file
    with open(output_file, 'w') as file:
        json.dump(updated_json_data, file, indent=2)

    print(f"Updated JSON data written to {output_file}")

if __name__ == "__main__":
    main()
