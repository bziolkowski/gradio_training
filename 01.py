import gradio as gr

def submit(text):
    text = text.lower()
    return gr.Textbox(value=text, visible=True), gr.Textbox(value="", visible=False)

with gr.Blocks() as ui:
    text1 = gr.Textbox()
    text2 = gr.Textbox(label="Wynik", visible=False)
    text1.submit(fn=submit, inputs=text1, outputs=[text2,text1])

ui.launch()