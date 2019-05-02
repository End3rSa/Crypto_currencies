#partie twitter

#In order to authorise our app to access Twitter on our behalf, 
#we need to use the OAuth interface:

import sqlite3
import pyhton-twitter
import OAuthHandler from pyhton-twitter 
import json
import twitter
import requests
# je sais pas si import 1 fois suffit pour tout le code ou pas

def keys_twitter ():
    api = twitter.api(api_key = "hsyH5l8Jmqt92rdNYH48R8Q2G"
                    api_secret_key = "5QTiYkp4v0AovzZvyRJ1toPyet7Z1zZyClSzjsnnLKqn3xOajm"
                    access_token = "1123573301568319488-7m3GkF7uDlN8Oy6rDNGiZRrvuKIIoR"
                    access_secret_token = "bqsfhqjydcwa6fPhoyCVWKZhLFoZVuag7WvLPOWCOxRPr")

auth = OAuthHandler(api_key, api_secret_key)
auth.set_access_token(access_token, access_secret_token)

api = pyhton-twitter.API(auth)

#to gather all the upcoming tweets (temps continu)
from pyhton-twitter import Stream
from pyhton-twitter.streaming import StreamListener
#je sais pas si ca nous sera necessaire

# pour obtenir les resultats 
# methode 1 
results = api.GetSearch(
    raw_query="q???"
#mais pour ca on a besoin d'abord des 10 crypto avec leur rang et (d'un lien exact du python-twitter donc aussi)

#methode 2
request_string = "lien twitter"
reponse = requests.get(request_string)

#remplir la table tweets
input_tweets [(tweets["URL"], tweets["date"], tweets["content"], tweets["nb_likes"], tweets["nb_retweets"], tweets["content"], tweets["extract_id"], tweets["ticker_id"], tweets["indicator1"], tweets["indicator2"], tweets["indicator3"], tweets["indicator4"]) for ???tweets??? in tweets if int(tweet[rank]) <= "11"]





