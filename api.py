# api_fastapi.py
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from chatbot_exam import chat
import nltk
nltk.download('stopwords')
nltk.download('punkt')


app = FastAPI()

class UserInput(BaseModel):
    user_input: str

@app.post("/api/chat")
def chat_api(data: UserInput):
    try:
        user_input = data.user_input

        response, confidence_score, predicted_tag = chat(user_input)

        result = {
            'response': response,
            'confidence_score': confidence_score,
            'predicted_tag': predicted_tag
        }

        return result

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000, log_level="info")
