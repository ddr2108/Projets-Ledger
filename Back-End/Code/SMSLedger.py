import sys
import datetime
import time
from googlevoice import Voice
from bs4 import BeautifulSoup
from pymongo import MongoClient

###############################################################################
########################Initial Setup##########################################
source = "Deep Datta Roy:"      #holds the number which is the source
number = "4045148059"           #the actual number
email = "deepdattaroy8888@gmail.com"    #login info
pwd = "5891Deep"
###############################################################################
###############################################################################

#Global Variables
prevTransaction = -1           #holds the number of messages earlier
voice = -1                     #holds the Google Voice Interface

#main function
def main():
    global voice

    #Google Voice Interface
    voice = Voice()
    voice.login(email,pwd)              #Login
    while True:
        voice.sms()                     #Get SMS Data  
        messages = extractSMS(voice.sms.html)      #Get messages
        processMessages(messages)                   #Process Recieved Messages
        time.sleep(30)

#processes the recieved messages
def processMessages(messages):
    #Break each message into words
    for message in messages:
        messagePieces = message.split()
        #if 3 words, do more processing
        if (len(messagePieces)==4 and messagePieces[0].lower() =="ledger"):
            insertDB(messagePieces)
            sendSMS("Transaction Added")
        elif (len(messagePieces)==2 and messagePieces[0].lower() =="ledger"):
            #data = requestDB(messagePieces)
            sendSMS("asd")

#insert new info into ledger
def insertDB(messagePieces):
    #client = MongoClient('localhost', 27017)
    #db = client.test_database
    #collection = db.test_collection
    #collection.insert(({     'first_name': 'John',     'last_name': 'Doe',     'dob': {         'month': 5,         'day': 14,         'year': 1984     } })
    #mongo_collection.find({     'last_name': 'Doe' })
    a = 1

#get data from ledger to send as SMS
def requestDB(messagePieces):
    a = 1

#send requested data via SMS
def sendSMS(data):
    voice.send_sms(number, data)

#process the SMS HTML file
def extractSMS(HTMLSMS):
    global prevTransaction
    messagesValid = []                      #array to hold the messages
    messagesNew = []

    tree = BeautifulSoup(HTMLSMS)           #convert to beautiful soup object
    
    messages = tree.findAll("div","gc-message-sms-row")     #find all texts and pull data
    for message in messages:
        #Seperate messages from correct user
        fromMessage = message.find("span","gc-message-sms-from").get_text()
        if fromMessage.find(source)>=0:
            messagesValid.append(message)

    #if this is first go through, set value
    if prevTransaction == -1:
        prevTransaction = len(messagesValid)
        return messagesNew;
    
    #new text has arrived
    if prevTransaction != len(messagesValid):
        #get the new messages
        for x in range(prevTransaction, len(messagesValid)):
            textMessage = messagesValid[x].find("span","gc-message-sms-text").get_text()
            messagesNew.append(textMessage);
        prevTransaction = len(messagesValid)        #set new value for messages

    return messagesNew

if __name__=="__main__":
    main()