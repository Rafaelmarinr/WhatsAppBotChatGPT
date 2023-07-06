import requests
import json

def SendMessageWhatsapp(data):
    try:
        token = "EAAD3yUmcRcoBABvyztBZAiPwFGqj7Sm5Tag2e7s2fzYQbxybI4Q6PZBWn7bZCzqr3Y946hacoZBLfZC9JjXnfWJudT18Y61NAveGKlKLstJ97K3tWwci4P5ZAZASR9XcXJzVUNyFZBW8eDBmk8MatUusIImXZB4yu98HZA7hJsBpLgyxydCaujAmg1"
        api_url = "https://graph.facebook.com/v17.0/104167649396940/messages"
        headers = {"Content-Type": "application/json", "Authorization": "Bearer " + token}
        response = requests.post(api_url, data = json.dumps(data), headers = headers)
        if response.status_code == 200:
            return True
        
        return False
    
    except Exception as exception:
        print(exception)
        return False