import torch
import transformers
import gradio as gr
from transformers import pipeline

text_generator = pipeline("text-generation", model="gpt2")

def text_generate(prompt, temperature, max_length, top_p):
    do_sample = False if temperature == 0 else True
    output = text_generator(prompt, temperature=temperature, max_length=max_length, top_p=top_p, do_sample=do_sample)
    return output[0]['generated_text']

demo = gr.Interface(
    fn=text_generate,
    inputs=[gr.Textbox(lines=5), 
            gr.Slider(label="Temperature", value=1, minimum=0, maximum=2), 
            gr.Slider(label="Max Length", value=16, minimum=1, maximum=256), 
            gr.Slider(label="Top P", value=1, minimum=0, maximum=1)],
    outputs=["text"],
)

demo.launch()