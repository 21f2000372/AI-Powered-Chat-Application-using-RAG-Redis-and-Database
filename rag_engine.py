import os
import openai
from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

def read_pdf_text(path):
    from PyPDF2 import PdfReader
    reader = PdfReader(path)
    text = ""
    for page in reader.pages:
        text += page.extract_text()
    return text.strip()

pdf_text = read_pdf_text("data/sample_doc.pdf")

# def get_rag_answer(query: str) -> str:
#     prompt = f"Answer the question based on this text:\n\n{pdf_text}\n\nQuestion: {query}"
    
#     response = openai.chat.completions.create(
#         model="gpt-3.5-turbo",
#         messages=[
#             {"role": "system", "content": "You are a helpful assistant."},
#             {"role": "user", "content": prompt}
#         ]
#     )
#     return response.choices[0].message.content

def get_rag_answer(query: str) -> str:
    from openai import OpenAIError
    prompt = f"Answer the question based on this text:\n\n{pdf_text}\n\nQuestion: {query}"
    
    try:
        response = openai.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": prompt}
            ]
        )
        return response.choices[0].message.content
    except openai.RateLimitError:
        return "Rate limit reached. Please try again later."
    except Exception as e:
        return f"Error generating response: {str(e)}"

