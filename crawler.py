import requests
from bs4 import BeautifulSoup
import csv

HEADERS = {
    "User-Agent": "Mozilla/5.0"
}

def get_article_links(category_url):
    links = []
    print(f"Đang truy cập: {category_url}")
    res = requests.get(category_url, headers=HEADERS)

    if res.status_code != 200:
        print(f"Lỗi truy cập: {res.status_code}")
        return []

    soup = BeautifulSoup(res.text, "html.parser")
    articles = soup.select("div.klw-top-news ul li h3 a")

    if not articles:
        print("❌ Không tìm thấy bài viết nào.")
    else:
        print(f"✅ Tìm thấy {len(articles)} bài viết.")

    for a in articles:
        link = a.get("href")
        title = a.get_text(strip=True)
        if link and link.startswith("/"):
            link = "https://kenh14.vn" + link
        links.append((title, link))

    return links

if __name__ == "__main__":
    category_url = "https://kenh14.vn/cong-nghe.chn"
    links = get_article_links(category_url)

    # Ghi ra file CSV
    csv_file = "kenh14_links.csv"
    with open(csv_file, "w", encoding="utf-8", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["Tiêu đề", "Link bài viết"])
        for title, link in links:
            writer.writerow([title, link])

    print(f"✅ Đã ghi {len(links)} bài viết vào file {csv_file}")
    # Kiểm tra lại nội dung file CSV
print("\n📄 Nội dung file CSV:")
with open(csv_file, "r", encoding="utf-8") as f:
    for line in f.readlines():
        print(line.strip())