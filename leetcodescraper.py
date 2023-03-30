from bs4 import BeautifulSoup
import requests
from requests_futures.sessions import FuturesSession
import time
from rand_prob import problemsAPI

url = 'https://leetcode.com/'
id = [
    'lazrek',
    'NassimNamous',
    'rayan555',
    'walidhabbach',
    'yaska______',
    'user0034OK/',
    'nezhari',
    'oussama-seme-elayne',
    'badertebaa2',
    'ibarakate0',
    'larbiabbadelandaloussi'
]

#Scrapper
def GetPage(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    return soup

def GetFullName(soup):
    return soup.findAll('div', attrs={"class": "text-label-1 dark:text-dark-label-1 break-all text-base font-semibold"})[0].text

def GetAvatar(soup):
    return soup.findAll('img', attrs={"class": "h-20 w-20 rounded-lg object-cover", "alt":"Avatar"})[0]['src']

def GetSolvedSolutionNumber(soup):
    return int(soup.findAll('div', attrs={"class": "text-[24px] font-medium text-label-1 dark:text-dark-label-1"})[0].text)

def GetRecentProblem(soup):
    problemList = []
    problemsInfo = soup.findAll('a')
    for p in problemsInfo:
        if "/submissions/detail/" in p['href']:
            title = p.findAll('span', attrs={"class": "text-label-1 dark:text-dark-label-1 font-medium line-clamp-1"})[0].text
            link = "https://leetcode.com"+p['href']
            time = p.findAll('span', attrs={"class": "text-label-3 dark:text-dark-label-3 hidden whitespace-nowrap lc-md:inline"})[0].text
            
            difficulty = None
            for problem in problemsAPI:
                if title == problem["stat"]["question__title"]:
                    level = problem["difficulty"]['level']
                    if level == 1:
                        difficulty = "Easy"
                    elif level == 2:
                        difficulty = "Medium"
                    else:
                        difficulty = "Hard"
            problemList.append({"title":title, "link":link, "time":time, "difficulty":difficulty})
    return problemList

#Main Functions
def GetUserData(soup,link):
    fullname = GetFullName(soup)
    avatar = GetAvatar(soup)
    nbr_solved = GetSolvedSolutionNumber(soup)
    recent_ac = GetRecentProblem(soup)
    
    return fullname, avatar, link, nbr_solved, recent_ac

#Async Functions
def GetData():
    session = FuturesSession()
    future = []
    usersData = []
    for user in id:
        link = url+user
        future_tmp = session.get(link)
        future.append((future_tmp,link))
        time.sleep(1)
    for f,link in future:
        response = f.result()
        soup = BeautifulSoup(response.content, 'html.parser')
        usersData.append(GetUserData(soup,link))

    usersData.sort(key=lambda a: a[3], reverse=True)
    return usersData

def GetDataFiltered(data, problem_name):
    filtredData = []
    for userData in data:
        fullname = userData[0]
        avatar = userData[1]
        link = userData[2]
        nbr_solved = userData[3]
        recent_ac = userData[4]
        for problem in recent_ac:
            if problem['title'] == problem_name:
                filtredData.append((fullname,avatar,link,nbr_solved))      
                break
    return filtredData 

#Sync Function  
def GetUser(url):
    soup = GetPage(url)
    fullname = GetFullName(soup)
    avatar = GetAvatar(soup)
    nbr_solved = GetSolvedSolutionNumber(soup)
    recent_ac = GetRecentProblem(soup)
    
    return fullname, avatar, url, nbr_solved, recent_ac