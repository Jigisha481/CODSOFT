def reply(message):
    msg = message.lower()

    if "hi" in msg or "hello" in msg:
        return "Hello! Nice to meet you."
    
    if "how are you" in msg:
        return "I'm doing well! What about you?"
    
    if "name" in msg:
        return "I'm a small chatbot created for my AI internship task."
    
    if "help" in msg:
        return "I can reply to basic questions. Try asking me something!"
    
    if "bye" in msg:
        return "Bye! Have a good day."

    # default response
    return "I didn't understand that, but I'm learning!"

print("Chatbot: Hello! Type something (type 'bye' to stop).")

while True:
    user = input("You: ")
    if user.lower() == "bye":
        print("Chatbot: Bye! Take care.")
        break
    print("Chatbot:", reply(user))
