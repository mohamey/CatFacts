# CatFacts
This script was born out of my friends love of cats and my innate need to annoy people. It's a fairly straightforward script you can host on a server or your own computer, what it does out of the box is it retrieves a random catfact from an API, then using Three Irelands webtext service it sends the webtext to some recipient specified by their phone number.

## Requirements
* Python3
* Pip3

## Usage
To use this script, clone the repo and run:
```
pip3 install -r requirements.txt
```

Then open up the script script `catFacts.py` and add your Three Ireland Login and Password where appropriate, then add the target recipients number where required. The script is already configured to automatically send a text everyday at 8am, but feel free to change this.

Then simply run
```
python3 catFacts.py
```
and it should send a catfact at the specified time. If you want it to run with no output then just call:
```
python3 catFacts.py > /dev/null 2>&1 &
```
This would discard the output and run the script in the background.
