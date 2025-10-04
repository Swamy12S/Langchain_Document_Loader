from langchain_community.document_loaders import TextLoader

from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser   # this is for generating the output as a summary from given poem 
from langchain_core.prompts import PromptTemplate

from dotenv import load_dotenv

load_dotenv()

model = ChatOpenAI()

prompt = PromptTemplate(
    template  = 'write the summary for the following poem -\n {poem}',
    input_variables = ['poem']

)

loader = TextLoader('cricket.txt', encoding = 'utf-8')


docs = loader.load()

print(type(docs))

print(len(docs))

print(docs[0])   #extracting first document
print(type(docs[0]))  #type of first document

print(docs[0].page_content)  #content of first document
print(docs[0].metadata)  #metadata of first document

chain = prompt | model | Parser

result = chain.invoke({'poem':docs[0].page_content})

print(result)