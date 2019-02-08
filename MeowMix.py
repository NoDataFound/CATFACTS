#!/usr/bin/env python
# -*- coding: utf-8 -*- 
from twilio.rest import Client
import requests
import json
catfact = requests.get('https://catfact.ninja/fact')
account_sid = 'OUR_TWILLO_SID'
auth_token = 'YOUR_TWILLO_TOKEN'
client = Client(account_sid, auth_token)
numbers_to_message = ['+TARGET_NUMBER_SEPERATE_WITH_COMMAS']
for number in numbers_to_message:
    client.messages.create(
 	 body='/ᐠ｡‸｡ᐟ\ - Did you know?!' + (json.dumps(catfact.json(), sort_keys=True, indent=4))+'😹',
         from_='+TWILLO_NUMBER',
         to=number
     )
