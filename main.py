import requests
from bs4 import BeautifulSoup

# 키워드 목록
KEYWORDS = ['통합 콜센터', '1388', '전화상담', '희망', '청소년']

# 알리오 채용 공고 URL
URL = "https://www.alioplus.go.kr/news/recruitList.do"

def fetch_announcements():
    response = requests.get(URL)
    response.encoding = 'utf-8'
    soup = BeautifulSoup(response.text, "html.parser")
    
    items = soup.select(".list-typeA li")  # 게시물 목록
    results = []
    
    for item in items:
        title = item.select_one(".tit").text.strip()
        link = "https://www.alioplus.go.kr" + item.select_one("a")["href"]
        
        if any(keyword in title for keyword in KEYWORDS):
            results.append(f"[{title}]({link})")
    
    return results

if __name__ == "__main__":
    matches = fetch_announcements()
    if matches:
        print("📢 새 공고 발견!\n" + "\n".join(matches))
    else:
        print("오늘은 해당 키워드 공고가 없습니다.")
