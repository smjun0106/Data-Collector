import openai
import gradio

openai.api_key = "####"

messages = [{"role": "system", "content": "You are an expert on logical and critical thinking skills"}]

def CustomChatGPT(input):
    messages.append({"role": "user", "content": input})
    response = openai.ChatCompletion.create(
        model = "gpt-3.5-turbo",
        messages = messages
    )
    ChatGPT_reply = response["choices"][0]["message"]["content"]
    messages.append({"role": "assistant", "content": ChatGPT_reply})
    return ChatGPT_reply

demo = gradio.Interface(fn=CustomChatGPT, inputs = "text", outputs = "text", title = "ThoughtCoach")

demo.launch(share=True)
