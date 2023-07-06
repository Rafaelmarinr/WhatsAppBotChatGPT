from flask import Flask, request
import util
import whatsappservice
import chatgptservice

app = Flask(__name__)
@app.route('/welcome', methods=['GET'])
def index():
    return "welcome developer"

@app.route('/whatsapp', methods=['GET'])
def VerifyToken():
    try:
        accessToken = "7SDASDSSDSD485S4DSESDS44"
        token = request.args.get("hub.verify_token")
        challenge = request.args.get("hub.challenge")

        if token != None and challenge != None and token == accessToken:
            return challenge
        else:
            return "", 400
    except:
        return "",400

    
@app.route('/whatsapp', methods=['POST'])
def ReceivedMessage():
    try:
        body = request.get_json()
        entry = (body["entry"])[0]
        changes = (entry["changes"])[0]
        value = changes["value"]
        message = (value["messages"])[0]
        number = message["from"]

        text = util.GetTextUser(message)

        responseGPT = chatgptservice.GetResponse(text)
        if responseGPT != "error":
            data = util.TextMessage(responseGPT, number)
        else:
            data = util.TextMessage("Lo siento ocurrio un problema", number)
        
        whatsappservice.SendMessageWhatsapp(data)
        # print(text)
        return "EVENT_RECEIVED"
    except:
        return "EVENT_RECEIVED"

def ProcessMessages(text,number):
    text = text.lower()
    listMenu = []

    if "hi" in text or "hello" in text:
        data = util.TextMessage("Hello, how can i help you?", number)
        dataMenu = util.ListMessage(number)

        listMenu.append(data)
        listMenu.append(dataMenu)

    elif "thank" in text:
        data = util.TextMessage("thank you for contacting me", number)

    elif "agency" in text:
        data = util.TextMessage("This is our agency", number)
        dataLocation = util.LocationMessage(number)

        listMenu.append(data)
        listMenu.append(dataLocation)
    elif "contact" in text:
        data = util.TextMessage("**Contact center**\n+584129971185", number)
        listMenu.append(data)
    
    elif "buy" in text:
        data = util.ButtonsMessage(number)
        listMenu.append(data)

    elif "sell" in text:
        data = util.ButtonsMessage(number)
        listMenu.append(data)

    elif "sign up" in text:
        data = util.TextMessage("Enter this link to register your account: https://www.rafaelmarin.site/register", number)
        listMenu.append(data)
    
    elif "login" in text or "log in" in text:
        data = util.TextMessage("Enter this link to login your account: https://www.rafaelmarin.site/login", number)
        listMenu.append(data)

    else:
        data = util.TextMessage("I'm sorry, I can't understand you. \n You have others options", number)
        dataMenu = util.ListMessage(number)
        listMenu.append(data)
        listMenu.append(dataMenu)

    for item in listMenu:
        whatsappservice.SendMessageWhatsapp(item)

def GenerateMessage(text, number):

    text = text.lower()
    if "text" in text:
        data = util.TextMessage("Text", number)

    if "format" in text:
        data = util.TextFormatMessage(number)

    if "image" in text:
        data  = util.ImageMessage(number)
    
    if "audio" in text:
        data = util.AudioMessage(number)

    if "video" in text:
        data = util.VideoMessage(number)
    
    if "document" in text:
        data = util.DocumentMessage(number)

    if "location" in text:
        data = util.LocationMessage(number)

    if "button" in text:
        data = util.ButtonsMessage(number)

    if "list" in text:
        data = util.ListMessage(number)
    
    whatsappservice.SendMessageWhatsapp(data)

if(__name__ == "__main__"):
    app.run()