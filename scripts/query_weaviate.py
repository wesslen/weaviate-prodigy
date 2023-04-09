import weaviate
import json
import os
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

examples = srsly.read_jsonl("data/sick-test.jsonl")
choice = 5

top_choice = []
bottom_choice = []

for int, eg in enumerate(examples):

    if int % 10 == 0:
        print(int)

    nearText = {"concepts": [eg["text"]]}

    result = (
        client.query
        .get("Sentences", ["text"])
        .with_near_text(nearText)
        .with_limit(choice)
        .do()
    )

    top_choice.append({"id": int, "input": {"text": eg["text"]}, "output": {"text": result["data"]["Get"]["Sentences"][0]["text"]}})
    bottom_choice.append({"id": int, "input": {"text": eg["text"]}, "output": {"text": result["data"]["Get"]["Sentences"][choice - 1]["text"]}})

srsly.write_jsonl("data/choice_top.jsonl", top_choice)
srsly.write_jsonl("data/choice_bottom.jsonl", bottom_choice)