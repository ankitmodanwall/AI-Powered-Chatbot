import openai

# Set your OpenAI API key here
openai.api_key = 'YOUR_API_KEY'  # 🔐 Replace with your actual key or use environment variable

# Store conversation history
conversation_history = [
    {"role": "system", "content": "You are a helpful assistant."}
]

def get_chatbot_response(user_input):
    # Add user message to history
    conversation_history.append({"role": "user", "content": user_input})

    # Get response from OpenAI
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=conversation_history
    )

    # Extract and store assistant's reply
    reply = response['choices'][0]['message']['content']
    conversation_history.append({"role": "assistant", "content": reply})
    return reply

def display_conversation():
    print("\n--- 💬 Conversation History ---")
    for msg in conversation_history[1:]:  # Skip system prompt
        role = "You" if msg["role"] == "user" else "Chatbot"
        print(f"{role}: {msg['content']}")

def main():
    print("Welcome to the AI-Powered Chatbot!")
    print("Type 'exit' to quit the chat.")
    print("Type 'history' to view the conversation so far.")

    while True:
        user_input = input("\nYou: ")
        if user_input.lower() == 'exit':
            print("Exiting the chatbot. Goodbye!")
            break
        elif user_input.lower() == 'history':
            display_conversation()
            continue

        response = get_chatbot_response(user_input)
        print(f"Chatbot: {response}")

if __name__ == "__main__":
    main()
