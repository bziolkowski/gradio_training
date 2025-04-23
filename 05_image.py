import gradio as gr
import numpy as np

def sepia(input_img):
    sepia_filter = np.array([
        [0.393, 0.769, 0.189],
        [0.349, 0.686, 0.168],
        [0.272, 0.534, 0.131]
    ])
    sepia_img = input_img.dot(sepia_filter.T)
    sepia_img /= sepia_img.max()
    return sepia_img

with gr.Blocks() as ui:
    title_image = gr.Image('assets/rebus.png', type='filepath')
    input_image = gr.Image(type='numpy', label="Input image")
    output_image = gr.Image(type='numpy', label="Output image")

    input_image.change(sepia, inputs=input_image, outputs=output_image)

ui.launch()

