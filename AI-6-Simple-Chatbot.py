print("Type 'bye' to exit.")

while True:
    message = input("You: ").lower()

    if "bye" in message:
        print("Bot: Goodbye!")
        break
    elif "hello" in message or "hi" in message:
        print("Bot: Hello!")
    elif "how are you" in message:
        print("Bot: I am fine.")
    elif "your name" in message:
        print("Bot: I am a simple chatbot.")
    else:
        print("Bot: I do not understand.")
