from chatterbot import ChatBot
from chatterbot.conversation import Statement
from chatterbot.trainers import ChatterBotCorpusTrainer  # ChatterBotCorpusTrainer is a collection of words or sentences

chatBot = ChatBot('ChatBOt')
trainer = ChatterBotCorpusTrainer(chatBot)

trainer.train("chatterbot.corpus.english") #you can train ur chatbot only on one aspect to food or greeting trainer.train("chatterbot.corpus.english.greetings")

print("Hi, I am ChatBot")

while True:
    query = input(">>>>")
    print(chatBot.get_response(Statement(text=query, search_text=query)))