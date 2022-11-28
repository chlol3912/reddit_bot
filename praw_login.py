import praw

################################################################################
# Step 1: Logging in
################################################################################

# There are two methods for logging into reddit with PRAW.

########################################
# Method I: Include the login details directly in your python file
# NEVER do method 1

########################################
# Method II: Include the login details in a `praw.ini` file
# See: https://praw.readthedocs.io/en/latest/getting_started/configuration/prawini.html
reddit = praw.Reddit('bot', user_agent='cs40')

# NOTE:
# For this class, you must ALWAYS use Method II.
# Why?
# The python file is something that you will have to post to github/share with other people.
# But you should never share login credentials with other people for any reason.
# One of the easiest ways for companies to get "hacked" (i.e. cracked) is to leak login credentials.
# See, for example:
# 1. https://qz.com/674520/companies-are-sharing-their-secret-access-codes-on-github-and-they-may-not-even-know-it/
# 1. https://securityboulevard.com/2021/03/solarwinds-intern-leaked-passwords-on-github/
#
# NOTE:
# If you submit your login credentials with any assignment in this class,
# YOU WILL RECEIVE NEGATIVE POINTS ON THE ASSIGNMENT.
# That is because giving someone your login credentials is worse than not completing the assignment at all.
# Companies have lost **b**illions of dollars due to improper handling of login credentials.

################################################################################
# Step 2: Reading data
################################################################################

# See the PRAW QuickStart Guide for instructions on how to use the library:
# https://praw.readthedocs.io/en/stable/getting_started/quick_start.html

for submission in reddit.subreddit("test").hot(limit=10):
    print(submission.title)

# A URL to a funny reddit submission
url = "https://www.reddit.com/r/funny/comments/3g1jfi/buttons/"