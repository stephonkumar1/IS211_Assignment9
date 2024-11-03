#Stephon Kumar

import requests
from bs4 import BeautifulSoup

def scrape_world_series_champions():
    url = "https://en.wikipedia.org/wiki/List_of_World_Series_champions"
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, "html.parser")
        table = soup.find("table", class_="wikitable")
        if table:
            rows = table.find_all("tr")[1:]  # Skip the header row
            for row in rows:
                columns = row.find_all("td")
                if len(columns) >= 2:
                    year = columns[0].text.strip()
                    champion = columns[1].text.strip()
                    print(f"Year: {year}, Champion: {champion}")
        else:
            print("Could not find the World Series champions table.")
    else:
        print(f"Failed to retrieve data. Status code: {response.status_code}")

if __name__ == "__main__":
    print("Running Wikipedia scraper...")
    scrape_world_series_champions()
