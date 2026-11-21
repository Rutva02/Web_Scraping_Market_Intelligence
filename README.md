# E-Commerce Book Catalogue Scraping & Market Intelligence

## Project Overview

This project demonstrates an end-to-end web scraping and data analysis workflow using Python.

Product information is collected from [Books to Scrape](https://books.toscrape.com/), a sandbox website designed for practicing web scraping techniques.

The project extracts book information from all 50 catalogue pages, processes and validates the collected data, and performs exploratory data analysis to identify pricing patterns, rating distributions, and product availability.

## Project Objectives

- Scrape product information from multiple website pages.
- Automate pagination to collect the complete catalogue.
- Extract and structure relevant product attributes.
- Clean and validate the scraped dataset.
- Analyze book prices, ratings, and availability.
- Investigate the relationship between product prices and ratings.
- Create meaningful visualizations to communicate findings.

## Technologies Used

| Technology | Purpose |
|---|---|
| Python | Core programming language |
| Requests | Sending HTTP requests |
| BeautifulSoup | HTML parsing and data extraction |
| Pandas | Data cleaning and analysis |
| Matplotlib | Data visualization |
| Google Colab | Development environment |
| Git & GitHub | Version control and project hosting |

## Dataset Information

The final cleaned dataset contains **1,000 book records and 10 columns**.

| Column | Description |
|---|---|
| title | Book title |
| price | Book price |
| currency | Currency (GBP) |
| rating | Original rating category |
| availability | Product availability status |
| product_url | Individual product page URL |
| image_url | Product image URL |
| page_number | Catalogue page from which the product was scraped |
| rating_score | Numerical rating from 1 to 5 |
| price_category | Price classification |

### Data Quality Checks

The collected dataset was checked for:

- Missing values
- Duplicate product URLs
- Invalid or non-positive prices
- Rating conversion errors
- Consistent page-level product counts

The dataset contains 1,000 records, with no missing values, duplicate product URLs, or invalid prices.

## Exploratory Data Analysis

The following analyses were performed:

### 1. Price Analysis
- Average and median book prices
- Minimum and maximum prices
- Price distribution
- Price category distribution

### 2. Rating Analysis
- Distribution of ratings from 1 to 5
- Average book rating
- Identification of highly rated books

### 3. Price and Rating Relationship
- Average price across rating groups
- Price versus rating scatter plot
- Pearson correlation analysis
- Box plot comparison of prices by rating

### 4. Availability Analysis
- Product availability counts
- Availability percentages

## Key Findings

| Metric | Result |
|---|---:|
| Total books scraped | 1,000 |
| Catalogue pages processed | 50 |
| Average price | £35.07 |
| Median price | £35.98 |
| Minimum price | £10.00 |
| Maximum price | £59.99 |
| Average rating | 2.92 / 5 |
| Price-rating correlation | 0.0282 |
| In-stock products | 1,000 (100%) |

### Key Insights

1. The average book price is £35.07, while the median price is £35.98.
2. Book prices range from £10.00 to £59.99.
3. The average rating across the catalogue is approximately 2.92 out of 5.
4. The Pearson correlation between price and rating is 0.0282, indicating a negligible linear relationship.
5. All 1,000 collected products were listed as in stock during the scraping process.
6. Some lower-priced books have high ratings, while some expensive books have low ratings.

## Visualizations

Four visualizations were created to communicate the findings:

| Visualization | Purpose |
|---|---|
| `price_distribution.png` | Understand the distribution of book prices |
| `rating_distribution.png` | Compare the number of books across rating levels |
| `price_vs_rating.png` | Examine the relationship between price and rating |
| `price_by_rating.png` | Compare price distributions across rating groups |

All visualizations are available in the `visualizations/` directory.

## Project Structure

```text
Web_Scraping/
│
├── Web_Scraping.ipynb
├── scraper.py
├── README.md
├── scraped_books_cleaned.csv
├── book_analysis_summary.csv
│
└── visualizations/
    ├── price_distribution.png
    ├── rating_distribution.png
    ├── price_vs_rating.png
    └── price_by_rating.png
```

## Installation and Usage

### 1. Clone the Repository

git clone https://github.com/Rutva02/Web_Scraping_Market_Intelligence.git
cd Web_Scraping_Market_Intelligence

### 2. Install Dependencies

```bash
pip install requests beautifulsoup4 pandas matplotlib
```

### 3. Run the Scraper

```bash
python scraper.py
```

The scraper collects the catalogue data and exports it to `scraped_books.csv`.

### 4. Explore the Analysis

Open `Web_Scraping.ipynb` in Google Colab or Jupyter Notebook to explore the complete scraping, cleaning, and analysis workflow.

## Data Source

[Books to Scrape](https://books.toscrape.com/)

Books to Scrape is a sandbox website intended for web scraping practice. The collected information is used for educational and analytical purposes. This project does not represent a real-world live e-commerce marketplace.

## Limitations

- The analysis represents the catalogue information collected during the scraping session.
- Product availability may change over time.
- The website is a practice environment, so findings should not be generalized to the wider book market.
- The observed price-rating correlation does not establish causation.
