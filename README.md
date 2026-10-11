# OTT Streaming Content Trend Analysis

**An Exploratory Data Analysis Project Using Netflix Data**

## Project Overview

This project explores Netflix's Movies and TV Shows dataset to identify content catalogue patterns, release-year trends, country-wise distribution, genre diversity, content ratings, and movie-duration patterns.

The objective is to demonstrate how data analytics can turn raw streaming catalogue data into meaningful insights and potential content strategy recommendations.

## Objectives

- Analyze the distribution of Movies and TV Shows.
- Explore content trends across release years.
- Identify countries with the highest representation in the dataset.
- Examine popular catalogue genres and content ratings.
- Study the distribution of movie durations.
- Prepare SQL queries for core aggregations.
- Develop three actionable content strategy recommendations.

## Tools and Technologies

- **Python** — Data analysis
- **Pandas** — Data cleaning and manipulation
- **Matplotlib / Seaborn** — Data visualization
- **SQL** — Aggregations and analytical queries
- **Google Colab** — Notebook development
- **GitHub** — Project version control and sharing

## Dataset

The project uses the Netflix Movies and TV Shows dataset, which contains **8,807 records and 12 columns**.

Dataset source: [Netflix Movies and TV Shows Dataset](https://github.com/shivamb/netflix-shows)

The dataset includes title, content type, director, cast, country, date added, release year, rating, duration, genre/category information, and description.

## Project Structure

```text
OTT_Streaming_Content_Analysis/
│
├── data/
├── notebook/
│   └── OTT_Content_Trend_Analysis.ipynb
├── reports/
│   └── content_strategy_memo.md
├── sql/
│   └── ott_analysis.sql
├── src/
├── visualizations/
├── README.md
└── .gitignore
```

## Data Cleaning and Analysis

The analysis includes:

1. Inspecting the dataset structure and data types.
2. Checking duplicate records and missing values.
3. Handling missing values in selected columns.
4. Converting date fields into a suitable format.
5. Exploring content types, release years, countries, genres, ratings, and movie durations.
6. Creating six exploratory data visualizations.

## Visualizations

The project includes six visualizations:

1. Movies vs. TV Shows distribution
2. Content distribution by release year
3. Top 10 countries represented
4. Top 10 individual genres
5. Content ratings distribution
6. Movie duration distribution

The corresponding chart images are maintained in the `visualizations/` directory.

## Key Findings

- Movies represent approximately **69.6%** of the dataset, while TV Shows account for approximately **30.4%**.
- The United States and India are among the countries with the highest representation.
- Genre and duration analysis provides a basis for investigating catalogue composition and potential content planning opportunities.

These findings describe catalogue patterns and should not be interpreted as direct measures of audience popularity or profitability.

## Content Strategy Recommendations

1. **Balance the content portfolio:** Evaluate opportunities for additional series and other formats using audience-demand evidence.
2. **Explore regional opportunities:** Combine country and genre analysis with regional audience preferences and licensing costs.
3. **Use data-driven content planning:** Compare genre and duration patterns with viewing hours, completion rates, and business costs before making acquisition decisions.

## SQL Analysis

The SQL script contains queries for:

- Total title count
- Movies vs. TV Shows
- Release-year trends
- Country-wise title counts
- Content ratings
- Content type percentages

## Limitations

- The dataset is a historical snapshot, not a live Netflix catalogue.
- Viewer engagement, revenue, subscriber behaviour, and licensing costs are not included.
- Catalogue counts alone cannot establish content success or profitability.
- Country and genre fields may contain multiple values that require careful splitting for detailed analysis.

## Conclusion

This project demonstrates an end-to-end introductory data analytics workflow involving data inspection, cleaning, exploratory visualization, SQL query preparation, and business recommendations.

## Author

**Diya Goel**

