import praw
import time
import os.path

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

words = ["SA", "DSA", "gmk", "Carbon", "Hydro", "Jukebox", "1976", "Hyperfuse", \
	 "Hana", "Pulse", "Troubled Minds", "Otaku", "Triumph Adler"]
words = [x.lower() for x in words]

while True:
    print "Scanning..."
    for submission in r.get_subreddit('mechmarket').get_new(limit=1):
        time.sleep(16)

        # modify the raw data so it is easier to search in

        title = submission.title.lower()
        text = submission.selftext.lower()
        print title
        try:
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
