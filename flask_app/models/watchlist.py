from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
from flask_app.models import user

class Watchlist:

    db = "stock_api"
    def __init__(self, data):
    # the left had side are the key names we have avaiable for our html file
        self.id = data["id"]
        self.name = data["name"]
        self.category = data["category"]
        self.portfolio = data["portfolio"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]
        # ****************Parsing Data into associated Classes **********************
        self.owner = None 


    @classmethod
    def create(cls, data):
        query = "INSERT INTO watchlists (name, category, portfoilo) VALUES (%(name)s, %(category)s, %(portfoilo)s);"
        results = connectToMySQL(cls.db).query_db(query, data)
        print(results)
        return results



    @staticmethod
    def validate_create(watchlist):
        is_valid = True
        if len(watchlist["name"]) < 1:
            flash("Name needs at least 1 character!")
            is_valid = False
        if len(watchlist["category"]) < 1:
            flash("Category needs at least 1 character!")
            is_valid = False
        if len(watchlist["portfolio"]) < 1:
            flash("Portfolio needs at least 1 character!")
            is_valid = False
        return is_valid