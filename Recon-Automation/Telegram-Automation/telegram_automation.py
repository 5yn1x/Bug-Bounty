#-------------simple method-------------#
#create a bot with Godfather and get the API


import requests


TOKEN = "API_TOKEN"
chat_id = "CHAT_ID"


message = "Recon is completed!"
# url = f"
url = f"https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={chat_id}&text={message}"


print(requests.get(url).json())
