#Stephon Kumar

import requests
from bs4 import BeautifulSoup

def scrape_cbs_football_stats():
    url = "https://www.cbssports.com/nfl/stats/player/passing/nfl/regular/qualifiers/"
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, "html.parser")
        players_table = soup.find("table")
        if players_table:
            rows = players_table.find_all("tr")[1:21]  # Get the top 20 players
            for row in rows:
                columns = row.find_all("td")
                if len(columns) >= 5:
                    player_name = columns[0].text.strip()
                    position = columns[1].text.strip()
                    team = columns[2].text.strip()
                    touchdowns = columns[4].text.strip()
                    print(f"Player: {player_name}, Position: {position}, Team: {team}, Touchdowns: {touchdowns}")
        else:
            print("Could not find the players table.")
    else:
        print(f"Failed to retrieve data. Status code: {response.status_code}")

if __name__ == "__main__":
    print("Running scraper one...")
    scrape_cbs_football_stats()
