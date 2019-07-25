import requests, json, pprint

class Fetch():
    def __init__(self, total=999):
        self.total = total
        self.retrieve()

    def retrieve(self, total=None):
        if total==None: total=self.total
        url = "https://mee6.xyz/api/plugins/levels/leaderboard/166630061217153024?limit={}&page={}"
        dataset = []
        pages = total // 999 # Process n amount of pages
        print(pages)
        last = total % 999 # Then process the last n amount of pages in addition
        print(last)
        for i in range(pages):
            resp = requests.get(url.format(999, i))
            dataset.append(resp.json()['players'])
        if last > 0:
            resp = requests.get(url.format(last, pages+1))
            dataset.append(resp.json()['players'])
        self.data = dataset

    def get(self):
        return self.data

pp = pprint.PrettyPrinter()    
fetcher = Fetch(1005)
dataset = fetcher.get()

print(len(dataset[]))
# pp.pprint(dataset[0]['players'])