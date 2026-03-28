from langchain_community.document_loaders import PyPDFLoader
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS

# Loading Documents
loader = PyPDFLoader("./attention.pdf")
documents = loader.load()

# Splitting Documents
text_splitter = RecursiveCharacterTextSplitter(chunk_size=800,chunk_overlap=100)
chunks = text_splitter.split_documents(documents)

# Embeddings
emb = HuggingFaceEmbeddings(model_name="intfloat/e5-small-v2")

# Storing Vector DB
db = FAISS.from_documents(chunks,emb)

# Retrieving
query = "What is the attention mechanism"
retriever = db.similarity_search(query)
print("\nAnswer:",retriever[0].page_content)

