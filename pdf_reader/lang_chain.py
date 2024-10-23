#pip install -U langchain-community

from langchain_community.document_loaders.pdf import PyPDFDirectoryLoader

def load_documents():
    document_loader = PyPDFDirectoryLoader("./pdf_reader/data/islp_sample.pdf")
    return document_loader.load()


documents = load_documents()
print(documents)