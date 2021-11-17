from gfs_connection import db
from models import Gig, Company, Pro

from typing import Optional

from fastapi import FastAPI

description = """
Instawork Clone is a clone of the Instawork app that allows anyone quickly and easily find high paying gigs in their area! 🚀

## Gigs

You can **create, read, update, and delete gigs**.

## Companies

You can **create, read, update, and delete companies**.

## Pros

You can **create, read, update, and delete pros**.

"""

app = FastAPI(title="Instawork Clone Backend", description=description)

# sample queries


@app.get("/")
def read_root():
    return {"Message": "Hello and welcome to Instawork Clone Backend"}


# @app.get("/items/{item_id}")
# def read_item(item_id: int, q: Optional[str] = None):
#     return {"item_id": item_id, "q": q}

# gigs

    # READ ALL


@app.get("/gigs", tags=["gigs"])
def read_all_gigs():
    gigs_ref = db.collection('gigs')
    return {doc.id: doc.to_dict() for doc in gigs_ref.stream()}

    # READ ONE


@app.get("/gigs/{gig_id}", tags=["gigs"])
def read_gig(gig_id: str):
    doc_ref = db.collection('gigs').document(gig_id)

    doc = doc_ref.get()
    if doc.exists:
        return {doc.id: doc.to_dict()}
    else:
        return {doc.id: 'No such document!'}

    # CREATE ONE


@app.post("/gigs/", tags=["gigs"])
async def create_gig(gig: Gig):
    db.collection('gigs').document().set(gig.dict())

    return {'message': 'doc added successfully!'}


# companies

    # READ ALL
@app.get("/companies", tags=["companies"])
def read_all_companies():
    companies_ref = db.collection('companies')
    return {doc.id: doc.to_dict() for doc in companies_ref.stream()}

    # READ ONE


@app.get("/companies/{company_id}", tags=["companies"])
def read_company(company_id: str):
    doc_ref = db.collection('companies').document(company_id)

    doc = doc_ref.get()
    if doc.exists:
        return {doc.id: doc.to_dict()}
    else:
        return {doc.id: 'No such document!'}

    # CREATE ONE


@app.post("/companies/", tags=["companies"])
async def create_company(company: Company):
    db.collection('companies').document().set(company.dict())

    return {'message': 'doc added successfully!'}


# pros

    # READ ALL
@app.get("/pros", tags=["pros"])
def read_all_pros():
    pros_ref = db.collection('pros')
    return {doc.id: doc.to_dict() for doc in pros_ref.stream()}

    # READ ONE


@app.get("/pros/{pro_id}", tags=["pros"])
def read_company(pro_id: str):
    doc_ref = db.collection('pros').document(pro_id)

    doc = doc_ref.get()
    if doc.exists:
        return {doc.id: doc.to_dict()}
    else:
        return {doc.id: 'No such document!'}

    # CREATE ONE


@app.post("/pros/", tags=["pros"])
async def create_pro(pro: Pro):
    db.collection('pros').document().set(pro.dict())

    return {'message': 'doc added successfully!'}
