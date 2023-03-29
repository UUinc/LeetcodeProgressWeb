from flask import Blueprint, render_template
from leetcodescraper import url, GetData, GetDataFiltered, GetUser
from firebase import SetFirebaseData, GetFirebaseData
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred)
db = firestore.client()

Data = None

views = Blueprint(__name__, "views")

@views.route("/")
def home():
    global Data 
    if Data == None:
        Data = GetData()
    return render_template("index.html", data=Data)

@views.route("/problems")
def problems():
    problemsList = GetFirebaseData(db)
    return render_template("problems.html", data=problemsList)

@views.route("/problem/<problemname>")
def problem(problemname):
    global Data 
    if Data == None:
        Data = GetData()

    filtredData = GetDataFiltered(Data, problemname)
    return render_template("problem.html", data=filtredData)

@views.route("/user/<username>")
def user(username):
    fullname,avatar,link,nbr_solved,recent_ac = GetUser(url+username)
    return render_template("user.html", fullname=fullname, avatar=avatar, url=link, nbr_problem_solved=nbr_solved, recent_ac=recent_ac)

@views.route("/refresh", methods=["POST"])
def refresh():
    global Data
    Data = GetData()
    return render_template("index.html", data=Data)