# DEPENDANCIES
from flask import Flask, redirect, render_template, request
import praw

# INITIALISE FLASK APP
app = Flask(__name__)

# INITIALISE PRAW
reddit = praw.Reddit(user_agent = 'praw-tutorial',
                     client_id = '_kefauEVtw-uMg', client_secret = 'mIJj27ZGaW63V-vuny6iXlNe0O0',
                     username = 'that15fine', password = 'Dillon01')

exceptions = []

file = open('exceptions.txt', 'r')
for line in file:
    exceptions.append(line.strip())
file.close()

# HOMEPAGE
@app.route('/')
def index():
    return render_template("home.html")

# SEARCH FOR SUBREDDIT
@app.route('/subreddit', methods=["GET", "POST"])
def subreddit():
    posts = 0
    upvotes = 0
    highest_ups = 0
    top_title = ""
    top_created = ""
    top_url = ""

    word_counter = {}

    if request.method == "GET":
        return render_template("sub.html")
    else:
        userinput = request.form.get("sub")
        userinput = reddit.subreddit(userinput)

        for submission in userinput.hot(limit=None):
            try:
                posts += 1
                upvotes += submission.ups
                if submission.ups > highest_ups:
                    highest_ups = submission.ups
                    top_title = submission.title
                    top_created = submission.created
                    top_url = submission.url
                
                title = submission.title
                words = title.split(' ')
                for term in words:
                    term = term.lower()
                    if term in exceptions:
                        continue
                    elif term in word_counter:
                        x = word_counter[term]
                        word_counter[term] = x + 1
                    else:
                        word_counter[term] = 1

            except praw.exceptions.PRAWException as e:
                pass
        
        word_counter = sorted(word_counter.items(), key=lambda x: x[1], reverse=True)
        
        avg_upvotes = round(upvotes/posts, 2)

        return render_template("data.html", holder1="Posts", prefix="r/", avg_upvotes=avg_upvotes, userinput=userinput, upvotes=upvotes, posts=posts, highest_ups=highest_ups, word_counter=word_counter)

# SEARCH FOR USER
@app.route('/user', methods=["GET", "POST"])
def user():
    karma = 0
    comment_karma = 0
    link_karma = 0
    highest_ups = 0
    comments = 0
    posts = 0
    highest_ups = 0
    top_title = ""
    top_created = ""
    top_url = ""
    upvotes = 0

    word_counter = {}

    if request.method == "GET":
        return render_template("user.html")
    else:
        userinput = request.form.get("user")
        userinput = reddit.redditor(userinput)
        karma = userinput.comment_karma + userinput.link_karma
        comment_karma = userinput.comment_karma
        link_karma = userinput.link_karma
        
        for comment in userinput.comments.new(limit=1000):
            comments += 1
            comment_body = comment.body
            words = comment_body.split(' ')
            for term in words:
                term = term.lower()
                if term in exceptions:
                    continue
                elif term in word_counter:
                    x = word_counter[term]
                    word_counter[term] = x + 1
                else:
                    word_counter[term] = 1  

        for submission in userinput.submissions.hot(limit=None):
            try:
                posts += 1
                upvotes += submission.ups
                if submission.ups > highest_ups:
                    highest_ups = submission.ups
                    top_title = submission.title
                    top_created = submission.created
                    top_url = submission.url
                
                title = submission.title
                words = title.split(' ')
                for term in words:
                    term = term.lower()
                    if term in exceptions:
                        continue
                    elif term in word_counter:
                        x = word_counter[term]
                        word_counter[term] = x + 1
                    else:
                        word_counter[term] = 1

            except praw.exceptions.PRAWException as e:
                pass
            
        word_counter = sorted(word_counter.items(), key=lambda x: x[1], reverse=True)
        
        avg_upvotes = round(upvotes/(posts + comments), 2)

        return render_template("data.html", holder1="Submissions", prefix="u/", avg_upvotes=avg_upvotes, upvotes=karma, userinput=userinput, posts=posts, highest_ups=highest_ups, word_counter=word_counter)   

# RUN FLASK
if __name__ == "__main__":
    app.run()
