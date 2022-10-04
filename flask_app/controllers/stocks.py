from flask_app import app
from flask import Flask, render_template, redirect, request, session
from flask_app.models.user import User 
# We need to import the requests package that we downloaded (pipenv install requests)
import requests
# We need to import jsonify to run JavaScript.
from flask import jsonify
# We import the API keys that we put in the apis.py file over as variables 
from apis import STOCK_API_KEY

# Access stock prices using Yahoo Fanance API (pip install yfiance)
import yfinance as yf

# -----------------------Read one (step 2 of 3)-------------------------------
@app.route("/dashboard")
def dashboard():
    # ***Login validation****:  For any route inside the app, we can write an if statment (if "key" not in session:)to mkae sure the user has either logged in or registered 
    #if user tried to bypass logging in or resistration, we can redirect them to the main page
    if "user_id" not in session:
        return redirect("/") 
    # The id for the data dictionary is no longer coming from a parameter in the route, Id is now coming from session. 
    data = {
        "id": session["user_id"]
    }
    return render_template("dashboard.html", logged_in_user = User.get_by_id(data)) #passing in (data) which is our session user id to our class method


# Raid API code 
url = "https://yahoo-finance97.p.rapidapi.com/stock-info"

# payload = "symbol=AAPL" #put f string here to change the ticker symbol
payload = (f"symbol = {request.form['ticker']}")
headers = {
    "content-type": "application/x-www-form-urlencoded",
    "X-RapidAPI-Key": STOCK_API_KEY,
    "X-RapidAPI-Host": "yahoo-finance97.p.rapidapi.com"
}
# response = requests.request("POST", url, data=payload, headers=headers)
# print(response.text)

# This is coming from a form so it still needs the POST method
# We are not changing routes.  JavaScript is going to get the data and return it 
@app.route('/stock_data', methods=["POST"])
def getStockdata():
        response = requests.request("POST", url, data=payload, headers=headers)
        print(response.text)
        return jsonify( response.json() )