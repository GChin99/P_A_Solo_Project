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
        self.user_id = data["user_id"]
        # ****************Parsing Data into associated Classes **********************
        self.owner = None 

# -- ------------------------- Create ---------------------------
    @classmethod
    def create(cls, data):
        query = "INSERT INTO watchlists (name, category, portfolio, user_id) VALUES (%(name)s, %(category)s, %(portfolio)s, %(user_id)s);"
        results = connectToMySQL(cls.db).query_db(query, data)
        # print(results)
        return results

# *****Associating Users in Classes*******
    @classmethod
    def get_all_watchlist_with_user(cls):
        query = "SELECT * FROM watchlists JOIN users ON watchlists.user_id = users.id;"
        results = connectToMySQL(cls.db).query_db(query)
        # print(results)
        # We have an empty list to hold all the watchlist instances that have the user instance inside of them
        all_watchlists = []
        for row in results:
            # Create a watchlist class instance from the information from each db row
            one_watchlist = cls(row)
            # Prepare to make a User class instance, we need to match up the data dictionary to the User class in models/user.py 
            user_data = {
                "id": row['users.id'], 
                "first_name": row['first_name'],
                "last_name": row['last_name'],
                "email": row['email'],
                "password": row['password'],
                "created_at": row['users.created_at'],
                "updated_at": row['users.updated_at']
            }
            user_obj = user.User(user_data)
            # Associate the Watchlist class instance with the User class instance by filling in the empty owner attribute in the Watchlist class (self.owner = None)
            one_watchlist.owner = user_obj
            # Append the Watchlist containing the associated User to your list of watchlists
            all_watchlists.append(one_watchlist)
        return all_watchlists

#---------------------Delete --------------------------------------
    @classmethod
    def delete(cls, data):
        query = "DELETE FROM watchlists WHERE id = %(id)s;"
        results = connectToMySQL(cls.db).query_db(query, data)
        # print(results)
        return results


# ---------------------Read one -----------------------
    @classmethod
    def get_one_with_user(cls, data): 
        query = "SELECT * FROM watchlists JOIN users ON watchlists.user_id = users.id WHERE watchlists.id = %(id)s"
        results = connectToMySQL(cls.db).query_db(query, data) 
        # print(results)
        watchlist = cls(results[0])
        user_data = {
            "id": results[0]['users.id'], 
            "first_name": results[0]['first_name'],
            "last_name": results[0]['last_name'],
            "email": results[0]['email'],
            "password": results[0]['password'],
            "created_at": results[0]['users.created_at'],
            "updated_at": results[0]['users.updated_at']
        }
        user_obj = user.User(user_data)
        # Associate the Recipe class instance with the User class instance by filling in the empty chef attribute in the Recipe class (self.chef = None)
        watchlist.owner = user_obj
        return watchlist


# -- -- ------------ Update  ---------------------------
    @classmethod
    def update(cls, data):
        query = "UPDATE watchlists SET name = %(name)s, category = %(category)s, portfolio = %(portfolio)s WHERE id = %(id)s;"
        results = connectToMySQL(cls.db).query_db(query, data) 
        print(results)
        return results




# --------------------validation ---------------------------------
    @staticmethod
    def validate_watchlist(watchlist):
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