from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
from flask_app.models import user
from flask_app.models import watchlist

class Stock:

    db = "stock_api"
    def __init__(self, data):
    # the left had side are the key names we have avaiable for our html file
        self.id = data["id"]
        self.name = data["name"]
        self.symbol = data["symbol"]
        self.exchange = data["exchange"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]
        self.user_id = data["user_id"]
        self.watchlist_id = data["watchlist_id"]
    
    @classmethod
    def save(cls, data):
        query = 'INSERT INTO stocks (name, symbol, exchange, user_id, watchlist_id) VALUES (%(name)s, %(symbol)s, %(exchange)s, %(user_id)s, %(watchlist_id)s;'
        return connectToMySQL(cls.db).query_db(query, data)