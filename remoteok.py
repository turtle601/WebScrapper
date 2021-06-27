import requests

headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'}

def get_remoteok_jobs(word):
  jobs = []
  url = f'https://remoteok.io/api?tags={word}'
  r = requests.get(url,headers = headers)
  json = r.json()

  for i in range(1,len(json)):
    job = {
      "title": json[i]["position"],
      "company": json[i]["company"],
      "link": json[i]["url"]
    }
    jobs.append(job)
      
  return jobs 