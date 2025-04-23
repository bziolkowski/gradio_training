import gradio as gr
import time

def processing():
    time.sleep(10)
    return "Koniec"

with gr.Blocks() as ui:
    text = gr.Textbox("Wciśnij przycisk")
    button = gr.Button("Start")
    button.click(fn=processing, outputs=text, concurrency_limit=3)

ui.queue(default_concurrency_limit=2)
ui.launch()

# w powyższym przypadku defaultowa liczba równolegle przetwarzanych zadań to 2, a dla processing po kliknięciu przycisku to 3