import os
import requests
from openai import OpenAI

from config import GPT_FREE_APIKEY


api_key = os.getenv("OPENAI_API_KEY", GPT_FREE_APIKEY)
base_urls = ["https://api.chatanywhere.tech/v1", "https://api.chatanywhere.com.cn/v1"]
client = OpenAI(api_key=api_key, base_url=base_urls[0])


def get_model_list():
    url = base_urls[0] + "/models"
    headers = {
        'Authorization': f'Bearer {api_key}',
        'User-Agent': 'Apifox/1.0.0 (https://apifox.com)'
        }
    response = requests.request("GET", url, headers=headers)
    if "error" in response.json():
        return response.json()
    data = response.json()['data']
    models = [model['id'] for model in data]
    return {"models": models}


def chat(model="gpt-3.5-turbo", messages=None, temperature=0.7):
    if messages is None:
        messages = []
    completion = client.chat.completions.create(
        model=model,
        messages=messages,
        temperature=temperature,
    )
    return completion.choices[0].message.content


def ask_llm(assistant_documents: list[str], user_question: str):
    # build message
    messages = []
    for document in assistant_documents:
        messages.append({"role": "system", "content": document})
    messages.append({"role": "user", "content": user_question})

    # chat
    answer = chat(messages=messages, model="gpt-3.5-turbo")
    return answer


if __name__ == '__main__':
    # print(get_model_list())
    ass_documents = ["你是百科全书", "周树人的笔名是鲁迅", "鲁迅的真名是周树人"]
    # sys_documents = []
    usr_question = "鲁迅和周树人的关系"
    print(ask_llm(ass_documents, usr_question))
