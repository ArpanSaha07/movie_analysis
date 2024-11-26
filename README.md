# Analysis of Movie Visibility and Reception on News Media

## Project Overview
This repository contains scripts and visualizations for our project analyzing the visibility and reception of movies in the media, with a focus on the historical drama *Napoleon*, released in late 2023. Using Python for data processing and visualization, we explore how *Napoleon* compares to four other contemporaneously released films in terms of thematic focus, public perception, and media engagement. Detailed description on the project can be found [here](https://github.com/ArpanSaha07/movie_analysis/blob/main/Report%20on%20Analysis%20of%20Movie%20Visibility%20and%20Reception%20on%20News%20Media%20of%20'Napoleon'.pdf).

## Data
We sourced over 600 news articles from **NewsAPI.org** between November 7th and December 4th, 2023. The movies analyzed are:

1. **The Marvels** (Action)
2. **The Hunger Games: Ballad of Songbirds and Snakes** (Action)
3. **Five Nights at Freddy’s** (Horror)
4. **Thanksgiving** (Horror)
5. **Napoleon** (Historical Drama)

Data preprocessing included:
- Filtering articles using targeted queries.
- Removing duplicates and null entries.
- Converting JSON data to CSV format for easier annotation and analysis.

## Methods
The dataset was categorized into six distinct topics through manual annotation and open coding:
1. **Box Office**: Commercial performance metrics.
2. **Cast**: Actor interviews and relationships.
3. **Lore**: Historical or fictional background.
4. **Production**: Technical aspects like cinematography and direction.
5. **Writing**: Plot and character analysis.
6. **Delivery**: Performance and dialogue delivery.

We calculated **Term Frequency-Inverse Document Frequency (TF-IDF)** scores to identify the top 10 words characterizing each topic. These scores provide a quantitative basis for understanding thematic focus.

## Visualizations
- **TF-IDF Topic Analysis**: Visualizations of the most relevant terms for each topic.
- **Topic Visualization Pie Charts**: Topic distribution for each movie, highlighting media focus and public engagement on each aspect of the movie.

The visualizations can be found in the [`visualizations/`](https://github.com/ArpanSaha07/movie_analysis/tree/main/Visualization) directory.

## Key Findings
1. **The Hunger Games** consistently showed the highest engagement across all topics, reflecting robust media attention.
2. **Napoleon**, while present across topics, showed comparatively lower engagement, suggesting a narrower media focus.
3. Articles categorized under "Box Office" had notable correlations with seasonal factors like Thanksgiving.

## Getting Started
### Prerequisites
- Python 3.7+
- Required libraries: `pandas`, `numpy`, `scikit-learn`, `matplotlib`

### Installation
Clone this repository:
```bash
git clone https://github.com/username/repo-name.git
cd repo-name
```

Install dependencies:
```bash
pip install -r requirements.txt
```

### Running the Analysis
1. **Data Preprocessing**: Run the scripts in `scripts/preprocessing/` to clean and prepare the dataset.
2. **TF-IDF Calculation**: Use the `tfidf.py` script to compute scores.
3. **Visualizations**: Execute scripts `visualize_tfidf.py` or `visualize_topics.py` to generate visual outputs.

---

Feel free to contribute by submitting a pull request or opening an issue! For inquiries, contact the team members.
