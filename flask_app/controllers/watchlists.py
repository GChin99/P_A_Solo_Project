from flask_app import app
from flask import Flask, render_template, request, redirect#, session
from flask_app.models.user import User
from flask_app.models.watchlist import Watchlist




@app.route("/watchlist")
def make_a_watchlist():
    return render_template("create_watchlist.html")

@app.route("/create_watchlist", methods = ["POST"])
def create_toy():
    print(request.form)
    if not Watchlist.validate_create(request.form):
        return redirect("/watchlist")
    data = {
        "name": request.form["name"], 
        "category": request.form["category"],
        "portfolio": request.form["portfolio"],
    }
    Watchlist.create(data) 
    return redirect("/dashboard")
