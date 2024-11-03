#Stephon Kumar
import requests
from bs4 import BeautifulSoup

def scrape_apple_stock_data():
    url = "https://finance.yahoo.com/quote/AAPL/history/?p=AAPL"
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, "html.parser")
        rows = soup.find_all("tr", class_="BdT")
        for row in rows:
            columns = row.find_all("td")
            if len(columns) >= 6:
                date = columns[0].text.strip()
                close_price = columns[4].text.strip()
                print(f"Date: {date}, Close Price: {close_price}")
    else:
        print(f"Failed to retrieve data. Status code: {response.status_code}")

if __name__ == "__main__":
    print("Running scraper two...")
    scrape_apple_stock_data()
