import openai

def GetResponse(text):
    try:
        openai.api_key = "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"
        result = openai.Completion.create(model = "text-davinci-003", prompt = text, n = 1, max_tokens = 500)

        response = result.choices[0].text
        return response

    except Exception as exception:
        print(exception)
        return "Error"
