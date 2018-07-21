import sys
import tweepy
import requests
import codecs
from pymongo import MongoClient
# Conexion a MongoDB
cliente = MongoClient()
cliente = MongoClient('127.0.0.1', 27017)
bd = cliente.twitter
tweets = bd.tweets
# Llaves del API de Twitter
consumer_key = '5OyelwrI4vJ5swWijMSE44wmJ'
consumer_secret = 'JS1oIcUdDnOoaVL2gjzgjKhFwrhIBkY5FNIbyP7cu8RAmAt016'
access_token = '4740190268-DSjDVKwg1R1yWyrFOMYLpugjnK56NibFrtC2nUi'
accesss_secret = 'xhg3R6EWHPXQCy51qicHPzSKkLhOyxzd3NuqVLfM0gN5B'
class MyStreamListener(tweepy.StreamListener):
    def on_status(self, status): # Procesar nuevos tweets
        if not hasattr(status, 'retweeted_status'): # Ignorar retweets
            # Codificar en UTF-8 el mensahe antes de imprimirlo
            print status.text.encode('utf-8')+"<>"+status.text.encode('utf-8')
            # Crear objeto
            tweet = {
                "idt": str(status.id),
                "tweet": status.text.encode('utf-8'),
                "fecha_creacion": status.created_at,
                "sentimiento": "";}
            tweets.insert_one(tweet) #Alamacenar el tweet
    def on_error(self, status_code):
        if status_code == 420:
            print "Numero de intentos excesivos de conectarse al"
            print "streaming API, esperar y ejecutar de nuevo..."
        elif status_code == 401:
            print "Credenciales de API incorrectas."
        else:
            print "Ocurrio un error"
    def on_timeout(self):
        print "Timeout..."
        return True # Seguir la ejecucion
                    # False cancelaria la ejecucion del programa
tauth = tweepy.OAuthHandler(consumer_key, consumer_secret)
tauth.set_access_token(access_token, accesss_secret)
streamListen = MyStreamListener() # Instanciar clase
twStream = tweepy.Stream(auth = tauth, listener = streamListen)
# Especificar filtro & Iniciar stream
twStream.filter(track = ['#CDMX, #EPN, #Mexico, #UDLAP'], async = False)
