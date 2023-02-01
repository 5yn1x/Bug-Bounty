#-------------simple method-------------#

import requests


TOKEN = "6012451460:AAGuTsxJoaeJ5Pqbqac3fW08siFZhN7Gy2E"
chat_id = "826415224"


message = "Hello how are you!"
# url = f"
url = f"https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={chat_id}&text={message}"


print(requests.get(url).json())