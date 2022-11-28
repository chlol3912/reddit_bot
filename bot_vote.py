import praw
from textblob import TextBlob

reddit = praw.Reddit('bot')
subreddit = reddit.subreddit('cs40_2022fall')
submissions = list(subreddit.new(limit=None))
submissions = submissions[:130]
for submission in submissions:
    try:
        print(f'Starting:\t', submission.title)
        if 'biden' in submission.title.lower():
            blob = TextBlob(submission.title)
            sum = 0
            for sentence in blob.sentences:
                sum += sentence.sentiment.polarity
            if sum > 0:
                submission.upvote()
            else:
                submission.downvote()
        elif 'biden' in submission.selftext.lower():
            blob = TextBlob(submission.selftext)
            sum = 0
            for sentence in blob.sentences:
                sum += sentence.sentiment.polarity
            if sum > 0:
                submission.upvote()
            else:
                submission.downvote()
        submission.comments.replace_more(limit=100)
        comments = submission.comments.list()
        for comment in submission.comments.list():
            blob = TextBlob(comment.body)
            sum = 0
            for sentence in blob.sentences:
                sum += sentence.sentiment.polarity
            if sum > 0:
                comment.upvote()
            else:
                comment.downvote()
    except:
        print('Didn\'t work')