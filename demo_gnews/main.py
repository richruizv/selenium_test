from gnews import GNews
from gnews import GNews

def run():
    news = GNews()
    print(news.get_news('Mexico'))

if __name__ == '__main__':
    run()

