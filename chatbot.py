from langchain_community.llms import Ollama
from langchain.memory import ConversationBufferMemory
from langchain.chains import ConversationChain

llm = Ollama(model="phi3")

memory = ConversationBufferMemory()

conversation = ConversationChain(
    llm=llm,
    memory=memory
)

print("Chatbot with Memory (type exit to stop)\n")

while True:

    user_input = input("You: ")

    if user_input.lower() == "exit":
        break

    response = conversation.predict(input=user_input)

    print("Bot:", response)