import requests
import json

url = "https://llm.api.cloud.yandex.net/foundationModels/v1/completion"
headers = {
    "Content-Type": "application/json",
    "Authorization": "Api-Key <<VALIDATION_KEY>>"
}

def get_response(user_message: str):
    prompt = {
        "modelUri": "gpt://<<API_KEY>>/yandexgpt-lite",
        "completionOptions": {
            "stream": False,
            "temperature": 0.6,
            "maxTokens": "2000"
        },
        "messages": [
            {
                "role": "user",
                "text": user_message
            },
        ]
    }
    response = requests.post(url, headers=headers, json=prompt)

    if response.status_code == 200:
        result = response.text
        return json.loads(result)['result']['alternatives'][0]['message']['text']
    else:
        return (f"Ошибка при работе с нейросетью.\n"
                f"Приносим свои извинения!\n"
                f"Код ошибки: {response.status_code}")
