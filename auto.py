import requests
import time
payload = {
            'content': "b!work"
        }
payload2 = {
            'content': "b!dep all"
        }
header = {
            'authorization': 'NTgxMzQ4NTM1NjE0NzAxNTcy.YOBZ7Q.4wNB-XOiJ8JxlWFo-LCNUkpVx40'
        }

timeout = time.time() + 3
while True:
    if time.time() > timeout:
        r = requests.post("https://discord.com/api/v9/channels/874628006080049222/messages", data=payload,
                          headers=header)
        r = requests.post("https://discord.com/api/v9/channels/874628006080049222/messages", data=payload2,
                          headers=header)
    time.sleep(5)
