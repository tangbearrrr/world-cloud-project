# world-cloud-project

This project required [python3](https://www.python.org/download/releases/3.0/) to run.

## Install libraries
```sh
~ pip install tweepy
~ pip install fastapi
~ pip install "uvicorn[standard]"
```
## Setup configuration file
open config.py and enter your own twitter api keys
```
consumer_key: str = "ENTER YOUR OWN CONSUMER KEY HERE"
consumer_secret: str = "ENTER YOUR OWN SECRET KEY HERE"
access_token: str = "ENTER YOUR OWN ACCESS TOKEN HERE"
access_token_secret: str = "ENTER YOUR OWN ACCESS TOKEN SECRET HERE"
```


## Run it
```sh
~ uvicorn main:app --reload
```
## Check it

Open your browser at http://127.0.0.1:8000/api/v1/world-clouds
