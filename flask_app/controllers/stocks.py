from flask_app import app
from flask import Flask, render_template, redirect, request, session
from flask_app.models.user import User 
from flask_app.models.stock import Stock 
from flask_app.models.watchlist import Watchlist
# We need to import the requests package that we downloaded (pipenv install requests)
import requests
import time
# We need to import jsonify to run JavaScript.
from flask import jsonify
# We import the API keys that we put in the apis.py file over as variables 
from apis import STOCK_API_KEY, Twelvedata_API_KEY

# Access stock prices using Yahoo Fanance API (pip install yfiance)
# import yfinance as yf

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
    return render_template("dashboard.html", logged_in_user = User.get_by_id(data), all_watchlist = Watchlist.get_all_watchlist_with_user()) #passing in (data) which is our session user id to our class method


# Twelvedata.com API
@app.route('/stock_data', methods=["POST"])
def get_stock_price():
    url = f"https://api.twelvedata.com/quote?symbol={request.form['ticker']}&apikey={Twelvedata_API_KEY}"
    response = requests.get(url)
    print(response)
    return jsonify (response.json())

# URL for:
# company profile: https://api.twelvedata.com/profile?symbol=AAPL&apikey=demo
# compnay dividens:https://api.twelvedata.com/dividends?symbol=AAPL&apikey=demo
# SMA:https://api.twelvedata.com/sma?symbol=AAPL&interval=1min&apikey=demo
# RSI:https://api.twelvedata.com/rsi?symbol=AAPL&interval=1min&apikey=demo
# MACD:https://api.twelvedata.com/macd?symbol=AAPL&interval=1min&apikey=demo


@app.route('/stock/save/', methods=['post'])
def createStock():
    data = {
        'name': request.form['name'],
        'symbol': request.form['symbol'],
        'exchange': request.form['exchange'],
        'user_id': session['user_id'],
        'watchlist_id':int(request.form['watchlist_id'])
    }
    Stock.save(data)
    return redirect('/dashboard')



#---------------------Delete show (step 2 of 3))--------------------------------------
@app.route("/stock/<int:id>/delete", methods=["POST"])
def delete_stock(id):
    print(request.form)
    # logged in Validation
    if "user_id" not in session:
        return redirect("/") 
    data = {
        "id": id
    }
    Stock.delete_stock(data)
    return redirect(f"/watchlist/{id}")






# Raid API code 
# url = "https://yahoo-finance97.p.rapidapi.com/stock-info"

# # payload = "symbol=AAPL" #put f string here to change the ticker symbol
# payload = (f"symbol = {request.form['ticker']}")
# headers = {
#     "content-type": "application/x-www-form-urlencoded",
#     "X-RapidAPI-Key": STOCK_API_KEY,
#     "X-RapidAPI-Host": "yahoo-finance97.p.rapidapi.com"
# }
# # response = requests.request("POST", url, data=payload, headers=headers)
# # print(response.text)

# # This is coming from a form so it still needs the POST method
# # We are not changing routes.  JavaScript is going to get the data and return it 
# @app.route('/stock_data', methods=["POST"])
# def getStockdata():
#         response = requests.request("POST", url, data=payload, headers=headers)
#         print(response.text)
#         return jsonify( response.json() )


