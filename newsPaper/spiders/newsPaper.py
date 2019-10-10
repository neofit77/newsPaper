import scrapy
import csv
import nltk
import newspaper
from pathlib import Path
from newsPaper.items import newsPaperItem

csv_input = Path('newsPaper/csvInput')
csv_folder = csv_input.iterdir()
urls = []
for input_file in csv_folder:
    with open(csv_input/input_file.name, 'r') as file:
        links = csv.reader(file)
        for link in links:
            urls.append(link[0])

class newsCrawler (scrapy.Spider):
    name = 'news'
    start_urls = urls

    def parse(self, response):
        newsItem = newsPaperItem()
        article = newspaper.Article(response.url)
        article.download()
        article.parse()
        nltk.download('punkt')
        article.nlp()
        newsItem["Author_Name"] = article.authors
        newsItem['Publication_Date'] = article.publish_date
        newsItem['Keywords'] = article.keywords
        newsItem['Article_text'] = article.text
        yield newsItem



