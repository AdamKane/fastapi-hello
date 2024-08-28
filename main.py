from fastapi import FastAPI, HTTPException, Depends
from simple_salesforce import Salesforce
from salesforce import (
    create_salesforce_connection, get_account_names, get_contacts_for_account,
    get_opportunities_for_account, get_all_opportunity_names, get_proposal_due_opportunities,
    get_lead_count
)

app = FastAPI()

def get_sf_connection():
    sf = create_salesforce_connection()
    if not sf:
        raise HTTPException(status_code=500, detail="Failed to connect to Salesforce")
    return sf

@app.get("/")
async def root():
    return {"message": "Hello World!!"}

@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}

@app.get("/accounts")
async def list_accounts(sf: Salesforce = Depends(get_sf_connection)):
    try:
        return get_account_names(sf)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/contacts/{account_id}")
async def list_contacts(account_id: str, sf: Salesforce = Depends(get_sf_connection)):
    try:
        return get_contacts_for_account(sf, account_id)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/opportunities/{account_id}")
async def list_opportunities(account_id: str, sf: Salesforce = Depends(get_sf_connection)):
    try:
        return get_opportunities_for_account(sf, account_id)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/opportunities")
async def list_all_opportunities(sf: Salesforce = Depends(get_sf_connection)):
    try:
        return get_all_opportunity_names(sf)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/opportunities/proposal-due")
async def list_proposal_due_opportunities(sf: Salesforce = Depends(get_sf_connection)):
    try:
        return get_proposal_due_opportunities(sf)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/leads/count")
async def count_leads(sf: Salesforce = Depends(get_sf_connection)):
    try:
        return {"total_leads": get_lead_count(sf)}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
