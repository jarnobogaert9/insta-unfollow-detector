# Instagram unfollow detector

## Introduction

Ever wondered who followed you and after a while unfollowed you? This python script helps you with that and keeps track of all the accounts that unfollowed you.

## Usage

1. Install all dependencies (can be done in a virtual environment)
```
pip install -r requirements.txt
```

2. Create a .env file with listed values.
```
USER_NAME=
PASSWORD=
```
> You can copy the content of the .env.example and enter the correct username and password.

3. Execute script
```
python index.py
```
> This will create a `followers.json` file where all your current followers will be listed and a `unfollowed.json` file where all the users that unfollowed you recently will be listed.
