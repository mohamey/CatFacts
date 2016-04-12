# CatFacts
Send daily cat facts to any number!
<hr>
To get started just download catFacts.py, add your Three Ireland Login and Password, and specify your target recipient. This script is designed to automatically send facts daily, so configure the time of day you'd like to send the facts at and the rest is handled by the script. 

This script needs to be kept on a running machine, so I personally recommend using a server - any will do. 

If you're a part of the Ubuntu Server Master Race, change the permissions of catFacts.py to make it executable, then call "nohup python3 catFacts.py &". The process will have to be manually terminated if you want to stop it. But nobody wants that, right?

Finally, this script was written using Python3, and requires that you install requests and schedule before you can use it. pip3 is the easiest way to install these. 
