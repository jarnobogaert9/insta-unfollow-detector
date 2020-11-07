#!/usr/bin/env python3
from instagram_private_api import Client, ClientCompatPatch
from datetime import datetime
import uuid
import json
from InstaBot import InstaBot
# from mongo import MongoClient

instaBot = InstaBot()
# db = MongoClient()

prev_followers = instaBot.read_followers()
now_followers = instaBot.get_followers()
# We use this later on
now_followers_to_write = now_followers

# This step is when their are no followers in the file
if len(prev_followers) == 0:
    print('no followers in file')
    prev_followers = now_followers
    instaBot.write_followers(now_followers)


unfollowed = []
prev_followers = [user.get('username') for user in prev_followers]
now_followers = [user.get('username') for user in now_followers]

for user in prev_followers:
    if user not in now_followers:
        unfollowed.append(user)

print(unfollowed)

instaBot.write_unfollowed(unfollowed)

instaBot.write_followers(now_followers_to_write)

# Write amount of followers to db
# amount_of_followers = len(now_followers)

# now = datetime.now()
# # dd/mm/YY H:M:S
# dt_string = now.strftime("%d/%m/%Y %H:%M:%S")

# obj = {
#     'amountOfFollowers': amount_of_followers,
#     'createdAt': dt_string
# }

db.insert_one(data=obj, coll='amounts')