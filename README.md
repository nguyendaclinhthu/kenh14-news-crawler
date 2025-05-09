📰 Crawler Tin Tức Kênh14
Script tự động thu thập dữ liệu tin tức từ chuyên mục Công Nghệ của trang kenh14.vn.

🚀 Tính năng
Tự động thu thập các bài viết từ chuyên mục Công Nghệ.

Trích xuất thông tin chi tiết từng bài viết, bao gồm:

Tiêu đề

Mô tả

Hình ảnh

Nội dung bài viết

URL bài viết

Lưu dữ liệu vào file CSV với định dạng: kenh14_news_YYYYMMDD.csv.

Chạy tự động theo lịch (mỗi ngày lúc 6:00 sáng).

🧰 Yêu cầu
Python 3.x

Các thư viện Python (được liệt kê trong file requirements.txt):

beautifulsoup4

requests

pandas

schedule (nếu sử dụng tính năng lên lịch)

⚙️ Cài đặt
Cài đặt các thư viện cần thiết:

bash
Sao chép
Chỉnh sửa
pip install -r requirements.txt
Đảm bảo đã tạo thư mục data/ trong cùng thư mục với script để lưu trữ dữ liệu.

📝 Cách sử dụng
Chạy script crawler:

bash
Sao chép
Chỉnh sửa
python crawler.py
Script sẽ:

Gửi yêu cầu đến trang kenh14.vn, chuyên mục Công Nghệ.

Trích xuất thông tin từ các bài viết.

Lưu dữ liệu vào file CSV trong thư mục data/.

(Tùy chọn) Chạy script lên lịch:

bash
Sao chép
Chỉnh sửa
python scheduler.py
Script sẽ:

Tự động chạy crawler.py mỗi ngày lúc 6:00 sáng.

📁 Cấu trúc thư mục
kotlin
Sao chép
Chỉnh sửa
kenh14-news-crawler/
├── crawler.py
├── scheduler.py
├── requirements.txt
├── README.md
└── data/
    └── kenh14_news_YYYYMMDD.csv
📌 Lưu ý
Đảm bảo máy tính của bạn có kết nối internet khi chạy script.

Kiểm tra và cập nhật các selector trong crawler.py nếu trang kenh14.vn thay đổi cấu trúc HTML
