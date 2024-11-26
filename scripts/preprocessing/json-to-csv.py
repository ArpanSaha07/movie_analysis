from pathlib import Path
import json
import csv

CSV_HEADER = ['Source ID', 'Source Name', 'Author', 'Title', 'Description', 'URL', 'URL To Image', 'Published At', 'Content']
def main():
    file_paths = Path('./data/DATA_F').glob('*')
    output_file_names = ['annotation_Ta.csv', 'annotation_Pe.csv', 'annotation_Ph.csv'] 

    data = []
    for file in file_paths:
        with file.open('r') as f:
            content = json.load(f)
        data += content['articles']


    for index, filename in enumerate(output_file_names):
        with Path('./data/annotation/' + filename).open('w') as f:
            writer = csv.writer(f)
            writer.writerow(CSV_HEADER)
            if (index == 0):
                articles = data[:150]
            elif (index == 1):
                articles = data[150:300]
            else: 
                articles = data[300:]
            for article in articles:
                writer.writerow([article['source']['id'], 
                                 article['source']['name'], 
                                 article['author'], 
                                 article['title'], 
                                 article['description'], 
                                 article['url'], 
                                 article['urlToImage'], 
                                 article['publishedAt'], 
                                 article['content']])

if __name__ == '__main__':
    main()
