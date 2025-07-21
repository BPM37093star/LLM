import torch
import transformers
import gradio as gr
from transformers import pipeline

models = {
    "GPT-2": "gpt2",
    "DistilGPT-2": "distilgpt2",
    "GPT-Neo 125M": "EleutherAI/gpt-neo-125M"
}

generators = {name: pipeline("text-generation", model=model_id) for name, model_id in models.items()}


def text_generate(prompt, temperature, max_length, top_p, model_name):
    generator = generators[model_name]
    do_sample = False if temperature == 0 else True
    output = generator(prompt, temperature=temperature, max_length=max_length, top_p=top_p, do_sample=do_sample)
    return output[0]['generated_text']

demo = gr.Interface(
    fn=text_generate,
    inputs=[gr.Textbox(lines=5), 
            gr.Slider(label="Temperature", value=1, minimum=0, maximum=2), 
            gr.Slider(label="Max Length", value=16, minimum=1, maximum=256), 
            gr.Slider(label="Top P", value=1, minimum=0, maximum=1),
            gr.Dropdown(label="Model", choices=list(models.keys()), value="GPT-2")],
    outputs=["text"],
    title="Multi-Model Text Generator",
    description="Select a language model from the dropdown menu to generate text."
)

demo.launch()