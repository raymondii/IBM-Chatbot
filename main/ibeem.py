import nltk
from nltk.chat.util import Chat, reflections

# Define pairs of patterns and responses
pairs = [
    (
        r"my name is (.*)",
        ("Hello %1, how can I help you today?",)
    ),
    (
        r"what is your name?",
        ("My name is IBeeM. I'm here to assist you.",)
    ),
    (
        r"how are you ?",
        ("I'm doing well, thank you!", "I'm doing fine, how can I assist you?",)
    ),
    (
        r"sorry (.*)",
        ("It's alright, no worries.", "No problem.",)
    ),
    (
        r"(.*) (good|great|fine)",
        ("That's wonderful to hear!", "Excellent!",)
    ),
    (
        r"(.*) (help|assist)",
        ("Sure, I can help you with that. What do you need assistance with?",)
    ),
    (
        r"quit",
        ("Goodbye! Have a great day.",)
    ),
    (
        r"what does IBM stand for ?",
        ("IBM stands for International Business Machines Corporation.",)
    ),
    (
        r"who founded IBM ?",
        ("IBM was founded by Charles Ranlett Flint in 1911.",)
    ),
    (
        r"where is IBM headquartered ?",
        ("IBM is headquartered in Armonk, New York, United States.",)
    ),
    (
        r"what year was IBM founded ?",
        ("IBM was founded in 1911.",)
    ),
    (
        r"what was the first product of IBM ?",
        ("The first product of IBM was a meat slicer, not computers as many people think.",)
    ),
    (
        r"what is IBM famous for ?",
        ("IBM is famous for its computer hardware, software, and services.",)
    ),
    (
        r"who was the first CEO of IBM ?",
        ("The first CEO of IBM was Thomas J. Watson.",)
    ),
    (
        r"what is the nickname of IBM ?",
        ("IBM is often referred to as 'Big Blue'.",)
    ),
    (
        r"what is the IBM Watson ?",
        ("IBM Watson is an artificial intelligence system capable of answering questions posed in natural language.",)
    ),
    (
        r"where was the first IBM headquarters located ?",
        ("The first IBM headquarters was located in Endicott, New York, United States.",)
    ),
    (
        r"what is the Deep Blue ?",
        ("Deep Blue was a chess-playing computer developed by IBM. It became the first computer to defeat a reigning world champion, Garry Kasparov, in a match under standard chess tournament time controls.",)
    ),
    (
        r"what is the IBM PC ?",
        ("The IBM PC, also known as the IBM Personal Computer, was introduced by IBM in 1981. It played a significant role in popularizing the use of personal computers.",)
    ),
    (
        r"what is IBM Research ?",
        ("IBM Research is the research and development division of IBM, which conducts scientific research in various fields, including computer science, artificial intelligence, and quantum computing.",)
    ),
    (
        r"who is the current CEO of IBM ?",
        ("As of my last update, Arvind Krishna is the CEO of IBM.",)
    ),
    (
        r"what is IBM's revenue ?",
        ("IBM's revenue varies year by year. You can check the latest financial reports for the most accurate information.",)
    ),
]

# Create a Chatbot instance
chatbot = Chat(pairs, reflections)

def chat():
    print("Hi! I'm IBeeM. How can I assist you today?")
    print("Type 'quit' to exit.")
    while True:
        user_input = input("You: ")
        response = chatbot.respond(user_input)
        print("IBeeM:", response)
        if user_input.lower() == 'quit':
            break

if __name__ == "__main__":
    chat()
