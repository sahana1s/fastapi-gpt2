# main.py
from fastapi import FastAPI
from pydantic import BaseModel
from transformers import pipeline

# Initialize FastAPI app
app = FastAPI()

# Load Hugging Face model
generator = pipeline('text-generation', model='gpt2')

# Define the input format for the API
class InputText(BaseModel):
    text: str

# Define the endpoint for text generation
@app.post("/generate/")
async def generate_text(input_text: InputText):
    result = generator(input_text.text, max_length=50, num_return_sequences=1)
    return {"generated_text": result[0]['generated_text']}
