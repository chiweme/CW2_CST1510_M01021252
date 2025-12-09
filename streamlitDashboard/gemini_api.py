import os
import google.genai as genai
from google.genai.types import GenerateContentConfig

#load API key from streamlit secrets or system environment
API_KEY = os.getenv("GEMINI_API_KEY")

if not API_KEY:
    raise ValueError("Missing GEMINI_API_KEY. Add it to your .streamlit/secrets.toml")
#create the Gemini client using the official Google GenAI SDK
client = genai.Client(api_key=API_KEY)

def ask_gemini(prompt: str) -> str:
    """
    sends a single prompt to Gemini and returns the model output. 
    parameters:
        prompt (str): the user question or input.
    returns: 
        str: the AI text output or an error message.
    """
    try:
        response = client.models.generate_content(
            model="gemini-2.0-flash",
            contents=prompt,
            config=GenerateContentConfig(
                temperature=0.4 #small creativity for clarity
            )
        )
    
        return response.text or "(No response received from Gemini)"
    except Exception as e:
        return f"Gemini API error: {str(e)}"



#def ask_gemini_chat(messages):
    """
    Takes a list of messages (conversation history) and returns model reply.
    `messages` must be a list of dicts: {"role": "user" or "model", "content": "..."}
    """
    
    #try:
        #response = client.responses.create(
            #model="gemini-2.0-flash",
            #contents=messages
        #)
        #return response.output_text
    
    #except Exception as e:
        #return f"Gemini API error: {str(e)}"
    