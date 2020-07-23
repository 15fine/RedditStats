import praw
import pandas as pd
import datetime as dt

# initialise with instance of reddit
reddit = praw.Reddit(user_agent = 'praw-tutorial',
                     client_id = '_kefauEVtw-uMg', client_secret = 'mIJj27ZGaW63V-vuny6iXlNe0O0',
                     username = 'that15fine', password = 'Dillon01')


# take a code from user
print("Input subreddit")
subreddit = input()
subreddit = reddit.subreddit(subreddit)

posts = 0
upvotes = 0
highest_ups = 0
top_title = ""
top_created = ""
top_url = ""

topics_dict = { "title":[],
                "score":[]
                }

for submission in subreddit.hot(limit=1000):
    try:
        posts += 1
        upvotes += submission.ups
        if submission.ups > highest_ups:
            highest_ups = submission.ups
            top_title = submission.title
            top_created = submission.created
            top_url = submission.url
        
        topics_dict["title"].append(submission.title)
        topics_dict["score"].append(submission.score)

    except praw.exceptions.PRAWException as e:
        pass

topics_data = pd.DataFrame(topics_dict)
topics_data.to_csv('data.csv', index=False) 