#Import dependencies
import pymongo
from pymongo import MongoClient
import pandas as pd 
from scrape_mars import scrape 
import json

#String connection
conn = "mongodb://localhost:27017"
#Creation of Mongo Client
client = pymongo.MongoClient(conn)
#Conection to the DataBase
db = client.mars_DB
#Drop the content if any
db.mars.drop() 

document = scrape()
#print(documento)

db.mars.insert_many([document])
