from openai import OpenAI
import os
client = OpenAI(
    api_key=os.getenv("DEEPSEEK_KEY"),
    base_url="https://api.deepseek.com"
)


messages = [{"role":"system","content":"你是一个金融术语翻译器。"}]

print("金融术语翻译器(按q退出)")

while True:
    user_input = input("\n你:")
    if user_input == "q":
        print("再见")
        break
    messages.append({"role":"user","content":user_input})
    respones = client.chat.completions.create(
        model="deepseek-chat",
        messages=messages
    )
    reply = respones.choices[0].message.content
    messages.append({"role":"assistant","content":reply})
    print(f"翻译：{reply}")