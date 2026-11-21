
import requests
import pandas as pd
import time
import logging

from bs4 import BeautifulSoup
from urllib.parse import urljoin

BASE_URL = "https://books.toscrape.com/"

logging.basicConfig(
    level=logging.INFO,
    format="%(levelname)s: %(message)s"
)

def extract_product(product, page_url):
    title = product.select_one('h3 a')['title']

    price_text = product.select_one('.price_color').get_text(strip=True)
    price = float(price_text.replace('Â£', '').replace('£', '').strip())

    rating = product.select_one('.star-rating')['class'][-1]
    availability = product.select_one('.availability').get_text(strip=True)

    product_url = urljoin(
        page_url,
        product.select_one('h3 a')['href']
    )

    image_url = urljoin(
        page_url,
        product.select_one('.image_container img')['src']
    )

    return {
        'title': title,
        'price': price,
        'currency': 'GBP',
        'rating': rating,
        'availability': availability,
        'product_url': product_url,
        'image_url': image_url
    }


def scrape_all_pages(start_url=BASE_URL):
    all_products = []
    current_url = start_url
    page_number = 1

    session = requests.Session()
    session.headers.update({
        'User-Agent': 'Mozilla/5.0 (compatible; EducationalBookScraper/1.0)'
    })

    while current_url:
        logging.info(f"Scraping page {page_number}")

        try:
            response = session.get(current_url, timeout=15)
            response.raise_for_status()

            soup = BeautifulSoup(response.text, 'html.parser')
            products = soup.find_all('article', class_='product_pod')

            for product in products:
                try:
                    product_data = extract_product(product, current_url)
                    product_data['page_number'] = page_number
                    all_products.append(product_data)

                except (AttributeError, KeyError, ValueError) as error:
                    logging.warning(f"Product extraction failed: {error}")

            next_button = soup.select_one('li.next a')

            if next_button:
                current_url = urljoin(current_url, next_button['href'])
                page_number += 1
                time.sleep(1)
            else:
                current_url = None

        except requests.exceptions.RequestException as error:
            logging.error(f"Request failed on page {page_number}: {error}")
            break

    session.close()

    df = pd.DataFrame(all_products)

    if not df.empty:
        df.to_csv('scraped_books.csv', index=False, encoding='utf-8')

    logging.info(f"Scraping finished. Total products: {len(df)}")

    return df


if __name__ == "__main__":
    books_df = scrape_all_pages()
    print("\nScraped dataset shape:", books_df.shape)
    print(books_df.head())
