# interact_fastapi.py
import httpx

url = "http://127.0.0.1:8000/api/chat"

def interact_with_chatbot(user_input):
    payload = {"user_input": user_input}

    with httpx.Client() as client:
        response = client.post(url, json=payload)

    if response.status_code == 200:
        return response.json()
    else:
        return {"error": f"Failed to interact with chatbot. Status Code: {response.status_code}"}

if __name__ == "__main__":
    while True:
        user_input = input("User: ")

        if user_input.lower() == 'exit':
            print("Exiting the chatbot.")
            break

        result = interact_with_chatbot(user_input)

        print(f"Chatbot: {result['response']}")
        print(f"Confidence Score: {result['confidence_score']}")
        print(f"Predicted Tag: {result['predicted_tag']}")
