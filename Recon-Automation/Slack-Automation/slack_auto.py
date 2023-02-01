# First build your app in slack and create the webhook and copy the link of the webhook

import requests
import os
import json


data = {
    #Your message
    "text":"Your Recon is completed"  
}

webhook = "webhook link!"

requests.post(webhook, json.dumps(data))