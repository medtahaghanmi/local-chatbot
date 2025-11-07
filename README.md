# 🤖 My Local Chatbot (with Text-to-Speech)

This is a super simple **local chatbot** that talks using your own locally hosted **LLaMA model**, and can **speak** its replies out loud with `pyttsx3`.  
It remembers recent chats, sounds natural, and works completely **offline** once your model is running!

---

## ✨ What It Does

- 💬 Remembers your last few messages (so it feels like a real chat)
- 🗣️ Talks back using your computer’s voice (thanks to `pyttsx3`)
- ⚡ Works with **Ollama** and local LLaMA models
- 💻 100% local — no cloud, no API keys, just Python
- 🔧 Easy to tweak and customize

---

## 🧰 What You’ll Need

- Python **3.8+**
- [`requests`](https://pypi.org/project/requests/) and [`pyttsx3`](https://pypi.org/project/pyttsx3/)
- A local AI model running with [**Ollama**](https://ollama.ai/)

Install dependencies:
```bash
pip install requests pyttsx3
```

---

## 🚀 How to Run It

1. **Start your local model** (for example with Ollama):
   ```bash
   ollama run llama3.2:3b
   ```
   This script will connect to:
   ```
   http://localhost:11434/api/generate
   ```

2. **Run the chatbot:**
   ```bash
   python chatbot.py
   ```

3. **Chat with it!**
   ```
   ----------------------------WELCOME TO MY CHATBOT----------------------------
   YOU : hey there
   AI  : Hey! How’s it going?
   ```

4. Type `exit` anytime to quit:
   ```
   YOU : exit
   AI  : take care !
   ```



---

## 🧩 A Quick Look at the Code

- **Memory:** keeps up to 10 recent messages  
- **bot_query():** sends your prompt to the local model  
- **speak():** makes your computer read the reply out loud  

Everything’s short, readable, and easy to edit!

---



## 🔧 Custom Stuff You Can Change

- Try different models:
  ```python
  bot_query(prompt, model="mistral:7b")
  ```
- Change the speaking speed:
  ```python
  engine.setProperty('rate', 150)
  ```
- Or make it remember more messages:
  ```python
  max_memory = 20
  ```

---

## 👤 Made by

**Mohamed Taha Ghanmi**

---
