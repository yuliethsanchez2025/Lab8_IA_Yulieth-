01_HuggingFace/README.md

# Evidencias Hugging Face

# 🚀 Evidencias — Hugging Face (Parte 2.1)

Este apartado contiene todas las evidencias solicitadas en la sección **2.1 del Laboratorio 8**: exploración de modelos, ejecución en notebook, desarrollo de un Space y análisis técnico.

---

## 📌 1. Modelos explorados

Se exploraron 3 modelos representativos de las categorías requeridas:

### 🔹 **NLP – distilbert-base-uncased-finetuned-sst-2-english**
Modelo de clasificación de sentimiento basado en BERT, reducido y optimizado.

### 🔹 **Visión – google/vit-base-patch16-224**
Modelo de clasificación de imágenes basado en Vision Transformer.

### 🔹 **Audio – facebook/wav2vec2-base-960h**
Modelo para reconocimiento de voz entrenado sobre 960 horas de audio.

---

## 📌 2. Notebook ejecutado (Pipeline NLP)
Se ejecutó un modelo NLP utilizando el pipeline de **sentiment-analysis** de Hugging Face.

📎 **Evidencias del notebook:**  
- `Captura de pantalla 2025-11-22 021210.png`  
- `notebook_ejecucion_2.png`  


El código usado fue:

```python
from transformers import pipeline

classifier = pipeline("sentiment-analysis")
result = classifier("I love studying artificial intelligence!")
result

---

## 📌 3. Hugging Face Space publicado

Se creó un **chatbot funcional** utilizando Gradio y el modelo GPT-2.

🔗 **Enlace al Space:**  
https://huggingface.co/spaces/yysanchez/chatbot_yulieth 

### 📂 Archivos incluidos

- `app.py` → Código completo del chatbot  
- `requirements.txt` → Librerías necesarias  

---

## 📌 4. Análisis Técnico del Chatbot (GPT-2)

El chatbot fue creado usando **GPT-2**, un modelo basado en la arquitectura Transformer (Decoder Only).  
Este modelo genera texto prediciendo el siguiente token más probable según el contexto previo.  
Se integró mediante el pipeline de `text-generation` de Hugging Face.

### ✔ **Fortalezas**
- Rápido y ligero para la inferencia.  
- No requiere GPU para ejecutarse en Hugging Face Spaces.  
- Fácil de integrar con **Gradio**, ideal para prototipos.  
- Adecuado para fines educativos y demostrativos.  

### ✔ **Limitaciones**
- GPT-2 no está alineado a instrucciones modernas.  
- Puede generar respuestas incoherentes si la conversación es larga.  
- No posee memoria extendida ni capacidades de razonamiento.  

### ✔ **Rendimiento**
- Latencia aproximada: **1–2 segundos** por respuesta.  
- Funcionamiento estable en CPU dentro del Space.  
- Bajo consumo de memoria comparado con modelos más grandes.  

---



