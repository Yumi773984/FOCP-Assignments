import random  # Importing the random module for random choices
import json    # Importing JSON to make the system configurable
import time    # Importing time to simulate random disconnections

# Configuration for keywords and responses
config = {
    "keywords": {
        "coffee": "The campus coffee bar is open from 8 AM to 8 PM every day.",
        "study": "The library is located in the main building and is open from 7 AM to 10 PM daily.",
        "help": "The SSD (Student Services Department) is available to assist you with any queries or issues. You can contact them via email at ssd@britishinternationalcollege.edu.np or visit the SSD.",
        "sports": "The university has a state-of-the-art sports center open from 6 AM to 10 PM."
    },
    "random_responses": [
        "That's an interesting question!", 
        "I'm not sure about that. Let me get back to you!", 
        "Could you please clarify?", 
        "I'm here to help, ask me anything!"
    ]
}

# Function to log the chat session
log_file = "chat_log.txt"  # Name of the log file
def log_chat(user_name, agent_name, user_input, agent_response):
    with open(log_file, "a") as log:
        log.write(f"{user_name}: {user_input}\n{agent_name}: {agent_response}\n")

# Function to simulate random disconnections
def simulate_disconnection():
    if random.randint(1, 10) == 1:  # 10% chance to disconnect
        print("Freya: Oops! It seems I've been disconnected. Please try again later.")
        return True
    return False

# Main chatbot function
def chatbot():
    print("Welcome to the University of Poppleton Chatbot!")
    user_name = input("Please enter your name: ")
    print(f"Hello, {user_name}! My name is Freya, your virtual assistant.")

    # Start the chat loop
    while True:
        user_input = input("\nAsk me a question or type 'bye' to exit: ").strip().lower()

        # Simulate random disconnection
        if simulate_disconnection():
            break

        # Exit condition
        if user_input in ["bye", "exit", "quit"]:
            print(f"Goodbye, {user_name}! Have a great day.")
            break

        # Check for keywords
        response = None
        for keyword, reply in config["keywords"].items():
            if keyword in user_input:
                response = reply
                break

        # Generate response
        if response:
            print(f"Freya: {response}")
        else:
            response = random.choice(config["random_responses"])
            print(f"Freya: {response}")

        # Log the interaction
        log_chat(user_name, "Freya", user_input, response)

# Run the chatbot
if __name__ == "__main__":
    chatbot()
