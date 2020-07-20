import praw

# initialise with instance of reddit
reddit = praw.Reddit(user_agent = 'praw-tutorial',
                     client_id = '_kefauEVtw-uMg', client_secret = 'mIJj27ZGaW63V-vuny6iXlNe0O0',
                     username = 'that15fine', password = 'Dillon01')

# take a code from user
print("Input subreddit")
subreddit = input()
subreddit = reddit.subreddit(subreddit)

for comment in subreddit.stream.comments():
    try:
        print(30*'_')
        print()
        parent_id = str(comment.parent())
        submission = reddit.comment(parent_id)
        print('Parent:')
        print(submission.body)
        print('Reply')
        print(comment.body)
    except praw.exceptions.PRAWException as e:
        pass
