from flask import Blueprint, render_template
from leetcodescraper import url, GetData, GetDataFiltered, GetUser

views = Blueprint(__name__, "views")

@views.route("/")
def home():
    data = GetData()
    return render_template("index.html", data=data)

@views.route("/problem/<problemname>")
def problem(problemname):
    data = GetDataFiltered(problemname)
    return render_template("problem.html", data=data)

@views.route("/user/<username>")
def user(username):
    fullname,avatar,link,nbr_solved,recent_ac = GetUser(url+username)
    return render_template("user.html", fullname=fullname, avatar=avatar, url=link, nbr_problem_solved=nbr_solved, recent_ac=recent_ac)