from pathlib import Path
import json
import random

def main():
    files, articles = [], []
    filenames = Path('./DATA_F').glob('*')

    for filename in filenames:
        with filename.open() as f:
            files.append(json.load(f))

    for file in files:
        for article in file['articles']:
            articles.append(article)

    random.shuffle(articles)

    for x in range(4):
        with Path('./DATA_F/shuffled_' + str(x) + '.json').open(mode='w') as f:
            json.dump({'articles': articles[x*25:(x+1)*25]}, f, indent=4)

if __name__ == '__main__':
    main()
