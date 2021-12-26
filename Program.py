import os
import openai
 ## use the openai and gradio libary to train data and output text that
 ## the user wants to  talk to the ai with and be like a maid
 ## import the api key for openai from your account
openai.api_key = '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'

## write a test script that will verify if the openai key is being used correctly
## and if the api key is being used correctly
#print(openai.api_key,"You have used the api key correctly.")

## write a function that will take in the user input and return the response
## from the openai api
def talk_to_ai(user_input):
    ## use the openai api to get the response from the user input
    response = openai.Completion.create(engine='davinci-codex',
                                        prompt=user_input,
                                        max_tokens=20)
    ## return the response
    return response.choices[0].text
    ## use the macintosh voice to say the response and ask the user
    ### what commands they want
    say(response.choices[0].text)
    user_input = input("What do you want to do? ")
    return user_input
    print(talk_to_ai(user_input))

    ### make openai ask the user a 
    ## a question using the openai data structure
    ## and return the response
    print(response.choices[0].text)