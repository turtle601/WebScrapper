import requests
from bs4 import BeautifulSoup

url = f"https://stackoverflow.com/jobs?q=python&sort=i"

def so_lastpage():
    so_result = requests.get(url)
    so_soup = BeautifulSoup(so_result.text,"html.parser")

    pages = so_soup.find("div", class_ = "s-pagination").find_all("a")
    last_page = pages[-2].get_text(strip=True)

    return int(last_page)

def extract_so_jobs(html):
    title = html.find("h2",class_="mb4").find("a")["title"]
    # recursive를 통해 첫번째의 span만 가져온다. 
    company, location = html.find("h3").find_all("span",recursive = False)
    company = company.get_text(strip = True)
    location = location.get_text(strip = True)
    job_id = html["data-jobid"]
    
    return {
        "title": title, 
        "company": company, 
        "location": location,
        "link": f"https://stackoverflow.com/jobs/{job_id}"
        }


def extract_so_page(last_page):
    jobs = []
    for page in range(1,last_page+1):
        req = requests.get(f"{url}&pg={page}")
        soup = BeautifulSoup(req.text,"html.parser")
            
        results = soup.find_all("div", class_ = "-job")
        
        for result in results:
            job = extract_so_jobs(result)
            jobs.append(job)

    return jobs

def get_so_jobs():
    last_page = so_lastpage()
    so_jobs = extract_so_page(last_page)
    
    return so_jobs