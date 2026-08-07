from openai import OpenAI

client = OpenAI(
    api_key="sk-604d4f8ceb6c4cd2bd36563837515d82",
    base_url="https://api.deepseek.com"
)

response = client.chat.completions.create(
    model="deepseek-chat",
    messages=[
        {"role": "system", "content": "你是一个金融术语翻译器。用通俗的语言解释金融概念。"},
        {"role": "user", "content": "什么是量化宽松？"}
    ]
)

print(f"模型：{response.model}")
print(f"消耗 tokens：{response.usage.total_tokens}")
print(f"回复内容：{response.choices[0].message.content}")