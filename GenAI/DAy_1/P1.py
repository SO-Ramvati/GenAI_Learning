#Type Hints
Temp: float = 0.7
max_tok: int = 1024
isstream: bool = False
cont_bx: str|None = None
model_name: str ="Gemini_Flash"
print(type(model_name))

#Old style str fromatting
name="LLM"
print("Hello %s"%name)
sc=78.8
print("Score = %.1f"%sc)

word_limit=200
print(f"{'Over' if word_limit>150 else 'under'}limit")
data={"topic":"RAG"}
print(f"Topic: {data['topic']}")

pi=3.14159265
print(f"pi:{pi:.2f}")

#Debugging
temp=0.7
print(f"{temp=}")

#Multi line f-strings
user_in="What is LangChain?"
context_text="LangChain is a framework for building LLM apps"
system_prompt=f"""
You are a helpful AI tutor.
Context provided: {context_text}
student question: {user_in}
Instructions
-Answer based only on the context above
-If the answer is not in the context, say "I don't know"
-Keep the answer under 3 sentences
""".strip()
print(system_prompt)

#Lists: ordered, mutable, heterogenous sequence
#In GenAI: chat history, chunks of the retreived documents
#Token sequences
chat_history:list[dict]=[
    {"role":"user","content":"What is an LLM"},
    {"role":"assistant","content":"An LLM is a neural trained on vast amounts of texts."}
]
#Access
first_msg=chat_history[0]
print(first_msg)
print(chat_history[-1]["content"])

#Modify
chat_history.append({"role":"user","content":"What is a RAG"})
chat_history.pop(0)
print(chat_history)

#Iterate
for msg in chat_history:
    print(f"{msg["role"].upper()}:{msg["content"].upper()}")

#List of document chunks
chunks:list[str]=[
    "RAG stands for Retreival Augmented Generation",
    "It combines a retreiver with a generator",
]
#Filter chunks based on length
valid_chunk=[c for c in chunks if len(c.split())>=6]
print(valid_chunk)