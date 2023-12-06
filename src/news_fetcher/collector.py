import argparse
from fetch_movie_news import fetch_latest_news
from pathlib import Path
import json

def main():
    parser = argparse.ArgumentParser(description="Collects news information based on keywords and lookup date")

    parser.add_argument(
        "-b", help="Number of days to lookback", default=30, type=int)
    parser.add_argument(
        "-i", help="Input file containing the news keywords", required=True)

    args = parser.parse_args()

    with open(args.i, 'r') as f:
        data = json.load(f)

    for value in data.values():
        print(value)

        data = fetch_latest_news(value, args.b)

        with open("movie.json", 'w') as f:
            json.dump(data, f, indent=4)      

if __name__ == "__main__":
    main()
    