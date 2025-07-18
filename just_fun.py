def jarvis_response(command):
    command = command.lower()

    if "hello" in command:
        return "Hello! I'm Jarvis. How can I assist you?"
    elif "time" in command:
        from datetime import datetime
        return f"The current time is {datetime.now().strftime('%H:%M:%S')}"
    elif "open youtube" in command:
        import webbrowser
        webbrowser.open("https://youtube.com")
        return "Opening YouTube."
    else:
        return "Sorry, I didn't understand that."

while True:
    cmd = input("You: ")
    if cmd in ['exit', 'quit']:
        break
    print("Jarvis:", jarvis_response(cmd))
