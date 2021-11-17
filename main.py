from gfs_connection import db

from typing import Optional

from fastapi import FastAPI

app = FastAPI()

# sample queries


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}

# gigs

    # READ ALL


@app.get("/gigs")
def read_gigs():
    gigs_ref = db.collection('gigs')
    return {doc.id: doc.to_dict() for doc in gigs_ref.stream()}

    # READ ONE


@app.get("/gigs/{gig_id}")
def read_gig(gig_id: str):
    doc_ref = db.collection('gigs').document(gig_id)

    doc = doc_ref.get()
    if doc.exists:
        return {doc.id: doc.to_dict()}
    else:
        return {doc.id: 'No such document!'}


# companies


@app.get("/companies")
def read_companies():
    companies_ref = db.collection('companies')
    return {doc.id: doc.to_dict() for doc in companies_ref.stream()}

# pros


@app.get("/pros")
def read_pros():
    pros_ref = db.collection('pros')
    return {doc.id: doc.to_dict() for doc in pros_ref.stream()}
