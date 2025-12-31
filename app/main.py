from fastapi import FastAPI
from pydantic import BaseModel

from data_interactor import DataInteractor

app = FastAPI()
data_interactor = DataInteractor()

class Contact(BaseModel):
    first_name: str
    last_name: str
    phone_number: str

@app.get("/contacts")
def get_contacts():
    contacts = data_interactor.get_all_contacts()
    return contacts

@app.post("/contacts")
def create_contact(contact: Contact):
    contact_data = contact.dict()
    contact_id = data_interactor.create_contact(contact_data)
    return {"message": "Contact created successfully", "id": contact_id}

@app.put("/contacts/{id}")
def update_contact(id: str, contact: Contact):
    contact_data = contact.dict()
    success = data_interactor.update_contact(id, contact_data)
    if success:
        return {"message": "Contact updated successfully"}
    else:
        return {"message": "Contact not found"}
    
@app.delete("/contacts/{id}")
def delete_contact(id: str):
    success = data_interactor.delete_contact(id)
    if success:
        return {"message": "Contact deleted successfully"}
    else:
        return {"message": "Contact not found"}

@app.get("/health/db")
def check_db():
    if data_interactor.check_db():
        return {"mongo": "connected"}
    else:
        return {"mongo": "not connected"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)



