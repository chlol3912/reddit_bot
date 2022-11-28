import random
import praw
import time

madlibs=[
    '[BIDEN] is a [GREAT] leader for [AMERICA]. I really [ADMIRE] his [WORK].',
    "[BIDEN]'s [WORK] for our communities has really helped [AMERICA]. He is a [GREAT] [PRESIDENT].",
    '[BIDEN]\'s [BIDEN DOG] was the first shelter [DOG] to live in [WHITEHOUSE]. [BIDEN DOG] was fostered by the [BIDENS], and has been with them since late 2018.',
    '[BIDEN]\'s [VP], [KAMALA] said she will proudly join his ticket. If that doesn\'t say a [GREAT] [PRESIDENT], I don\'t know what will.',
    'I [ADMIRE] [BIDEN]. His [WORK] has been [SUPER] important to [AMERICA] and its people',
    '[BIDEN] is the 46th and best [PRESIDENT] that [AMERICA] has seen. Together with [KAMALA], they are [UNSTOPPABLE]!'
    
]
replacements={
    'BIDEN': ['Joe Biden', 'Big B', 'Joe the man'],
    'GREAT': ['wonderful', 'great', 'amazing'],
    'AMERICA': ['the United States', 'the US', 'America'],
    'ADMIRE': ['admire', 'look up to', 'respect'],
    'WORK': ['accomplishments', 'work', 'dedication'],
    'PRESIDENT': ['President', 'leader', 'head of state'],
    'BIDEN DOG': ['Major', "German Shepherd"],
    'DOG': ['dog', 'canine', 'doggy'],
    'WHITEHOUSE': ['the White House', 'the Presidential Mansion', 'the President\'s Palace'],
    'BIDENS': ['Biden Family', 'Bidens', 'Joe\'s family'],
    'VP': ['Vice President', 'Second in-command', 'VP'],
    'KAMALA': ["Kamala Harris", 'Kamala', 'the first woman VP'],
    'SUPER': ['extremely', 'super', 'very'],
    'UNSTOPPABLE': ['unstoppable', 'strong', 'boisterous']

}
def generate_comment():
    madlib = random.choice(madlibs)
    for replacement in replacements.keys():
        madlib = madlib.replace('['+replacement+']', random.choice(replacements[replacement]))
    return madlib

reddit = praw.Reddit('bot')
sub_url='https://www.reddit.com/r/cs40_2022fall/comments/yv4s9o/practice_posting_messages_here/'
submission = reddit.submission(url=sub_url)

# for i in range(70):
#     submission.reply(body=generate_comment())
#     time.sleep(3)
submission.comments.replace_more(limit=None)
comments = submission.comments.list()
for i in range(70):
    random.choice(comments).reply(body=generate_comment())
    time.sleep(4)