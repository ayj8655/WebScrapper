import requests
from bs4 import BeautifulSoup

LIMIT = 50
URL = f"https://kr.indeed.com/jobs?q=python&limit={LIMIT}"

def get_last_page():
    result = requests.get(URL)
    soup = BeautifulSoup(result.text, "html.parser") #페이지가 총 몇개인지 확인하기 위해
    pagination = soup.find("div", {"class" : "pagination"}) #indeed_soup에서 find로 찾은 결과를 변수에 저장
    links = pagination.find_all('a') # pages는 리스트인데 위에서 찾은거에서 a 태그만 찾아서 저장
    
    pages = []
    for link in links[:-1]: # 페이지중 마지막 한글을 제거
        pages.append(int(link.string)) # 스트링을 인트형으로 변환
    max_page = pages[-1]  # 마지막 페이지 값
    return max_page

def extract_job(html):
    title = html.find("div", {"class" : "title"}).find("a")["title"]
    company = html.find("span", {"class" : "company"})
    company_anchor = company.find("a")
    if company_anchor is not None:
        company = str(company_anchor.string)
    else:
        company = str(company.string)
    company = company.strip()
    location = html.find("div", {"class" : "recJobLoc"})["data-rc-loc"]
    job_id = html["data-jk"]
    return {'title' : title, 'company': company, 'location' : location, 'link': f"https://kr.indeed.com/viewjob?jk={job_id}"}

def indeed_jobs(last_page):
    jobs = []
    for page in range(last_page):
        print(f"Scrapping page {page}")
        result = requests.get(f"{URL}&start = {page*LIMIT}")
        soup = BeautifulSoup(result.text, "html.parser")
        results = soup.find_all("div", {"class": "jobsearch-SerpJobCard"})
        for result in results:
            job = extract_job(result)   
            jobs.append(job)
    return jobs

def get_jobs():
    last_page = get_last_page()
    jobs = indeed_jobs(last_page)
    return jobs
