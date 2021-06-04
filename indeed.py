from typing import List
import requests
from bs4 import BeautifulSoup

limit = 50
url = f"https://www.indeed.com/jobs?as_and=python&limit={limit}"

#해당 url의 페이지 숫자들을 가져온다.
def extract_indeed_page(): 
    # indeed의 사이트의 모든 내용을 가져온다. 
    indeed_result = requests.get(url)

    # BeatifulSoup를 통해 특정 데이터를 추출한다. 
    indeed_soup = BeautifulSoup(indeed_result.text,"html.parser")

    # div 태그에 pagination class로 이루어진 코드 추출
    result = indeed_soup.find("div", class_ = "pagination")

    # b태그와 span태그로 이루어진 내용을 answer라는 리스트에 담는다. 
    extract_context = result.find_all("b") + result.find_all("span")
    
    pages = []
    
    # string이 있는 요소들만 result리스트에 삽입
    for p in extract_context[:-2]:
        pages.append(int(p.string))
    
    return pages

# 페이지들의 링크들을 request
def request_pages_url(pages):
    for page in pages:
        req = requests.get(f"{url}&start={page*limit}")
        print(req.status_code)
    return 