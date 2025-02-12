# scrape blog from tanyongsheng.com 
# idea: combine with github actions to update README.md file with new blog article release

import requests
from urllib.parse import urljoin
from datetime import datetime

blog_url = "https://tanyongsheng.com"
response = requests.get(urljoin(blog_url, "/wp-json/wp/v2/posts/"))
data = response.json()


for idx in len(data):
    title = data[idx]["title"]["rendered"]
    date = datetime.strptime(response.json()[0]["date"], "%d/%m/%y")
