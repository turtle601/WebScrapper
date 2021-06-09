import requests
from bs4 import BeautifulSoup

limit = 50

#해당 url의 페이지 숫자들을 가져온다.
def extract_indeed_page(url): 
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
def request_pages_url(pages,url):
    for page in pages:
        req = requests.get(f"{url}&start={page*limit}")
        print(req.status_code)
    return 

# 해당 페이지 안의 채용 목록 중 직군들만 나열
def request_jobs(page,url):
    page -= 1
    req = requests.get(f"{url}&start={page*limit}")
    soup = BeautifulSoup(req.text,"html.parser")
    
    results = soup.find_all("div", class_ = "jobsearch-SerpJobCard")
    
    for result in results:
        title = result.find("h2", class_ = "title").find("a")["title"]
        print(title)
    
    return 

# 해당 페이지 안의 채용 목록 중 회사만 나열
def request_company(page,url):
    page -= 1
    req = requests.get(f"{url}&start={page*limit}")
    soup = BeautifulSoup(req.text,"html.parser")
    
    results = soup.find_all("div", class_ = "jobsearch-SerpJobCard")

    for result in results:
        title = result.find("h2", class_ = "title").find("a")["title"]
        company = result.find("span", class_ = "company")
        
        company_link = company.find('a')
        
        if company_link is None:
            result = company.string
        else:
            result = company_link.string
        
        print(result.strip())    

    return 

#일자리 중 직군, 회사에 대한 내용만
def extract_job(html):
    title = html.find("h2", class_ = "title").find("a")["title"]
    company = html.find("span", class_ = "company")
    location = html.find("div", class_ = "recJobLoc")["data-rc-loc"]
    job_id = html["data-jk"]
    
    company_link = company.find('a')
        
    if company_link is None:
        company = company.string
    else:
        company = company_link.string

    company = company.strip()

    return {
        'title' : title, 
        'company': company ,
        'location': location,
        'link': f"https://www.indeed.com/viewjob?jk={job_id}"
        }

# 일자리 추출 - request_jobs() + requests_company 합병 
def extract_indeed_jobs(page,url):
    jobs = []
    page -= 1

    #입력받은 page를 가져옴
    req = requests.get(f"{url}&start={page*limit}")
    soup = BeautifulSoup(req.text,"html.parser")

    results = soup.find_all("div", class_ = "jobsearch-SerpJobCard")

    for result in results:
        job = extract_job(result)
        jobs.append(job)
    
    return jobs

# 최종
def get_indeed_jobs(word):
    
    url = f"https://www.indeed.com/jobs?as_and={word}&limit={limit}"
    indeed = []
    pages = extract_indeed_page(url)

    for page in pages:
        indeed += extract_indeed_jobs(page,url)
    
    return indeed