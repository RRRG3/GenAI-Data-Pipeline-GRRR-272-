import csv
from langchain.vectorstores.cassandra import Cassandra
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.schema import Document
from astrapy.db import AstraDB

# Connect to AstraDB
db = AstraDB(
    token="AstraCS:odGkGHnXaGdeInHrteXtlbAw:807c6524cfddaf5429aedcfd6b3cddae23602bae05c474d5b938bc554dbbfe23",
    api_endpoint="https://3daece68-bb33-4ca9-8426-5d32efc4fad9-us-east-2.apps.astra.datastax.com"
)

# Load data from CSV
docs = []
with open("faq_bulk_150_records.csv", newline='', encoding='utf-8') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        text = f"Q: {row['question']} A: {row['answer']}"
        docs.append(Document(page_content=text))

# Initialize embedding model
embedding = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

# Store in AstraDB vector store
vectorstore = Cassandra(
    embedding=embedding,
    session=db.get_session(),
    keyspace="genai_keyspace",       # Replace with your keyspace if different
    table_name="faq_embeddings"      # Table will be created if not exists
)

# Add documents
vectorstore.add_documents(docs)

print("✅ Data successfully ingested into AstraDB!")

