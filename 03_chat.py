import gradio as gr
from openai import AzureOpenAI

client = AzureOpenAI(
    azure_endpoint="your_endpoint",
    api_key="your_key",
    api_version="2025-03-01-preview",
    azure_deployment="your_deployment",
)

def chat(message, chatbot):

    # Tworzymy nową listę, aby było czytelniej (moglibyśmy pracować na chatbot)
    conversation = []

    # Wstawiamy historię rozmowy z chatbota
    conversation.extend(chatbot)

    # Dopisujemy naszą wiadomość w formacie ChatML
    conversation.append({"role": "user", "content": message})

    # Wysyłamy do OpenAI API
    response = client.chat.completions.create(
        model="isdd-gpt-4o-2024-11-20-gs",
        messages=conversation,
    )

    # Dopisujemy odpowiedź bota (z OpenAI)
    conversation.append({"role": "assistant", "content": response.choices[0].message.content})

    # Dopisujemy odpowiedź bota (tutaj bez AI)
    # conversation.append({"role": "assistant", "content": "ja nic nie wiem"})

    # zwracamy pusty string do okna wprowadzania tekstu oraz całą konwersację do obiektu chatbota
    return gr.Textbox(value=""), gr.Chatbot(value=conversation, type="messages")
    # można też tak:
    # return "", chatbot

with gr.Blocks() as ui:
    chatbot = gr.Chatbot(type='messages')
    message = gr.Textbox()


    # wysyłamy nową wiadomość i historię rozmowy (z chatbota), odbieramy pustą wiadomość (czyścimy) oraz chatbota z naszą wiadomością i odpowiedzią
    message.submit(fn=chat, inputs=[message, chatbot], outputs=[message, chatbot])


ui.launch()



# Przykład wymiany wiadomości w formacie ChatML:
# [{"role": "user", "content": "czesc"}, {"role": "assistant", "content": "no czesc"}]