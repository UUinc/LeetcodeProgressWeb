from bs4 import BeautifulSoup
import requests

url = 'https://leetcode.com/';
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
    'ibarakate0'
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

def GetRecentAC(soup):
    return soup.findAll('span', attrs={"class": "text-label-1 dark:text-dark-label-1 font-medium line-clamp-1"})

#Main Functions
def GetData():
    usersData = []
    for user in id:
        usersData.append(GetUser(url+user))
    return usersData

def GetDataFiltered(problem_name):
    usersData = []
    for user in id:
        soup = GetPage(url+user)
        fullname = GetFullName(soup)
        avatar = GetAvatar(soup)
        nbr_solved = GetSolvedSolutionNumber(soup)
        recent_ac = GetRecentAC(soup)
        for title in recent_ac:
            if title.text == problem_name:
                usersData.append((fullname,avatar,url+user,nbr_solved))      
                break
    return usersData
    
def GetUser(url):
    soup = GetPage(url)
    fullname = GetFullName(soup)
    avatar = GetAvatar(soup)
    nbr_solved = GetSolvedSolutionNumber(soup)
    recent_ac = GetRecentAC(soup)
    
    return fullname, avatar, url, nbr_solved, recent_ac