import weaviate
import os
from dotenv import load_dotenv

load_dotenv()

WEAVIATE_CLUSTER = os.getenv('WEAVIATE_CLUSTER')
WEAVIATE_KEY = os.getenv('WEAVIATE_KEY')

auth_config = weaviate.auth.AuthApiKey(api_key=WEAVIATE_KEY)  # API Key for the Weaviate instance

# Instantiate the client with the auth config
client = weaviate.Client(
    url=WEAVIATE_CLUSTER, 
    auth_client_secret=auth_config
)

print(client.schema.get())