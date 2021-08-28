#This is a Chatbot named Nibs.
#Use Exit to terminate The Chat.
import re
import random
from datetime import datetime
from datetime import date
no_food = "I hate eating anything because I'm a bot obviously!"
food = "If I were you, I would go to the internet and type exactly what you wrote there!"
def not_found():
        response = ["Could you please re-phrase that? ",
                "...",
                "Sounds about right.",
                "What does that mean?"][
        random.randrange(4)]
        return response
def message_probability(user_message, recognised_words, single_response=False, required_words=[]):
    message_certainty = 0
    has_required_words = True

    # Counts how many words are present in each predefined message
    for word in user_message:
        if word in recognised_words:
            message_certainty += 1

    # Calculates the percent of recognised words in a user message
    percentage = float(message_certainty) / float(len(recognised_words))

    # Checks that the required words are in the string
    for word in required_words:
        if word not in user_message:
            has_required_words = False
            break

    # Must either have the required words, or be a single response
    if has_required_words or single_response:
        return int(percentage * 100)
    else:
        return 0


def check_all_messages(message):
    highest_prob_list = {}

    # Simplifies response creation / adds it to the dict
    def response(bot_response, list_of_words, single_response=False, required_words=[]):
        nonlocal highest_prob_list
        highest_prob_list[bot_response] = message_probability(message, list_of_words, single_response, required_words)

    # Responses -------------------------------------------------------------------------------------------------------
    response(random.choice(['Hello !! This is Your Assistant Nibs','Hey !! I am Nibs ','Hiii !! This is Nibs ','Hey Buddy!!! I am Nibs .']), ['hello', 'hi','hii', 'hey', 'sup', 'heyo'], single_response=True)
    response(random.choice(['bye!!','Have a Good Day !!!','See You Soon','See you!']), ['bye','Gooddbye'], single_response=True)
    response(random.choice(['Good','Fine.','I am Working fine.']), ['how', 'are', 'you', 'doing'], required_words=['how'])
    response(random.choice(['Mention Not !!!','Thank You','You are Welcome!!']), ['thank', 'thanks','great'], single_response=True)
    response(datetime.now().strftime("%H:%M:%S"), ['what', 'the', 'time'], required_words=['time'])
    response(date.today(), ['what', 'the', 'date'], required_words=['date'])


    # Longer responses
    response(food, ['give', 'advice'], required_words=['advice'])
    response(no_food, ['what', 'you', 'eat'], required_words=['you', 'eat'])

    best_match = max(highest_prob_list, key=highest_prob_list.get)
    # print(highest_prob_list)
    # print(f'Best match = {best_match} | Score: {highest_prob_list[best_match]}')

    return not_found() if highest_prob_list[best_match] < 1 else best_match


# Used to get the response
def get_response(user_input):
    split_message = re.split(r'\s+|[,;?!.-]\s*', user_input.lower())
    response = check_all_messages(split_message)
    return response


# Testing the response system
print("Hey There !!! This is your Virtual assistant Nibs!!")
while True:
    user=input('You: ')
    if ( user.casefold()=='exit' ):
         break
    response=get_response(user)
    print('Bot: ' , response)
print('Bot: ' + 'Thank You for using Me.')
