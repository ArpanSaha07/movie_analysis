from pathlib import Path
import json
import csv

CSV_HEADER = ['Source ID', 'Source Name', 'Author', 'Title', 'Description', 'URL', 'URL To Image', 'Published At', 'Content']
def main():
    file_paths = Path('./DATA_F').glob('shuffled_*')
    
    for file in file_paths:
        with file.open('r') as f:
            data = json.load(f)
        data = data['articles']

        with Path('./DATA_F_CSV/' + file.name[:-5] + '.csv').open('w') as f:
            writer = csv.writer(f)
            writer.writerow(CSV_HEADER)
            for article in data:
                writer.writerow([article['source']['id'], article['source']['name'], article['author'], article['title'], article['description'], article['url'], article['urlToImage'], article['publishedAt'], article['content']])




if __name__ == '__main__':
    main()
