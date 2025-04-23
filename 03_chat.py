import gradio as gr
from openai import AzureOpenAI

client = AzureOpenAI(
    azure_endpoint="", # tu_wstaw_endpoint
    api_key="", # tu_wstaw_api_key
    api_version="2025-03-01-preview",
    azure_deployment="isdd-gpt-4o-2024-11-20-gs",
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

def chat_stream(message, chatbot):
    conversation = []
    conversation.extend(chatbot)
    conversation.append({"role": "user", "content": message})
    stream = client.chat.completions.create(
        model="isdd-gpt-4o-2024-11-20-gs",
        messages=conversation,
        stream=True
    )

    conversation.append({"role": "assistant", "content": ""})

    for chunk in stream:
        if chunk.choices:
            if chunk.choices[0].delta.content is not None:
                chunk_text = chunk.choices[0].delta.content
                conversation[-1]["content"] += chunk_text
                yield conversation

with gr.Blocks(theme=gr.themes.Soft()) as ui:
    chatbot = gr.Chatbot(type='messages')
    message = gr.Textbox()
    button = gr.Button("Wyślij")


    # wysyłamy nową wiadomość i historię rozmowy (z chatbota), odbieramy pustą wiadomość (czyścimy) oraz chatbota z naszą wiadomością i odpowiedzią
    message.submit(fn=chat, inputs=[message, chatbot], outputs=[message, chatbot])

    # tutaj korzystamy z funkcje chat_stream, aby otrzymywać odpowiedź w czasie rzeczywistym
    # message.submit(fn=chat, inputs=[message, chatbot], outputs=[chatbot])
    # Alternatywnie możemy wywołać funkcję klikając w przycisk
    # button.click(fn=chat_stream, inputs=[message, chatbot], outputs=[chatbot])

    # Dla

ui.launch()



# Przykład wymiany wiadomości w formacie ChatML:
# [{"role": "user", "content": "czesc"}, {"role": "assistant", "content": "no czesc"}]