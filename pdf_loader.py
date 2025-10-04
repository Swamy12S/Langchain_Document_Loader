from langchain_community.document_loaders import PyPDFLoader      # basically we are working on the document loader some of the steps are constant like this first-step and which loadr

                                                                     we are used ove there just mention the loader 

loader = PyPDFLoader('dl-curriculum.pdf')  


docs = loader.load()

print(docs)
print(len(docs))
print(docs[0].page_content)

print(docs[1].metadata)
