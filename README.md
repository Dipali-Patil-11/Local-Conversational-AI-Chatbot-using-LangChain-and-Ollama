# Local-Conversational-AI-Chatbot-using-LangChain-and-Ollama
# 🤖 AEAI Local Chatbot (LangChain + Ollama)

A simple **AI chatbot with memory** built using **LangChain and Ollama**, running completely **locally without API keys**.

This project demonstrates how to integrate **local LLMs with Python** for conversational AI applications.

---

# 📌 Project Overview

This chatbot uses:

* **LangChain** – for conversational chains
* **Ollama** – to run local AI models
* **Phi-3 model** – Microsoft's lightweight LLM
* **Conversation Memory** – remembers previous messages

The chatbot runs in the **terminal** and maintains conversation history.

---

# 🛠 Technologies Used

* Python 3.10
* LangChain
* LangChain Community
* Ollama
* Phi-3 Model
* Virtual Environment (venv)

---

# 📂 Project Structure

AEAI_Project_3

chatbot.py

venv/

README.md

---

# ⚙️ Installation Guide

Follow these steps to run the project.

---

# Step 1: Install Python

Download Python:

https://www.python.org/downloads/

Verify installation:

```bash
python --version
```

---

# Step 2: Install Ollama

Download Ollama:

https://ollama.com/download

Verify installation:

```bash
ollama --version
```

---

# Step 3: Pull AI Model

Download the Phi-3 model:

```bash
ollama pull phi3
```

Check installed models:

```bash
ollama list
```

---

# Step 4: Create Virtual Environment

Navigate to project folder:

```bash
cd AEAI_Project_3
```

Create virtual environment:

```bash
python -m venv venv
```

Activate environment:

Windows:

```bash
venv\Scripts\activate
```

---

# Step 5: Install Required Libraries

```bash
pip install langchain
pip install langchain-community
pip install ollama
```

---

# Step 6: Run the Chatbot

Run:

```bash
python chatbot.py
```

Example interaction:

```
Chatbot with Memory (type exit to stop)

You: Hello
Bot: Hello! How can I assist you today?
```

---

# 🧠 Chatbot Code

```python
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

    response = conversation.run(user_input)

    print("Bot:", response)
```

---

# 🚀 Features

✔ Local AI (No API Key)
✔ Conversation Memory
✔ LangChain Integration
✔ Ollama LLM Support
✔ Simple Terminal Chatbot

---

# 📈 Future Improvements

* GUI chatbot using **Streamlit**
* PDF knowledge chatbot
* Web interface
* Voice chatbot
* Multi-model support

---

# 👩‍💻 Author

Dipali Patil

AIML Engineering Student 

---
