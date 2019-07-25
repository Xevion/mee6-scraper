from selenium import webdriver
from bs4 import BeautifulSoup
import time, pprint

class Leaderboard():
    def __init__(self, pages=1):
        self.update(pages)
        self.pp = pprint.PrettyPrinter()

    def parseEnding(self, n):
        if n.endswith("k"):
            n = float(n[:-1])
            n*=1000
        elif n.endswith("m"):
            n = float(n[:-1])
            n*=1000000
        if int(n) == n:
            n = int(n)
        return n

    def get(self):
        return self.users

    # Get the user listing off the ranks page and update the leaderboard data
    def update(self, pages=1):
        self.pages = pages
        self._get()

    def _get(self):
        url = "https://mee6.xyz/leaderboard/166630061217153024"
        browser = webdriver.Chrome()
        browser.get(url)
        for page in range(self.pages):
            browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(1)
        html = browser.page_source
        browser.quit()
        soup = BeautifulSoup(html, 'lxml')
        # Processing Web Page
        table_body = soup.find_all('div', attrs={'class':'leaderboardPlayer'})
        users = {}
        for entry in table_body:
            # User Info section
            userInfo = entry.find('div', attrs={'class':'leaderboardPlayerLeft'})
            rank = userInfo.find('div', attrs={'class':'leaderboardRank'}).string
            icon = userInfo.find('div', attrs={'class':'leaderboardPlayerIcon'}).find('img')['src']
            username = userInfo.find('div', attrs={'class':'leaderboardPlayerUsername'}).string

            # Stats section
            userStats = entry.find('div', attrs={'class':'leaderboardPlayerStats'}).find_all('div')
            messages = userStats[2].string
            experience = userStats[5].string
            percent = userStats[6]['class'][1][1:]
            level = userStats[9].string
            messages, experience = self.parseEnding(messages), self.parseEnding(experience)
            users[username] = {'rank':rank, 'icon':icon, 'messages':messages, 'percent': percent, 'experience':experience, 'level':level}
        self.users = users

    def print(self):
        self.pp.pprint(self.users)