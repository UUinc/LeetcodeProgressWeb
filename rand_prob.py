import random
import json
from datetime import datetime
from firebase import SetFirebaseData, GetFirebaseData

problemsList = GetFirebaseData()
with open('leetcode_problems_api.json') as fp:
    data = json.load(fp)
problemsAPI = data["stat_status_pairs"]

def get_only_free_problems(data):
    newList = []
    for d in data:
        if d["paid_only"] == False:
            newList.append(d)
    return newList
problemsAPI = get_only_free_problems(problemsAPI)


def get_random_problem_info():
    random_problem = random.choice(problemsAPI)
    
    problem_name = random_problem["stat"]["question__title"]
    problem_slug = random_problem["stat"]["question__title_slug"]

    if random_problem["difficulty"]['level'] == 1:
        problem_difficulty = "Easy"
    elif random_problem["difficulty"]['level'] == 2:
        problem_difficulty = "Medium"
    else:
        problem_difficulty = "Hard"

    problem_url = f"https://leetcode.com/problems/{problem_slug}/"

    return (problem_name, problem_url, problem_difficulty)

def Get_Random_Problem():
    problem_name, problem_url, problem_difficulty = get_random_problem_info()
    while 1:
        if problem_name not in [ item['name'] for item in problemsList ]:
            break
        problem_name, problem_url, problem_difficulty = get_random_problem_url()

    problemData = {"name": problem_name, "link": problem_url, "date": datetime.today().strftime('%d/%m/%Y'), "difficulty": problem_difficulty}
    return problemData

# new porblem today
todayDate = datetime.today().strftime('%d/%m/%Y')

if todayDate != problemsList[0]["date"]:
    print("new problem generate...")
    newProblem = Get_Random_Problem()
    SetFirebaseData(newProblem)