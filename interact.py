from chatbot_exam import chat 

while True:
    user_input = input("User: ")
    if user_input.lower() == 'exit':
        print("Exiting the chatbot.")
        break
    
    response, confidence_score, predicted_tag = chat(user_input)
    
    print(f"Chatbot: {response}")
    print(f"Confidence Score: {confidence_score}")
    print(f"Predicted Tag: {predicted_tag}")
