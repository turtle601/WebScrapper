import requests
from bs4 import BeautifulSoup

# indeed의 사이트의 모든 내용을 가져온다. 
indeed_result = requests.get("https://www.indeed.com/jobs?as_and=python&limit=50")

# BeatifulSoup를 통해 특정 데이터를 추출한다. 
indeed_soup = BeautifulSoup(indeed_result.text,"html.parser")

print(indeed_soup)