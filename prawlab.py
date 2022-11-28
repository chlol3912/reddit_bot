import praw
reddit = praw.Reddit('bot', user_agent='cs40')

poems = {}
submission = reddit.submission(url='https://www.reddit.com/r/cs40_2022fall/comments/yoc6la/rcs40_2022fall_lounge/')

submission.comments.replace_more(limit=None)
comments = submission.comments.list()

for comment in comments:
    if comment.author == 'ArmisticeBot':
        lines = comment.body.split('\n')
        title = lines[1][1:-1]
        if title in poems:
            poems[title] += 1
        else:
            poems.update({title: 1})
print(poems)

