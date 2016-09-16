import praw
import time

def log(submission, word):
    print "Word: \n    ", word
    print "Title: \n    ", submission.title
    print "Text: \n    ", submission.selftext
    print "Link: \n    ", submission.permalink

r = praw.Reddit(user_agent='my_cool_application')

words = ["SA", "DSA", "gmk", "Carbon", "Hydro", "CM"]
words = [x.lower() for x in words]
print words

for submission in r.get_subreddit('mechmarket').get_new(limit=1):
    time.sleep(0)

    # modify the raw data so it is easier to search in

    title = submission.title.lower()
    text = submission.selftext.lower()
    try:
        title = title.split("[h]")[1].split("[w]")[0]
    except:
        continue

    # check if words of interest are in the title after [H] but before [W]
    for i in range(0, len(words)):
        if words[i] in title:
            log(submission, words[i])

    # check if some kind of price is mentioned in the text


    # log findings to a text file