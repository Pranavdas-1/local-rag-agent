from langchain_ollama.llms import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate
from vector import retriver

model = OllamaLLM(model = 'llama3.2')

template = '''
You are an expert in answering questions about a pizza restaurant.

Here are some relevant reviews: {review}

Here is the question to answer: {question}

Answer based only on the reviews above. If the reviews don't contain 
enough information, say "I don't have enough information to answer that."
'''

prompt = ChatPromptTemplate.from_template(template)
chain = prompt | model

while True:
    print("\n\n-----------------------------------------")
    question = input("Ask your question (q to quit):    ")
    print("\n\n")
    
    if question == "q":
        break
    review = retriver.invoke(question)
    result = chain.invoke({"review":review,"question": question})
    print(result)