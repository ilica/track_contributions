from sodapy import Socrata
import twitter
import time
import os

tweet_format_map = {
        "no_on_prop_c": "{} donated ${:,.0f} to No on C on {}. Shame on them for not supporting the homeless. Vote #YESonC. @OurHomeSF Source: https://public.netfile.com/Pub2/AllFilingsByFiler.aspx?id=172795588",
        "yes_on_prop_c":"{} donated ${:,.0f} to #YESonC on {}! Thank you for caring about your neighbors and @OurHomeSF! Source: https://public.netfile.com/Pub2/AllFilingsByFiler.aspx?id=171465346"}

def tweet_for_all_in_filing(filings, tweet_format):
    for result in filings:
        name = ""
        if (result.get("enty_namf")!=None):
            name = result.get("enty_namf")+" "+result.get("enty_naml")
        else:
            name = result.get("enty_naml")
        amount = result.get("amount")
        reportDate = result.get("rpt_date")[0:10]

        if reportDate=="2018-11-03":
            tweet = tweet_format_map.get(tweet_format).format(name,
                    float(amount), reportDate)
            status = api.PostUpdate(tweet)
            print(tweet)

client = Socrata("data.sfgov.org",
        os.environ['socrataKey'],
                  username="mahajan.ilica@gmail.com",
                  password=os.environ['socrataPass'])

no_prop_c_results = client.get("chin-jaep", filer_id=1408152)
yes_prop_c_results = client.get("chin-jaep", filer_id=1405612)

api = twitter.Api(consumer_key='Xo7wj3gQ0Um9mKwuVLgY33iYO',
                      consumer_secret=os.environ['consumer_secret'],
                      access_token_key='1053866614821515264-Tt1yDNLLJvrQO7gNEme7zxGN7d5Ffe',
                      access_token_secret=os.environ['token_secret_twitter'])

# while(True):
#    tweet_for_all_in_filing(no_prop_c_results, "no_on_prop_c")
#    tweet_for_all_in_filing(yes_prop_c_results, "yes_on_prop_c")
#    time.sleep(60000)

tweet_for_all_in_filing(no_prop_c_results, "no_on_prop_c")
tweet_for_all_in_filing(yes_prop_c_results, "yes_on_prop_c")







