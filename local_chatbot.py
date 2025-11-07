# simple Local Chatbot with Text-to-Speech (pyttsx3)

import requests #for API requests
import pyttsx3 #for text-to-speech


# --------------------------- MEMORY --------------------------
# 'memory' stores the conversation history (both user and AI messages)
# 'max_memory' limits how many messages are kept to avoid overload
memory=[]
max_memory=10

# -------------------------- CHATBOT ---------------------------
def bot_query(prompt,model="llama3.2:3b"):

    # prepare the conversation history
    past_conv="\n".join(memory[-max_memory:])

    # complete prompt withpast conversation
    prompt=past_conv+"\n  USER :  "+prompt
    
    # API endpoint for your local LLaMA model
    url="http://localhost:11434/api/generate"

    # Data payload for the API request
    query={
        "prompt" : prompt,
        "model"  : model,
        "stream" : False # disable streaming responses
    }

    # send the POST request to the model server
    respond=requests.post(url,json=query)
    data=respond.json()

    # update memory with the latest interaction
    memory.append(prompt)
    memory.append("AI : "+data["response"])
    return data["response"]


# -------------------------- SPEECH ----------------------------
def speak(text):
    engine=pyttsx3.init() # initialize speech engine
    engine.setProperty('rate', 150) # adjust speech speed (150 words per minute)
    engine.say(text)
    engine.runAndWait()
    engine.stop()



# --------------------------- MAIN -----------------------------
if __name__=="__main__":
    print("\n----------------------------MY LOCAL CHATBOT----------------------------\n")
    
    while True:
        user_prompt=input("YOU : ")
        # exit condition
        if user_prompt.lower()=="exit":
            print("AI : take care ! \n")
            break
        else:
            # get the AI reply and speak it aloud
            ai_reply=bot_query(user_prompt)
            print("AI : ",ai_reply)
            speak(ai_reply)
            print("\n")