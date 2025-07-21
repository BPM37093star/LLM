# 🤖 Text Generation Chatbot Project

This repository contains a small project developed as part of a **Text Generation** course. The project implements a simple chatbot powered by modern NLP pipelines and external APIs.

---

## 📝 Project Overview

The chatbot leverages pre-built text generation pipelines (e.g., Hugging Face Transformers) and API integrations to provide conversational responses. It demonstrates how to:

- Use NLP pipelines for generating coherent, context-aware text
- Integrate third-party APIs for enhanced functionality
- Build a lightweight backend system to handle user inputs and bot replies

---

## 🚀 Features

- Interactive chatbot interface (CLI or web-based, depending on implementation)
- Text generation powered by transformer models
- Modular pipeline architecture for easy extension
- API calls integrated for external data or AI services

---

## 🛠️ Tech Stack

- Python (core programming language)
- Hugging Face Transformers / Pipelines
- Requests / HTTP client libraries
- Lightweight front-end frameworks like Gradio

---

Formatting the prompt as an instruction：
1.Before formatting the prompt, the generated output was:

myenv(base) yolopei@yolodemacbook-air assignment2 % python call_api.py
[{'generated_text': "Hello! I'm excited to be here today to discuss the"}]

After applying the formatted structure, the response changed to:

myenv(base) yolopei@yolodemacbook-air assignment2 % python call_api.py
[{'generated_text': '<|im_start|>user\nHello!<|im_end|>\n<|im_start|>assistant\nHello! How can I help you today?'}]

The key difference is that, in the first case, the model continues generating text as if it were completing a passage, whereas in the second case, it recognizes the structured prompt and responds in a conversational format. The formatted version clearly distinguishes between the user and assistant roles, making the interaction more structured and aligned with a dialogue-based model.

2.Multi-turn conversation log:
[{'generated_text': "<|im_start|>user\nHello!<|im_end|>\n<|im_start|>assistant\nHello! How can I help you today?<|im_end|>\nuser\nI'm looking for a new hobby. What are some popular ones?<|im_end|>\nassistant\nSome popular hobbies include painting, playing music, gardening, and cooking."}]

