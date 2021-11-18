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


@app.get("/")
def read_root():
    return {"Message": "Hello and welcome to Instawork Clone Backend. Please see /docs route to interact with the API"}

# gigs #################################################

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

    # CREATE


@app.post("/gigs/", tags=["gigs"])
async def create_gig(gig: Gig):
    db.collection('gigs').document().set(gig.dict())

    return {'message': 'doc added successfully!'}

    # UPDATE


@app.put("/gigs/{gig_id}", tags=["gigs"])
async def update_gig(gig_id: str, gig: Gig):
    doc_ref = db.collection('gigs').document(gig_id)

    doc = doc_ref.get()
    if doc.exists:
        doc_ref.set(gig.dict())
        return {'message': 'doc updated successfully!', gig_id: gig}
    else:
        return {doc.id: 'No such document!'}

    # DELETE


@app.delete("/gigs/{gig_id}", tags=["gigs"])
async def delete_gig(gig_id: str):
    doc_ref = db.collection('gigs').document(gig_id)
    doc = doc_ref.get()
    if doc.exists:
        doc_ref.delete()
        return {'message': 'doc deleted successfully!', gig_id: None}
    else:
        return {doc.id: 'No such document!'}


# companies ################################################

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

    # CREATE


@app.post("/companies/", tags=["companies"])
async def create_company(company: Company):
    db.collection('companies').document().set(company.dict())

    return {'message': 'doc added successfully!'}

    # UPDATE


@app.put("/companies/{company_id}", tags=["companies"])
async def update_company(company_id: str, company: Company):
    doc_ref = db.collection('companies').document(company_id)

    doc = doc_ref.get()
    if doc.exists:
        doc_ref.set(company.dict())
        return {'message': 'doc updated successfully!', company_id: company}
    else:
        return {doc.id: 'No such document!'}

    # DELETE


@app.delete("/companies/{company_id}", tags=["companies"])
async def delete_company(company_id: str):
    doc_ref = db.collection('companies').document(company_id)
    doc = doc_ref.get()
    if doc.exists:
        doc_ref.delete()
        return {'message': 'doc deleted successfully!', company_id: None}
    else:
        return {doc.id: 'No such document!'}


# pros ###############################################################

    # READ ALL
@app.get("/pros", tags=["pros"])
def read_all_pros():
    pros_ref = db.collection('pros')
    return {doc.id: doc.to_dict() for doc in pros_ref.stream()}

    # READ ONE


@app.get("/pros/{pro_id}", tags=["pros"])
def read_pro(pro_id: str):
    doc_ref = db.collection('pros').document(pro_id)

    doc = doc_ref.get()
    if doc.exists:
        return {doc.id: doc.to_dict()}
    else:
        return {doc.id: 'No such document!'}

    # CREATE


@app.post("/pros/", tags=["pros"])
async def create_pro(pro: Pro):
    db.collection('pros').document().set(pro.dict())

    return {'message': 'doc added successfully!'}

    # UPDATE


@app.put("/pros/{pro_id}", tags=["pros"])
async def update_pro(pro_id: str, pro: Pro):
    doc_ref = db.collection('pros').document(pro_id)

    doc = doc_ref.get()
    if doc.exists:
        doc_ref.set(pro.dict())
        return {'message': 'doc updated successfully!', pro_id: pro}
    else:
        return {doc.id: 'No such document!'}

    # DELETE


@app.delete("/pros/{pro_id}", tags=["pros"])
async def delete_pro(pro_id: str):
    doc_ref = db.collection('pros').document(pro_id)
    doc = doc_ref.get()
    if doc.exists:
        doc_ref.delete()
        return {'message': 'doc deleted successfully!', pro_id: None}
    else:
        return {doc.id: 'No such document!'}
