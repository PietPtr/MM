import praw
import time
import os.path
import sys

def log(submission, word, prices):
    file = open(file_name, 'w')
    try:
        file.write("Word found: " + word)
        file.write("\nFull Title: " + submission.title)
        file.write("\nURL to post: " + submission.url)
        file.write("\nPrices found:" + str(prices))
        file.write("\n\nRest of the text:\n\n" + submission.selftext)
    except UnicodeEncodeError:
        file.write("Something went wrong writing the file, here is the link:")
        file.write(submission.url)

    file.close()


r = praw.Reddit(user_agent='Mech market logger for market research in mechanical keyboards')

words = ["Carbon", "Hydro", "Jukebox", "1976", "Hyperfuse", "Ice Cap"\
	 "Hana", "Pulse", "Troubled Minds", "Otaku", "Triumph Adler", "Deep Space"]
words = [x.lower() for x in words]

while True:
    print "Scanning..."

    submission = 0
    try:
        for s in r.get_subreddit('mechmarket').get_new(limit=1):
            submission = s
    except:
        continue


    # modify the raw data so it is easier to search in

    title = submission.title.lower()

    text = submission.selftext.lower()
    print title
    try:
        want = title.split("[w]")[1]
        if not ("paypal" in want or "wallet" in want :
            print "Not for sale"
            continue
        print "For sale!"
        title = title.split("[h]")[1].split("[w]")[0]
        title = title.replace(",","").replace(".","")
        print title
    except:
        continue



    # check if some kind of price is mentioned in the text
    price_found = False
    prices = []
    if "$" in text:
        splittext = text.split("$")
        prices.append(splittext[1].split(" ")[0])
        price = splittext[0].split(" ")
        prices.append(price[len(price) - 1])


    file_name = "./log/" + submission.url.split("/")[6]

    # check if words of interest are in the title after [H] but before [W]
    for i in range(0, len(words)):
        word = " " + words[i] + " "
        if word in title and not os.path.isfile(file_name):
            log(submission, words[i], prices)


    time.sleep(16)
