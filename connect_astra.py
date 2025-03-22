from astrapy import DataAPIClient

# ✅ Your actual AstraDB Token
ASTRA_DB_TOKEN = "AstraCS:odGkGHnXaGdeInHrteXtlbAw:807c6524cfddaf5429aedcfd6b3cddae23602bae05c474d5b938bc554dbbfe23"

# ✅ Your actual API Endpoint
ASTRA_DB_ENDPOINT = "https://3daece68-bb33-4ca9-8426-5d32efc4fad9-us-east-2.apps.astra.datastax.com"

# Initialize Astra Client
client = DataAPIClient(ASTRA_DB_TOKEN)
db = client.get_database_by_api_endpoint(ASTRA_DB_ENDPOINT)

# Print all collections in this database
print("📂 Collections in your AstraDB:", db.list_collection_names())

