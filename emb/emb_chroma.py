import json

import chromadb
from chromadb.utils import embedding_functions

# config client
chroma_client = chromadb.Client()

# create collection
collection = chroma_client.create_collection(name="my_collection",
                                             metadata={"hnsw:space": "cosine"})


# add data to chroma db
def emb_add_documents(documents: list[str]):
    ids = ["id%s" % i for i in range(len(documents))]
    collection.add(
        ids=ids,
        documents=documents
    )


def emb_query(tex: list[str], result_num: int):
    try:
        results = collection.query(
            query_texts=tex,
            n_results=result_num
        )
    except Exception as e:
        return {"error": str(e)}

    return results


if __name__ == "__main__":
    docs = ["This is a document about engineer",
            "This is a document about steak",
            "This is a document about language"]
    query_texts = ["which food is the best"]

    emb_add_documents(docs)
    results = emb_query(tex=query_texts,
                        result_num=3)

    print(json.dumps(results, indent=4))
