import os
from anthropic import Anthropic
from dotenv import load_dotenv

load_dotenv()

client = Anthropic(api_key=os.getenv('ANTHROPIC_API_KEY'))

def run_chat():
    print('You: (type exit to quit)')
    goal=input("What is your goal? "
    system_message = "Your name is Lior, and you help people understand football better. You speak in a accessible manner, . Never say anything you don't know for a fact, and only answer questions related to soccer.. The user has a goal; help them achieve it:" + goal
    history = []
    num=1
    while True:
        print("       \n----------\n         ")
        user_input = input('>> ') + str(num)

        if user_input.lower() == 'exit':
            break
        elif user_input.lower() == 'reset':
            history = []
            print('History cleared.')
            continue
        
        num += 1

        history.append({'role': 'user', 'content': user_input})

        response = client.messages.create(
            model='claude-haiku-4-5-20251001',
            max_tokens=300,
            temperature=0.7,
            system=system_message,
            messages=history
        )


        reply = response.content[0].text
        print(f'lior: {reply}')
        history.append({'role': 'assistant', 'content': reply})

run_chat()

'''Reflection 1+2:  Every time I try to help my grandmother with technology, she forgets everything after five minutes.
I had a lot of issues with the libraries, but with the help of friends and artificial intelligence, I managed to overcome them.
It's like the Festigal with the arcade.
All the problems with the API were really annoying.
The AI ​​will lose the memory of its own answers
. It will remember only what I wrote and forget what it replied to me.
The program was running, but its memory was severely compromised.
 When I asked it, "What is my name?" (after having told it earlier),
   it couldn't answer because the history sent to it contained only my questions,
     without its own answers to link them together.   '''
     '''  Reflection 3:   All the behind-the-scenes work our Meet guides do that we don't see.
I had a problem with the code for a while and couldn't figure out what was going on; I was sure it was something major,
 but in the end, I just needed to move a single line of code. '''