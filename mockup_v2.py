import torch
import transformers
import gradio as gr

def greet(prompt, temperature, max_length, top_p):
    return "Hello, world!"

demo = gr.Interface(
    fn=greet,
    inputs=[gr.Textbox(lines=5), gr.Slider(label="Temperature", value=1, minimum=0, maximum=2), gr.Slider(label="Max Length", value=16, minimum=1, maximum=256), gr.Slider(label="Top P", value=1, minimum=0, maximum=1)],
    outputs=["text"],
)

demo.launch()