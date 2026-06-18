# Responces for the Available Commands

responses = {
    "hello": "Hi there! 👋",
    "hi": "Hello! 😊",

    "how are you": "I'm doing great today!",
    "what is your name": "I am LogicBot 🤖",
    "who created you": "I was created as a Rule-Based AI Chatbot.",

    "good morning": "Good Morning! 🌞",
    "good evening": "Good Evening! 🌙",

    "thanks": "You're welcome! 😄",
    "bye": "Goodbye! Have a wonderful day! 👋",

    "tell me a joke": "Why do programmers prefer dark mode? Because light attracts bugs! 😂",

    "what can you do": "I can respond to predefined commands and demonstrate rule-based AI concepts.",

    "what is ai": "AI stands for Artificial Intelligence, where machines simulate human intelligence.",

    "what is python": "Python is a popular programming language widely used in AI and Data Science.",

    "motivate me": "Success is the sum of small efforts repeated every day. 🚀",

    "who are you": "I am LogicBot, a Rule-Based AI Chatbot.",

    "version": "LogicBot Version 1.0",

    "date": "I am a rule-based chatbot and cannot fetch the current date.",

    "favorite language": "As a chatbot, I like Python because it is simple and powerful! 🐍",

    "help": """
    Available commands - 
    hello,
    how are you,
    what is your name,
    who are you,
    what can you do,
    what is ai,
    what is python,
    tell me a joke,
    motivate me,
    version,
    thanks,
    bye
"""
}


def get_response(user_input):
    clean_input = user_input.lower().strip()

    if clean_input == "exit":
        return "Session ended. Goodbye!"
    
    return responses.get(
        clean_input,
        "Sorry, I don't understand that command. Type 'help' to see available commands."
    )
