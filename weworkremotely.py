import requests
from bs4 import BeautifulSoup

def get_weworkremotely_jobs(word):
  jobs = []

  url = f"https://weworkremotely.com/remote-jobs/search?term={word}"

  r = requests.get(url)
  soup = BeautifulSoup(r.text,"html.parser")

  works = soup.find_all(class_ = "jobs")
  
  for work in works:
    results = work.find("ul").find_all("li")[:-1]
    for result in results:
      a = result.find_all('a')[1]
      job = {
        "title": a.find(class_ = "title").get_text(),
        "company": a.find(class_="company").get_text(),
        "link" : a['href']
      }
      jobs.append(job)
  
  
  return jobs