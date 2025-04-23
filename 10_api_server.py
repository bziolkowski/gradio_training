from openai import AzureOpenAI
import gradio as gr

client = AzureOpenAI(
    azure_endpoint="",  # tu_wstaw_endpoint
    api_key="",  # tu_wstaw_api_key
    api_version="2025-03-01-preview",
    azure_deployment="isdd-gpt-4o-2024-11-20-gs",
)

def respond_single(message):
    conversation = []
    conversation.append({"role": "user", "content": message})
    response = client.chat.completions.create(
        model = "isdd-gpt-4o-2024-11-20-gs",
        messages = conversation,
    )
    return response.choices[0].message.content

with gr.Blocks() as ui:
    response = gr.Textbox()
    text = gr.Textbox(placeholder="Zadaj pytanie")
    text.submit(respond_single, inputs=[text], outputs=[response])

ui.launch()