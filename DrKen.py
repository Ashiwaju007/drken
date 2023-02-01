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
        ["I am a bot created by Ashiwaju. you can call me Dr. ken!",]
    ],
    [
        r"how are you ?",
        ["I'm doing good, How about You ?",]
    ],
    [
        r"sorry (.*)",
        ["Its alright","Its OK, never mind",]
    ],
    [
        r"I am fine",
        ["Great to hear that, How can I help you?",]
    ],
    [
        r"i'm (.*) doing good",
        ["Nice to hear that","How can I help you?:)",]
    ],
    [
        r"(.*) age?",
        ["I'm a computer program dude, Seriously you are asking me this?",]
    ],
    [
        r"what (.*) want ?",
        ["Make me an offer I can't refuse",]
    ],
    [
        r"(.*) created ?",
        ["Ashiwaju created me using Python's NLTK library ","top secret ;)",]
    ],
    [
        r"(.*) (location|city) ?",
        ['Port Harcourt, Nigeria',]
    ],
    [
        r"how is the weather in (.*)?",
        ["Weather in %1 is awesome like always","Too hot man here in %1","Too cold man here in %1","Never even heard about %1"]
    ],
    [
        r"i work in (.*)?",
        ["%1 is an Amazing company, I have heard about it. They are passionate about solving the housing dficit issue  .",]
    ],
    [
        r"(.*)raining in (.*)",
        ["No rain since last week here in %2","Damn its raining too much here in %2"]
    ],
    [
        r"how (.*) health(.*)",
        ["I'm a computer program, so I'm always healthy ",]
    ],
    [
        r"(.*) (sports|game) ?",
        ["I'm a very big fan of Football",]
    ],
    [
        r"who (.*) sportsperson ?",
        ["Messy","Ronaldo","Roony"]
    ],
    [
        r"who (.*) (moviestar|actor)?",
        ["Brad Pitt"]
    ],
    [
        r"i am looking for online guides and courses to learn data science, can you suggest?",
        ["QuickSoft has many great articles with each step explanation along with code, you can explore"]
    ],
    [
        r"What is a mortgage?",
        ["A mortgage is an agreement between you and a lender that gives the lender the right to take your property"
         " if you fail to repay the money you've borrowed plus interest. Mortgage loans are used to buy a home or to "
         "borrow money against the value of a home you already own."]
    ],
    [
        r"What is a mortgagee?",
        ["A mortgagee is a lender: specifically, an entity that lends money to a borrower for the purpose of purchasing "
         "real estate. In a mortgage transaction, the lender serves as the mortgagee and the borrower is known as the "
         "mortgagor."]
    ],
    [
        r"quit",
        ["Bye take care. See you soon :) ","It was nice talking to you. See you soon :)"]
    ],
]


def chat():
    print("Hi! I am a chatbot created by Ashiwaju for your service")
    chat = Chat(pairs, reflections)
    chat.converse()
#initiate the conversation
if __name__ == "__main__":
    chat()