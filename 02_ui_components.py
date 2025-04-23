import gradio as gr

def process():
    return "jest ok"

def enable_button():
    return gr.Button(interactive=True), gr.Button(interactive=True)

def dd_list_fun(input_data):
    return input_data

def radio_and_checkbox(radio, checkbox):
    return f"RADIO: {radio}; CHECKBOX: {checkbox}"

with gr.Blocks() as ui:
    # ui elements
    with gr.Tab(label="Tab 1"):
        with gr.Row(visible=True) as row:
            button1 = gr.Button(value="Wyślij", interactive=False, scale=1)
            button2 = gr.Button(value="Tylko radio i checkbox", interactive=False, scale=3)
        with gr.Row():
            with gr.Column(scale=3):
                text = gr.Textbox(interactive=True)
                dd_list = gr.Dropdown(choices=["opcja1", "opcja2", "opcja3"], value="opcja2", multiselect=True, interactive=True)
            with gr.Column(scale=1):
                radio = gr.Radio(choices=["opcja1", "opcja2", "opcja3"], value="opcja2", interactive=True)
                checkbox_group = gr.CheckboxGroup(choices=["opcja1", "opcja2", "opcja3"], value="opcja2", interactive=True)
        with gr.Accordion(label="Ważne opcje", open=False):
            number_el = gr.Number(value=5, interactive=True, minimum=-100, maximum=100, step=10)
            slider_el = gr.Slider(value=0.5, interactive=True, minimum=0, maximum=1, step=0.01)
    with gr.Tab(label="Tab 2"):
        new_button = gr.Button("Nowy przycisk")


    # event listeners
    text.change(fn=enable_button, outputs=[button1, button2])
    button1.click(fn=dd_list_fun, inputs=dd_list, outputs=text)
    button2.click(fn=radio_and_checkbox, inputs=[radio, checkbox_group], outputs=text)
ui.launch()