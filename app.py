# DEPENDANCIES
import flask
import praw
import pandas as pd
import datetime as dt

# INITIALISE FLASK APP
app = Flask(__name__)

# INITIALISE PRAW
reddit = praw.Reddit(user_agent = 'praw-tutorial',
                     client_id = '_kefauEVtw-uMg', client_secret = 'mIJj27ZGaW63V-vuny6iXlNe0O0',
                     username = 'that15fine', password = 'Dillon01')

# HOMEPAGE
@app.route('/')
def index():
    return render_template("home.html")

# SEARCH FOR SUBREDDIT
@app.route('/subreddit')
def subreddit():
    return render_template("sub.html")

# SEARCH FOR USER
@app.route('/user')
def user():
    return render_template("user.html")

# PROCESS INPUT AND RETURN STATISTICS - USER
@app.route('/user-search')
def user_search():
    return("home.html")

# PROCESS INPUT AND RETURN STATISTICS - USER
@app.route('/sub-search')
def user_search():
    return("home.html")

# RUN FLASK
if __name__ == "__main__":
    app.run()