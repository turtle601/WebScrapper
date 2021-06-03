import requests
from bs4 import BeautifulSoup

# indeed의 사이트의 모든 내용을 가져온다. 
indeed_result = requests.get("https://www.indeed.com/jobs?as_and=python&limit=50")

# BeatifulSoup를 통해 특정 데이터를 추출한다. 
indeed_soup = BeautifulSoup(indeed_result.text,"html.parser")

# div 태그에 pagination class로 이루어진 코드 추출
result = indeed_soup.find("div", class_ = "pagination")

# b태그와 span태그로 이루어진 내용을 answer라는 리스트에 담는다. 
answer = result.find_all("b") + result.find_all("span")

# answer의 항목 중 string으로 이루어진 것만 출력
for s in answer[:-2]:
    print(s.string)