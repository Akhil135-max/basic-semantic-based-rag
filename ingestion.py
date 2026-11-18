from langchain_community.document_loaders import PyMuPDFLoader

def pdf_loader(pdf_path):
    loader = PyMuPDFLoader(pdf_path)
    docs = loader.load()
    return docs

