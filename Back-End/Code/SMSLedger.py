from googlevoice import Voice
import sys
from bs4 import BeautifulSoup
from pymongo import MongoClient
import datetime

prevTransaction = -1;
source = "Deep Datta Roy:"
#client = MongoClient('localhost', 27017)
#db = client.test_database
#collection = db.test_collection
#collection.insert(({     'first_name': 'John',     'last_name': 'Doe',     'dob': {         'month': 5,         'day': 14,         'year': 1984     } })
#mongo_collection.find({     'last_name': 'Doe' })
voice=Voice()
voice.login("deepdattaroy8888@gmail.com","5891Deep")


#process the SMS HTML file
def extractsms(htmlsms) :
    global prevTransaction
    messagesValid = []                      #array to hold the messages

    tree = BeautifulSoup(htmlsms)           #convert to beautiful soup object
    
    messages = tree.findAll("div","gc-message-sms-row")     #find all texts and pull data
    for message in messages:
        #get time and if never run before set newest message as the prevTransaction
        #timeMessage = message.find("span","gc-message-sms-time").get_text()
        #print(messages)
        #print(asd)
        #if prevTransaction == 0:
        #    prevTransaction = timeMessage
        #    break
        #continue getting new messages till reach previous transaction
        #if timeMessage == prevTransaction:
        #    break
        fromMessage = message.find("span","gc-message-sms-from").get_text()
        if fromMessage.find(source)>=0:
            print(fromMessage.find(source))
        textMessage = message.find("span","gc-message-sms-text").get_text()
        
    #msgitems.append(msgitems)					# add msg dictionary to list
    return messagesValid
    
while True:
    voice.sms()
    extractsms(voice.sms.html)
    break
