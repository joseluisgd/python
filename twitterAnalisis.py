#Lo que se hara es partir una horacion en palabras pequenas.
#Este proceso se llama Tokenization.
#Se tiene que instalar tweepy ---> sudo -H pip install tweepy para acceder a la API
#Instalar textblob ---> para realizar un analisis de sentimientos de los tweets
import tweepy
from textblob import TextBlob

#Almacenamos las llaves de twitter que se obtienen de apps.twitter.com
consumer_key = ""
consumer_secret = ""
access_token = ""
access_token_secret = ""

#Nos autentificamos con nuestras llaves (pub,priv)
auth = tweepy.OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token,access_token_secret)

#Nos autentificamos en la API
api = tweepy.API(auth)

#Buscamos variables con una frase en especial
tweetsPub = api.search("bad")

for tweet in tweetsPub:
    print(tweet.text)
    analisis = TextBlob(tweet.text)
    print(analisis.sentiment)
