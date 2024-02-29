# MangoDB-Atlas-demo

## Introduction
- Use the mangodb project to store data in MangoDB as a data source. You need to initialize database configuration on your cloud data platform.
- Configure triggers on the cloud database platform to monitor database insertion data events, automatically generate embedding vectors and create indexes. You need to configure triggers and create indexes on your cloud data platform
- Use the vector_search project to obtain the vector of query parameters, and query the text corresponding to the most similar vector through Atalas's VectorSearch.

## Usage
1. Set environment variables:  
Create a new ".env" file following the example shown in ".env.example" and enter your own environment variables.  
The project requires the following environment variables to be input:
```env
mongodb_password=
openai_api_key=
```

2. Install and run the code:  
- Store Data
```
cd mangodb
pip3 install -r requirements.txt
python3 insert.py
```

- Vector Search
```
cd vector_search
npm install
npm run test
```
