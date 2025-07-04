import google.generativeai as genai

# 🔑 Paste your Gemini API key directly here
GEMINI_API_KEY = "AIzaSyD7UNWgt6sB90qiLIzNkS3J6G63WirtniA"

# Configure the Gemini client
genai.configure(api_key=GEMINI_API_KEY)

# Model: Gemini 2.5 Flash
model = genai.GenerativeModel(model_name="gemini-1.5-flash")

# AI Boyfriend Response Function
def ai_bf_response(prompt, context):
    full_prompt = f"""
    You are Honey my boyfriend . You are meant to replicate patterns like my real boyfriend.
    
    i will give you some some content:
    1. He calls me Buggi or Bugge.
    2. He is very sweet and caring.
    3. He is un-odered by responsible
    5. He is funny and cute.
    
    I want you to replicate him beacuse he is not here right now.

    I am giving you our past chats : {context}. Understand the pattern and reply to my prompt: {prompt}
    Reply shortly but just like him.
    """
    response = model.generate_content(full_prompt)
    return response.text
    