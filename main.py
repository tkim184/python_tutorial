import requests
from bs4 import BeautifulSoup

indeed_results = requests.get("https://www.indeed.com/jobs?q=python&limit=50")



