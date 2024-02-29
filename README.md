# mangodb-atlas-demo

## Introduction
Use the mangodb project to store data in MangoDB as a data source, configure triggers on the cloud database platform to monitor database insertion data events, automatically generate embedding vectors and create indexes. Use the vector_search project to obtain the vector of query parameters, and query the text corresponding to the most similar vector through Atalas's VectorSearch.

## Usage
### Store Data
```
cd mangodb
pip3 install -r requirements.txt
python3 insert.py
```

### Vector search
```
cd vector_search
npm install
npm run test
```
