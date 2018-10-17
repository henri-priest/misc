# IOT Twitter

Python script for searching #IOT tweets using Twitter API. The tags to query are specified in tags.py

Uses Python 3.7

## Setup

`git clone git@github.com:henri-priest/iot-twitter.git`

`cd iot-twitter`

`virtualenv env`

`.\env\Scripts\activate` (Using Windows pathing)

`pip install -r requirements.txt`

Create a file called secrets.py at root directory level and place the api secrets as shown:

**consumer_key='...'**

**consumer_secret='...'**

**access_token_key='...'**

**access_token_secret='...'**

## Run

Run setup steps first

`.\env\Scripts\activate` (Using Windows pathing)

`python main.py`

Results will be placed in .\output.csv

## Unit tests

Run setup steps first

`.\env\Scripts\activate` (Using Windows pathing)

`py.test tests.py`
