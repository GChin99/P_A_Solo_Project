from flask_app import app
from flask import Flask, render_template, request, redirect, session, jsonify
from flask_app.models.user import User
from flask_app.models.watchlist import Watchlist



#----------------------------- Create --------------------------- --
@app.route("/watchlist")
def make_a_watchlist():
    if "user_id" not in session:
        return redirect("/") 
    return render_template("create_watchlist.html")

@app.route("/create_watchlist", methods = ["POST"])
def create_watchlist():
    print(request.form)
    if not Watchlist.validate_watchlist(request.form):
        return redirect("/watchlist")
    data = {
        "name": request.form["name"], 
        "category": request.form["category"],
        "portfolio": request.form["portfolio"],
        "user_id": session["user_id"]
    }
    Watchlist.create(data) 
    return redirect("/dashboard")


#---------------------Delete--------------------------------------
@app.route("/delete_watchlist/<int:id>", methods=["POST"])
def delete_watchlist(id):
    print(request.form)
    data = {
        "id": id
    }
    Watchlist.delete(data)
    return redirect("/dashboard")

# ---------------------Read one-----------------------
@app.route("/watchlist/<int:id>") 
def view_watchlist(id):
    if "user_id" not in session:
        return redirect("/") 
    data = {
        "id": id 
    }
    user_data = {
        "id" : session["user_id"]
    }
    return render_template("watchlist.html",logged_in_user = User.get_by_id(user_data),  watchlist = Watchlist.get_one_with_stocks(data))


# -- -- ------ update ---------------------------
@app.route("/edit_watchlist/<int:id>")
def edit_watchlist(id):
    if "user_id" not in session:
        return redirect("/") 
    data = {
        "id": id
    }
    return render_template("edit_watchlist.html", watchlist = Watchlist.get_one_with_user(data))

@app.route("/update_watchlist/<int:id>", methods = ["POST"])
def update_watchlist(id):
    print(request.form)
    if not Watchlist.validate_watchlist(request.form):
        return redirect(f"/edit_watchlist/{id}")
    data = {
        "id": id,
        "name": request.form['name'],
        "category": request.form["category"],
        "portfolio": request.form["portfolio"],
        # "user_id": session["user_id"]
    }
    Watchlist.update(data)
    return redirect("/dashboard")

