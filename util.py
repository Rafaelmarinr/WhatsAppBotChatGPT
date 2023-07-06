def GetTextUser(message):
    text = ""
    typeMessage = message["type"]

    if typeMessage == "text":
        text = (message["text"])["body"]
    elif typeMessage == "interactive":
        interactiveObject = message["interactive"]
        typeInteractive = interactiveObject["type"]

        if typeInteractive == "button_reply":
            text = (interactiveObject["button_reply"])["title"]
        elif typeInteractive == "list_reply":
            text = (interactiveObject["list_reply"])["title"]
        else:
            print('sin mensaje')
    else:
        print("sin mensaje")
    
    return text

def TextMessage(text, number):
    data ={
            "messaging_product": "whatsapp",
            "to": number,
            "text": {
                "body": text
            },
            "type": "text",
            }
    return data

def TextFormatMessage(number):
    data =  {
                "messaging_product": "whatsapp",    
                "recipient_type": "individual",
                "to": number,
                "type": "text",
                "text": {
                    "body": " formato *Negritas*  _Cursiva_ ~Tachado~ ```Small Text```"
                }
            }
    return data

def ImageMessage(number):
    data =  {
                "messaging_product": "whatsapp",
                "to": number,
                "type": "image",
                "image": {
                    "link":"https://imgmedia.larepublica.pe/640x377/larepublica/migration/images/3LJFPTTDVFGFZPKDPLW44QLCZM.webp"
                }
            }
    return data


def AudioMessage(number):
    data =  {
                "messaging_product": "whatsapp",    
                "recipient_type": "individual",
                "to": number,
                "type": "audio",
                "audio": {
                    "link":"https://biostoragecloud.blob.core.windows.net/resource-udemy-whatsapp-node/audio_whatsapp.mp3"
                }
            }

    return data

def VideoMessage(number):
    data =  {
                "messaging_product": "whatsapp",    
                "recipient_type": "individual",
                "to": number,
                "type": "video",
                "video": {
                    "link":"https://biostoragecloud.blob.core.windows.net/resource-udemy-whatsapp-node/video_whatsapp.mp4"
                }
            }

    return data

def DocumentMessage(number):
    data =  {
                "messaging_product": "whatsapp",    
                "recipient_type": "individual",
                "to": number,
                "type": "document",
                "document": {
                    "link":"https://biostoragecloud.blob.core.windows.net/resource-udemy-whatsapp-node/document_whatsapp.pdf"
                }
            }

    return data

def LocationMessage(number):
    data =  {
                "messaging_product": "whatsapp",
                "recipient_type": "individual",
                "to": number,
                "type": "location",
                "location": {
                    "latitude": "10.122662401319118",
                    "longitude": "-66.77415676952585",
                    "name": "Mi casa",
                    "address": "Ocumare del Tuy, Miranda"
                }
            }

    return data

def ButtonsMessage(number):
    data =  {
                "messaging_product": "whatsapp",
                "recipient_type": "individual",
                "to": number,
                "type": "interactive",
                "interactive": {
                    "type": "button",
                    "header":{
                        "type":"text",
                        "text": "Welcome"
                    },
                    "type": "button",
                    "body": {
                        "text": "Do you already have an account?"
                    },
                    "action": {
                        "buttons": [
                            {
                                "type": "reply",
                                "reply": {
                                    "id": "001",
                                    "title": "Sign up 😁"
                                }
                            },
                            {
                                "type": "reply",
                                "reply": {
                                    "id": "002",
                                    "title": "Log in 😄"
                                }
                            }
                        ]
                    }
                }
            }

    return data

def ListMessage(number):
    data =  {
                "messaging_product": "whatsapp",
                "recipient_type": "individual",
                "to": number,
                "type": "interactive",
                "interactive": {
                    "type": "list",
                    "header": {
                        "type": "text",
                        "text": "Options"
                    },
                    "body": {
                        "text": "how could i help you?"
                    },
                    "footer": {
                        "text": "help"
                    },
                    "action": {
                        "button": "View options",
                        "sections": [
                            {
                                "title": "Hello",
                                "rows": [
                                    {
                                        "id": "si",
                                        "title": "Buy",
                                        "description": "Comprar"
                                    },
                                    {
                                        "id": "no",
                                        "title": "Sell",
                                        "description": "Vender"
                                    }
                                ]
                            },
                            {
                                "title": "Info?",
                                "rows": [
                                    {
                                        "id": "si",
                                        "title": "Contact Center",
                                        "description": "Contacto"
                                    },
                                    {
                                        "id": "no",
                                        "title": "Agency",
                                        "description": "Informacion de la agencia"
                                    }
                                ]
                            }
                        ]
                    }
                }
            }

    return data