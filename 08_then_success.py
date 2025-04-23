import gradio as gr
import time

def processing():
    time.sleep(3)
    return "Koniec"

def processing_with_exception():
    time.sleep(3)
    raise Exception("Olaboga")

def result():
    return gr.Textbox("Sukces", visible=True)

with gr.Blocks() as ui:
    text = gr.Textbox("Wciśnij przycisk")
    button = gr.Button("Start")
    text2 = gr.Textbox(visible=False)

    # tu success zawsze zadziała
    button.click(fn=processing, outputs=text).then(result, outputs=text2)

    # tu success zadziała
    # button.click(fn=processing, outputs=text).success(result, outputs=text2)

    # tu success nie zadziała
    # button.click(fn=processing_with_exception, outputs=text).success(result, outputs=text2)

# pwa ustawione na True umożliwia uruchomienie aplikacji w trybie Progressive Web App
ui.launch(pwa=True)