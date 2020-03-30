# traffic-incident-related-tweet-identification
This code was being used for the research paper 'Traffic-incident identifation in Tweets: difference summer and winter'. It will pre-process Tweets and with two methods identify them as 'traffic-incident related' or 'not traffic-incident related'. 

## Requirements
- To make this code work, it has to be uploaded to the Karora servers.

## Instructions
You can run the code from karora with
*./traffic-incident-identification.py*
The output will only be the counted results.

Due to copyright protecting the RUG Twitter corpus the tweets which are identified as traffic-incident related, are not available in this repository. However, there are examples to be found in *sample.txt*. If you have access to Karora and the RUG Twitter corpus it is possible to get all tweets identified by this code as traffic-incident related. Therefore, you can run *./get-traffic-incident-tweets.py*. This code will give exactly the same results as *traffic-incident-identifcation.py*, but will also create two txt-files *wintertweets.txt* and *summertweets.txt*, whereto all traffic-incident related tweets will be written to. This will make the code slightly slower to run.


