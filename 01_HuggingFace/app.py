import gradio as gr
from transformers import pipeline

chatbot_model = pipeline("text-generation", model="gpt2")

def chat(message, history):
    response = chatbot_model(message, max_length=100, num_return_sequences=1)
    return response[0]["generated_text"]

iface = gr.ChatInterface(
    fn=chat,
    title="Chatbot NLP – Yulieth",
    description="Chatbot sencillo usando Hugging Face y GPT-2"
)

iface.launch()
