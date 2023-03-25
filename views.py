from flask import Blueprint, render_template
from leetcodescraper import url, GetData, GetUser

views = Blueprint(__name__, "views")

@views.route("/")
def home():
    # data = GetData()
    data = [('yahya','https://assets.leetcode.com/users/avatars/avatar_1679516073.png', 'https://leetcode.com/lazrek/','10',["<span>Palindrome</span>"])]
    return render_template("index.html", data=data)

@views.route("/user/<username>")
def user(username):
    fullname,avatar,link,nbr_solved,recent_ac = GetUser(url+username)
    return render_template("user.html", fullname=fullname, avatar=avatar, url=link, nbr_problem_solved=nbr_solved, recent_ac=recent_ac)