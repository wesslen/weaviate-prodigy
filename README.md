# weaviate-prodigy

A/B evaluation with Prodigy with weaviate vector database

To install, first create `PRODIGY_KEY` in `.env` file.

Create a new virtual environment:

```
python -m venv venv
source venv/bin/activate
```

Then run `make install` to install libraries.

# Weaviate

1. Create a [cloud instance](https://weaviate.io/developers/wcs/quickstart)
2. Add cloud URL (`WEAVIATE_CLUSTER`) and Auth token (`WEAVIATE_TOKEN`) to .env file. Can create manuallly or programmatically:

```
dotenv set WEAVIATE_CLUSTER https://my-sandbox-cluster-xxxxxx.weaviate.network
dotenv set WEAVIATE_KEY xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
```
3. Create [schema and upload data to cloud instance](https://weaviate.io/developers/weaviate/tutorials/schema)

