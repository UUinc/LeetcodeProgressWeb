from flask import Blueprint, render_template
from leetcodescraper import url, GetData, GetUser, CheckProblemSolved

views = Blueprint(__name__, "views")

@views.route("/")
def home():
    data = GetData()
    return render_template("index.html", data=data)

@views.route("/user/<username>")
def user(username):
    fullname,avatar,nbr_solved,recent_ac = GetUser(url+username)
    return render_template("user.html", fullname=fullname, avatar=avatar, nbr_problem_solved=nbr_solved, recent_ac=recent_ac)