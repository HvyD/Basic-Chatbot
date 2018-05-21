#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
EchoBot
Created on Mon May 21 10:57:45 2018

@author: hvyd
"""
import random
import re




bot_template = "BOT : {0}"
user_template = "USER : {0}"

# function that responds to a user's message: respond
#def respond(message):
    # Concatenate the user's message to the end of a standard bot respone
  #  bot_message = "I can hear you! You said: " + message
   # return bot_message

# variables
name = "DUDE"
weather = "cloudy with a chance of shit"

# dictionary with the predefined responses
responses = {
  "what's your name?": [
      "my name is {0}".format(name),
      "they call me {0}".format(name),
      "I go by {0}".format(name)
   ],
  "what's today's weather?": [
      "the weather is {0}".format(weather),
      "it's {0} today".format(weather)
    ],
  "default": ["Wut u dis say"]
}

# Randomly returns the matching response if there is one, default otherwise
def respond(message):
    # Check if the message is in the responses
    if message in responses:
        # Return a random matching response
        bot_message = random.choice(responses[message])
    else:
        # Return a random "default" response
        bot_message = random.choice(responses["default"])
    return bot_message

    if message.endswith("?"):
        # Return a random question
        return random.choice(responses["question"])
    # Return a random statement
    return random.choice(responses["statement"])
    
 # Call match_rule
    response, phrase = match_rule(rules, message)
    if '{0}' in response:
        # Replace the pronouns in the phrase
        phrase = replace_pronouns(phrase)
        # Include the phrase in the response
        response = response.format(phrase)
    return response

    

# function that sends a message to the bot: send_message
def send_message(message):
    # Print user_template including the user_message
    print(user_template.format(message))
    # Get the bot's response to the message
    response = respond(message)
    # Print the bot template including the bot's response.
    print(bot_template.format(response))


# Define match_rule()
def match_rule(rules, message):
    response, phrase = "default", None
    
    # Iterate over the rules dictionary
    for pattern, responses in rules.items():
        # Create a match object
        match = re.search(pattern, message)
        if match is not None:
            # Choose a random response
            response = random.choice(responses)
            if '{0}' in response:
                phrase = match.group(1)
    # Return the response and phrase
    return response, phrase

# Define replace_pronouns()
def replace_pronouns(message):

    message = message.lower()
    if 'me' in message:
        # Replace 'me' with 'you'
        return re.sub('me', 'you', message)
    if 'my' in message:
        # Replace 'my' with 'your'
        return re.sub('my', 'your', message)
    if 'your' in message:
        # Replace 'your' with 'my'
        return re.sub('your', 'my', message)
    if 'you' in message:
        # Replace 'you' with 'me'
        return re.sub('you', 'me', message)

    return message
# Test replace pronouns
#print(replace_pronouns("my last birthday"))
#print(replace_pronouns("when you went to Florida"))
#print(replace_pronouns("I had my own castle"))

# Test match_rule
#print(match_rule(rules, "do you remember your last birthday"))

# Send a message to the bot
#send_message("what's your name?")
    
# Send the messages
#send_message("do you remember your last birthday")
#send_message("do you think humans should be worried about AI")
#send_message("I want a robot friend")
#send_message("what if you could be anything you wanted")
