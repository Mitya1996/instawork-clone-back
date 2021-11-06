from gfs_connection import db

from typing import Optional

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}

# gigs


@app.get("/gigs")
def read_root():
    gigs_ref = db.collection('gigs')
    return {doc.id: doc.to_dict() for doc in gigs_ref.stream()}

# companies


@app.get("/companies")
def read_root():
    companies_ref = db.collection('companies')
    return {doc.id: doc.to_dict() for doc in companies_ref.stream()}

# pros


@app.get("/pros")
def read_root():
    pros_ref = db.collection('pros')
    return {doc.id: doc.to_dict() for doc in pros_ref.stream()}
