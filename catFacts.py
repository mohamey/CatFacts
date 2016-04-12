#!/usr/bin/env python3

import schedule
import requests
import json
import time

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
        sendMessage(sesh)
    else:
        #Try again in ten minutes
        time.sleep(600)
        login()
        #print("Unable to login")

#Send message on three website
def sendMessage(sesh):
    message_submission = "https://webtexts.three.ie/webtext/messages/send"
    catFact = ""
    #Try to get a cat fact. Sometimes doesn't work because connection drops
    #Easiest to just try again
    while catFact == "":
        try:
            catFact = getFact()
        except:
            pass
    message = "CFOTD! "+catFact+". Now you know! CATch ya later! :D (local)"
    payload = {
        'data[Message][message]' : message,
        'data[Message][recipients_individual][0]' : 'ENTER THE RECIPIENT NUMBER HERE'
    }
    res = sesh.post(message_submission, data=payload)

    #print("Done")

#Schedule cat fact to send everyday at 9
#couldn't set Daylight savings time on server
#so times must be set an hour behind
schedule.every().day.at("08:00").do(login)

while True:
    try:
        schedule.run_pending()
    except Exception as e:
        pass
    time.sleep(60)
