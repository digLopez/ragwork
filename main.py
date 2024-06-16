import json

from fastapi import FastAPI
from pydantic import BaseModel

from utils import file_loader, file_split
from emb import emb_chroma
from llm.gpt4 import ask_llm

app = FastAPI()


class Query(BaseModel):
    question: str = None


# file import and split
documents = []
file_list = file_loader.get_file_list()
for filepath in file_list:
    file = file_loader.read_file(filepath)
    documents.extend(file_split.r_splitter.split_text(file))

# embedding
emb_chroma.emb_add_documents(documents)


@app.post("/query/")
def post_items(query: Query):
    results = emb_chroma.emb_query([query.question], 10)
    chunks = results["documents"]
    answer = ask_llm(chunks, query.question[0])
    return {"answer": answer}


if __name__ == '__main__':
    query = Query()
    query.question = ["汽车的轴距是什么意思"]
    results = emb_chroma.emb_query(query.question, 30)
    print(json.dumps(results, indent=4, ensure_ascii=False))
    chunks = results["documents"][0]
    answer = ask_llm(chunks, query.question[0])
    print({"answer": answer})
