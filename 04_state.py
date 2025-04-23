import gradio as gr
from datetime import datetime

def set_time():
    current_time = str(datetime.now().time())
    return current_time, current_time

with gr.Blocks() as ui:
    time = gr.State("")
    title = gr.Markdown("")
    ui.load(fn=set_time, inputs=[], outputs=[time, title])
ui.launch()