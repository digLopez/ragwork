from openai import OpenAI

client = OpenAI(
    api_key="$MOONSHOT_API_KEY",
    base_url="https://api.moonshot.cn/v1",
)
completion = client.chat.completions.create(
    model="moonshot-v1-8k",
    messages=[
        {"role": "system", "content": "你是 Kimi，由 Moonshot AI 提供的人工智能助手。"},
        {"role": "user", "content": "你好，我叫李雷，1+1等于多少？"}
    ],
    temperature=0.3,
)
print(completion.choices[0].message.content)
