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
    login_url = "https://webtexts.three.ie/users/login"
    payload = {
        'msisdn' : "0876477540",
	    'pin' : '940367'
    }

    sesh = requests.Session()
    res = sesh.post(login_url, data=payload)
    if res.url == "https://webtexts.three.ie/messages/send":
        #Login Successful
        sendMessage(sesh)
    else:
        #Login Unsuccessful, Just try again
        #Try again in ten minutes
        time.sleep(600)
        login()

#Send message on three website
def sendMessage(sesh):
    message_submission = "https://webtexts.three.ie/messages/send"
    catFact = ""
    #Attempt to get a catfact
    loop = 0
    while loop < 320:
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
            #message = "CFOTD! "+catFact+". Now you know! CATch ya later! :D"
            print(catFact)
            payload = {
                'message' : catFact,
                'recipients_contacts[]' : '0857248233'
            }
            res = sesh.post(message_submission, data=payload)
            loop = loop + 1
            time.sleep(1)

if __name__ == "__main__":
    #Schedule cat fact to send everyday at 8
    #Check 'schedule' api to change how often
    #cat facts are sent
    #schedule.every().day.at("08:00").do(login)
    login()

    #run Forever!
    '''while True:
        #Ignore any exceptions (Bad practice, I know)
        try:
            schedule.run_pending()
        except Exception as e:
            pass
        #Sleep for 60 seconds, then wake and check the time again
        time.sleep(60)
'''
