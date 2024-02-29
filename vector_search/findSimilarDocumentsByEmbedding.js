require("dotenv").config();
const axios = require("axios");
const MongoClient = require("mongodb").MongoClient;

async function getEmbedding(query) {
    // Define the OpenAI API url and key.
    const url = "https://api.openai.com/v1/embeddings";
    const openai_api_key = process.env.openai_api_key; // Replace with your OpenAI key.
    // Call OpenAI API to get the embeddings.
    try {
        let response = await axios.post(
            url,
            {
                input: query,
                model: "text-embedding-ada-002",
            },
            {
                headers: {
                    Authorization: `Bearer ${openai_api_key}`,
                    "Content-Type": "application/json",
                },
            }
        );

        if (response.status === 200) {
            return response.data.data[0].embedding;
        } else {
            throw new Error(`Failed to get embedding. Status code: ${response.status}`);
        }
    } catch (error) {
        throw error?.response?.data ?? error.message;
    }
}

async function findSimilarDocuments(embedding) {
    const url = `mongodb+srv://rpmckg:${process.env.mongodb_password}@cluster0.nixga4w.mongodb.net/?retryWrites=true&w=majority`;
    const client = new MongoClient(url);

    try {
        await client.connect();

        const db = client.db("sample_mflix"); // Replace with your database name.
        const collection = db.collection("movies"); // Replace with your collection name.

        // const cursor = collection.find();

        // for await (const doc of cursor) {
        //     console.log(doc);
        // }

        // Query for similar documents.
        const documents = collection.aggregate([
            {
                $vectorSearch: {
                    queryVector: embedding,
                    path: "plot_embedding",
                    numCandidates: 10,
                    limit: 2,
                    index: "vector_index",
                },
            },
        ]);

        for await (const doc of documents) {
            console.log(doc);
        }
        return documents;
    } finally {
        await client.close();
    }
}

async function main() {
    const query = "say hello to world"; // Replace with your query.

    try {
        const embedding = await getEmbedding(query);
        await findSimilarDocuments(embedding);
    } catch (err) {
        console.error(err);
    }
}

main();
