from langchain_community.document_loaders import DirectoryLoader, PyPDFLoader

loader = DirectoryLoader(
    path='books',
    glob='*.pdf',
    loader_cls=PyPDFLoader        #Start faster, Save memory,Handle large datasets efficiently thats the reson using directory loader insted of lazy loader 
)

docs = loader.lazy_load()

for document in docs:
    print(document.metadata)