# RedditStats
### Statistics for Reddit, simplified

RedditStats is a web application designed to allow users to view analytics of any public subreddit. 
It displays the total number of upvotes, average upvotes per post, as well as the top 10 most-used words in post titles of the subreddit, alongside other data.

RedditStats is built with the Python Reddit API Wrapper (PRAW), and the Flask framework. The UI was designed with elements from Bootstrap 4.

RedditStats can pull and process up to 1000 posts from a subreddit, or 1,000 posts and comments from a user profile. This is due to limitations Reddit places on its API, which only allows a maximum of 1,000 items in a single request.
