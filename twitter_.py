import sqlite3
import twitter
import json
import requests

=

api = twitter.Api(consumer_key="hsyH5l8Jmqt92rdNYH48R8Q2G",
                  consumer_secret="5QTiYkp4v0AovzZvyRJ1toPyet7Z1zZyClSzjsnnLKqn3xOajm",
                  access_token_key="1123573301568319488-7m3GkF7uDlN8Oy6rDNGiZRrvuKIIoR",
                  access_token_secret="bqsfhqjydcwa6fPhoyCVWKZhLFoZVuag7WvLPOWCOxRPr")

nbTweets = 99 # C'est le maximum de tweets qu'on peut demander avec la version gratuite de l'API
tweets = api.GetSearch(raw_query="l=en&q=%23"+"bitcoin"+"&count="+str(nbTweets))

print(tweets[0].urls)
