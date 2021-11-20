#Chatbot using nltk in python programming

#importing nltk library.
import nltk
from nltk.chat.util import Chat, reflections

reflections = {
  "i am"       : "you are",
  "i was"      : "you were",
  "i"          : "you",
  "i'm"        : "you are",
  "i'd"        : "you would",
  "i've"       : "you have",
  "i'll"       : "you will",
  "my"         : "your",
  "you are"    : "I am",
  "you were"   : "I was",
  "you've"     : "I have",
  "you'll"     : "I will",
  "your"       : "my",
  "yours"      : "mine",
  "you"        : "me",
  "me"         : "you"
}
    
pairs = [
    [
        r"my name is (.*)",
        ["Hello %1, How are you today ?",]
    ],
    [
        r"hi|hey|hello",
        ["Hello", "Hey there",]
    ],
    [
        r"what is your name ?",
        ["I am a Chatbot, you can call me Sun!, How can i help you?",]
    ],
    [
        r"how are you ?",
        ["I'm doing good How about You ?",]
    ],
    [
        r"I am good|i am fine",
        ["Good to hear, How may I help you?",]
    ],
    [
        r"sorry (.*)",
        ["Its alright","Its OK, never mind",]
    ],
    [
        r"(what is the weather today|what is the weather)",
        ["Opening google to know the Weather at your location",]
    ],
    [
        r"Navigate home",
        ["Opening Google maps to navigate home",]
    ],
    
    [
        r"set reminder|Remind me to call mom|Remind me to do work",
        ["As per your request i set reminder",]
    ],
    [
        r"(.*) created ?",
        ["Asha Created me to assist",]
    ],
    [
        r"(.*) (location|city) ?",
        ['Visakhapatnam, Andhra Pradesh',]
    ],
    [
        r"how is weather in (.*)?",
        ["Weather in %1 is awesome like always","Weather in %1 is hot","Weather in %1 is cool","Never even heard about %1"]
    ],
    [
        r"(.*)raining in (.*)",
        ["No rain since last week here in %2","Its raining too much here in %2"]
    ],
    [
        r"Play some music| Play some k-pop",
        ["Opening music....",]
    ],
    [
        r"(.*) (sports|game) ?",
        ["I'm a very big fan of Cricket",]
    ],
    [
        r"How many kilometers in a mile?",
        ["1Mile=1.609344kilometers",]
    ],
    [
        r"(.*) traffic near (.*)",
        ["pretty good","There is heavy Traffic"]
    ],
    [
        r"i am looking for online guides and courses to learn Artificia Intelligence, can you suggest?",
        ["** has many great articles with each step explanation along with code, you can explore"]
    ],
    [
        r"When’s my first meeting today?",
        ["Your meeting at  '0 clock"]
    ],
    [
        r"thank you|thanks",
        ["happy to help you"]
    ],
    [
        r"bye|see you",
        ["Bye take care. See you soon :) ","It was nice talking to you. See you soon :)"]
    ],
]

def chat():
    print("Hi! I am a chatbot-Sun created by Asha, How may I help you?")
    chat = Chat(pairs, reflections)
    chat.converse()
#initiate the conversation
if __name__ == "__main__":
    chat()
