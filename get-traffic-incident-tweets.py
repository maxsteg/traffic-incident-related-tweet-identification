"""To make this code work, it must be running from Karora. This code
   is used to export all traffic-incident related tweets to
   wintertweets.txt and summertweets.txt. If you don't want to export
   the tweets, but only reproduce the numbers mentioned in the paper,
   it is faster to use traffic_incident_identification.py"""

import gzip
import os
import re


def preprocessing(line):
    """deletes author of tweet, replaces URL's to -URL,
       replaces user mentions with @USER"""
    # Deletes author of tweet
    line = line.split('\t', 1)[1].rstrip()

    # URL replacement
    line = re.sub(r"https?://[^ ]+ *", "-URL- ", line)
    line = re.sub(r"www\.[^ ]+ *", r"URL", line)

    # Username mentions replacement
    line = re.sub(r"@[^ ]+", r" @USER", line)
    return line
    

def main():
    # root directory on karora containing the text of all tweets 2010 - until now
    rootdir = '/net/corpora/twitter2/Tweets/Tekst/'

    # Selection of months: first three winter, last three summer.
    months = ['2017/12', '2018/01', '2018/02', '2018/07', '2018/08', '2018/09']

    # Set with keywords used for method 1.
    keywords = {'verkeersongeval', 'verkeersongeluk', 'verkeersdode', 'verkeersdoden',
                'autobotsing', 'auto-ongeluk', 'fiets-ongeluk', 'fietsongeluk', 'scooterongeluk'}

    # Two tuples used for method 2.
    vehicles = ("auto", "fiets", "scooter", "brommer", "scootmobiel", "rollator", "trekker",
                "tractor", "camper", "caravan", "voetganger", "wandelaar", "motor", "bus",
                "taxi", "trein", "tram",)
    events = ("bots", "ramd", "ramt", "tegenaangereden", "aangereden", "geknald", "knalt",
              "ongeluk", "ongeval", "overreden")

    # Initialising total_tweets. First number is winter, second is summer.
    total_tweets = [0, 0]

    # Initializing previous_line, winter_traffic_tweets, summer_traffic_tweets, total_tweets_inclusive_retweets
    winter_traffic_tweets = 0
    summer_traffic_tweets = 0
    tot_tweets_inc_rt = 0
    previous_line = ''

    # Opening/creating wintertweets.txt/summertweets.txt where all traffic-incident related tweets will be written to.
    wintertweets = open('wintertweets.txt', 'w', encoding='utf8')
    summertweets = open('summertweets.txt', 'w', encoding='utf8')
    for month in range(len(months)):
        directory = rootdir + months[month]
        for subdir, dirs, files in os.walk(directory):
            # Print current month on which the code is running.
            print(subdir)
            for file in files:
                # Opening of .out.gz file
                if 'out.gz' in file:
                    filepath = subdir + os.sep + file
                    with gzip.open(filepath, 'rt', encoding='utf8') as inp:
                        for line in inp:
                            tot_tweets_inc_rt += 1
                            line = preprocessing(line)
                            # Leave out retweets and duplicates
                            if line.startswith('RT ') == False and previous_line != line:
                                previous_line = line
                                #Check if tweets is from winter or summer
                                if month in [0, 1, 2]:
                                    total_tweets[0] += 1
                                else:
                                    total_tweets[1] += 1

                                # Method 1: Check if word in keywords is in line
                                # Method 2: Check if a word from vehicles and a word from events is in line
                                if (any(word in line.lower() for word in keywords)) or (any(item in line.lower() for item in vehicles) and any(item in line.lower() for item in events)):
                                    # Check if tweet is from winter or summer
                                    if month in [0, 1, 2]:
                                        winter_traffic_tweets  += 1
                                        wintertweets.write(line+'\n')
                                    else:
                                        summer_traffic_tweets += 1
                                        summertweets.write(line+'\n')

    wintertweets.close()
    summertweets.close()

    # Result printing
    print("Total number of tweets including retweets and duplicates: {0}".format(tot_tweets_inc_rt))
    print("Total number of tweets excluding retweets and duplicates is {0}, from which {1} tweets in winter and {2} in summer.\n\n"
           .format(total_tweets[0]+total_tweets[1], total_tweets[0], total_tweets[1]))
    print("Number of tweets winter traffic-incident related: {}".format(winter_traffic_tweets))
    print("Number of tweets summer traffic-incident related: {}.\n".format(summer_traffic_tweets))
    print("Total tweets traffic-incident related: {}.".format(winter_traffic_tweets+summer_traffic_tweets))


if __name__ == "__main__":
    main()
