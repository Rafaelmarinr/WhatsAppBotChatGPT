import requests
import json

def SendMessageWhatsapp(data):
    try:
        token = "#token"
        api_url = "https://graph.facebook.com/v17.0/104167649396940/messages"
        headers = {"Content-Type": "application/json", "Authorization": "Bearer " + token}
        response = requests.post(api_url, data = json.dumps(data), headers = headers)
        if response.status_code == 200:
            return True
        
        return False
    
    except Exception as exception:
        print(exception)
        return False
