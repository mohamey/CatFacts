#!/usr/bin/env python3

import schedule
import requests
import json
import time

#Specify how many times you should try to reach API
MAX_ATTEMPTS = 5

##Get a cat fact from the cat fact api
def getFact():
    dest = "http://catfacts-api.appspot.com/api/facts"
    payload = {"number" : "1"}
    ret = requests.get(dest, params=payload)
    jString = json.loads(ret.text)
    catList = jString["facts"]
    return catList[0]

#Login to three website
def login():
    login_url = "https://webtexts.three.ie/webtext/users/login"
    payload = {
        'data[User][telephoneNo]' : "PUT YOUR LOGIN NUMBER HERE",
		'data[User][pin]' : 'PUT YOUR LOGIN PASSWORD HERE'
    }

    sesh = requests.Session()
    res = sesh.post(login_url, data=payload)
    if res.url == "https://webtexts.three.ie/webtext/messages/send":
        #Login Successful
        sendMessage(sesh)
    else:
        #Login Unsuccessful, Just try again
        #Try again in ten minutes
        time.sleep(600)
        login()

#Send message on three website
def sendMessage(sesh):
    message_submission = "https://webtexts.three.ie/webtext/messages/send"
    catFact = ""
    #Attempt to get a catfact
    for i in range (1, MAX_ATTEMPTS):
        try:
            catFact = getFact()
        except:
            pass
        #If we got a catfact, exit the loop
        if not catFact == "":
            break

    #If we have a catfact, send it!
    if catFact:
        message = "CFOTD! "+catFact+". Now you know! CATch ya later! :D"
        payload = {
            'data[Message][message]' : message,
            'data[Message][recipients_individual][0]' : 'ENTER THE RECIPIENT NUMBER HERE'
        }
        res = sesh.post(message_submission, data=payload)

if __name__ == "__main__":
    #Schedule cat fact to send everyday at 8
    #Check 'schedule' api to change how often
    #cat facts are sent
    schedule.every().day.at("08:00").do(login)

    #run Forever!
    while True:
        #Ignore any exceptions (Bad practice, I know)
        try:
            schedule.run_pending()
        except Exception as e:
            pass
        #Sleep for 60 seconds, then wake and check the time again
        time.sleep(60)
