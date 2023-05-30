'''import random

# define a function to handle the bot's responses
def bot_response(user_input):
    # create a list of possible bot responses
    responses = ["Hello!", "How are you?", "What can I do for you?", "I don't understand.", "Goodbye!"]
    # return a random response from the list
    return random.choice(responses)

# start the chatbot
print("Welcome to the chatbot!")
while True:
    # get user input
    user_input = input("You: ")
    # check if user wants to quit
    if user_input.lower() == "quit":
        print("Goodbye!")
        break
    # respond with the bot's response
    bot_response = bot_response(user_input)
    print("Bot:", bot_response)'''

import random
responses = {
"hello": ["Hi there!", "Hello, how can I help you?", "Hey! What can I do for you?"],
"goodbye": ["Goodbye!", "See you later!", "Bye! Have a nice day!"],
"thank you": ["You're welcome!", "No problem!", "Happy to help!"],
"help": ["Sure, what do you need help with?", "What do you need assistance with?", "How can I assist you?"],
"default": ["I'm sorry, I don't understand. Can you please rephrase that?", "Please provide moreinformation.", "I'm not sure what you mean."]
}
while True:
    user_input = input("User: ")
    if user_input.lower() in responses:
        bot_response = random.choice(responses[user_input.lower()])
    else:
        bot_response = random.choice(responses["default"])
    print("Bot:", bot_response)