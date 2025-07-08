import requests
from bs4 import BeautifulSoup
import csv

# Just a quick note: this is a simple demo scraper for learning.
# It grabs quotes from a practice website made for this purpose.
# Make sure to get permission before scraping other websites!

URL = "http://quotes.toscrape.com"

def scrape_quotes():
    all_quotes = []

    # We'll check out the first 5 pages
    for page_num in range(1, 6):
        print(f"Scraping page {page_num}...")
        response = requests.get(f"{URL}/page/{page_num}/")
        soup = BeautifulSoup(response.text, 'html.parser')

        # Find all the quotes on this page
        quotes = soup.find_all('div', class_='quote')

        for q in quotes:
            text = q.find('span', class_='text').get_text()
            author = q.find('small', class_='author').get_text()
            tags = [tag.get_text() for tag in q.find_all('a', class_='tag')]

            all_quotes.append({
                'text': text,
                'author': author,
                'tags': ", ".join(tags)
            })

    return all_quotes

def save_to_csv(quotes, filename='quotes.csv'):
    # Save the quotes to a CSV file
    with open(filename, 'w', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=['text', 'author', 'tags'])
        writer.writeheader()
        writer.writerows(quotes)

    print(f"\nSaved {len(quotes)} quotes to '{filename}'. Check it out!")

if __name__ == "__main__":
    quotes = scrape_quotes()
    save_to_csv(quotes)
