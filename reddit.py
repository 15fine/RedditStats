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

word_counter = {
}

exceptions = []

file = open('exceptions.txt', 'r')
for line in file:
    exceptions.append(line.strip())
file.close()

for submission in subreddit.hot(limit=1000):
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
for i in range(10):
    print(word_counter[i])