# crawler.py
import requests
from bs4 import BeautifulSoup
import pandas as pd
from datetime import datetime
import os

HEADERS = {
    "User-Agent": "Mozilla/5.0"
}

def get_article_links(category_url, max_pages=5):
    links = []
    for page in range(1, max_pages + 1):
        url = f"{category_url}/trang-{page}.chn"
        res = requests.get(url, headers=HEADERS)
        if res.status_code != 200:
            break
        soup = BeautifulSoup(res.text, "html.parser")
        articles = soup.select("article.knswli a.knswli-title")
        for a in articles:
            link = a["href"]
            if link.startswith("/"):
                link = "https://kenh14.vn" + link
            links.append(link)
    return list(set(links))

def get_article_data(url):
    res = requests.get(url, headers=HEADERS)
    soup = BeautifulSoup(res.text, "html.parser")
    try:
        title = soup.select_one("h1.kbwc-title").get_text(strip=True)
        desc = soup.select_one("h2.kbwc-sapo")
        description = desc.get_text(strip=True) if desc else ""
        image_tag = soup.select_one(".VCSortableInPreviewMode img")
        image = image_tag["src"] if image_tag else ""
        content = "\n".join([p.get_text(strip=True) for p in soup.select(".VCSortableInPreviewMode p")])
        return {
            "title": title,
            "description": description,
            "image": image,
            "content": content,
            "url": url
        }
    except Exception as e:
        print(f"Lỗi khi đọc {url}: {e}")
        return None

def save_to_csv(data, output_dir="data"):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    today = datetime.now().strftime("%Y%m%d")
    df = pd.DataFrame(data)
    df.to_csv(f"{output_dir}/kenh14_news_{today}.csv", index=False, encoding="utf-8-sig")

def main():
    category_url = "https://kenh14.vn/cong-nghe.chn"
    links = get_article_links(category_url)
    data = []
    for link in links:
        article = get_article_data(link)
        if article:
            data.append(article)
    save_to_csv(data)

if __name__ == "__main__":
    main()
