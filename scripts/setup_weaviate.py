import weaviate
import os
import json
import requests
import srsly
from dotenv import load_dotenv

load_dotenv()

WEAVIATE_CLUSTER = os.getenv('WEAVIATE_CLUSTER')
WEAVIATE_KEY = os.getenv('WEAVIATE_KEY')
OPENAI_KEY = os.getenv('OPENAI_KEY')

auth_config = weaviate.auth.AuthApiKey(api_key=WEAVIATE_KEY)  # API Key for the Weaviate instance

# Instantiate the client with the auth config
client = weaviate.Client(
    url=WEAVIATE_CLUSTER, 
    auth_client_secret=auth_config,
    timeout_config=(5, 15),  # (Optional) Set connection timeout & read timeout time in seconds
    additional_headers={  # (Optional) Any additional headers; e.g. keys for API inference services
        "X-OpenAI-Api-Key": OPENAI_KEY,
    }
)

# we will create the class "Sentences"
class_obj = {
    "class": "Sentences",
    "description": "Sentences for similarity comparison",  # description of the class
    "properties": [
        {
            "dataType": ["text"],
            "description": "The sentence",
            "name": "text",
        },
    ],
    "vectorizer": "text2vec-openai",
    "moduleConfig": {
      "text2vec-openai": {
        "model": "ada",
        "modelVersion": "002",
        "type": "text"
      }
    }
}

# add the schema
client.schema.create_class(class_obj)

# get the schema
schema = client.schema.get()

# print the schema
print(json.dumps(schema, indent=4))

data = srsly.read_jsonl("data/sick-input.jsonl")

# Prepare a batch process
with client.batch as batch:
    batch.batch_size=100
    # Batch import all Questions
    for i, d in enumerate(data):
        print(f"importing sentences: {i+1}")  # To see imports

        properties = {
            "text": d["text"],
        }

        client.batch.add_data_object(properties, "Sentences")
