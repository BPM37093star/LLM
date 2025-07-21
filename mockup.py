import torch
import transformers
import gradio as gr

def greet(prompt, temperature, max_length, top_p):
    return "Hello, world!"

demo = gr.Interface(
    fn=greet,
    inputs=[gr.Textbox(), gr.Slider(label="Temperature"), gr.Slider(label="Max Length"), gr.Slider(label="Top P")],
    outputs=["text"],
)

demo.launch()