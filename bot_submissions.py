import praw
import random
import time

reddit = praw.Reddit('bot')
submissions = list(reddit.subreddit("liberal").hot(limit=300))
subreddit = reddit.subreddit('cs40_2022fall')
for i in range(200):
    submission = random.choice(submissions)
    title = submission.title
    selftext = submission.selftext
    print('Creating post for:    ', title)
    if selftext == '':
        url = submission.url
        subreddit.submit(title, url=url)
    else:
        subreddit.submit(title, selftext=selftext)
    
    time.sleep(15)