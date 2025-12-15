import google.genai as genai 

class AIAssistant:
    """
    Wrapper around Gemini API calls.
    Handles single-prompt responses and full chat conversations.
    """
    
    def __init__(self, api_key):
        self.client = genai.Client(api_key=api_key)
            
            
    def ask(self, prompt: str) -> str:
        try:
            response = self.client.models.generate_content(
                model="gemini-2.0-flash",
                contents=prompt,
                config={"temperature": 0.4}
            )
            return response.text
        except Exception as e:
            return f"Gemini error: {str(e)}"
        