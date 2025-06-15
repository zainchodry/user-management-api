from fastapi import FastAPI, status, HTTPException
from database import SessionLocal
import models 
from models import Person
from pydantic import BaseModel,EmailStr

app = FastAPI()
db = SessionLocal()


class OurBaseModel(BaseModel):
    class Config:
        orm_mode = True


class Person(OurBaseModel):
    id:int
    name:str
    email:EmailStr
    phone:int



@app.get('/', response_model=list[Person], status_code=status.HTTP_202_ACCEPTED)
def home():
    getperson = db.query(models.Person).all()
    return getperson



@app.post('/add-person', response_model=Person)
def add_person(person:Person):
    addperson = models.Person(
        id = person.id,
        name = person.name,
        email = person.email,
        phone = person.phone
    )

    filterperson = db.query(models.Person).filter(models.Person.email == person.email).first()
    if filterperson is not None:
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND, detail = "Person with this Email Already Exist")
    
    db.add(addperson)
    db.commit()

    return addperson



    
@app.put('/update-person/{person_id}', response_model=Person)
def update_person(person_id:int, person:Person):
    updateperson = db.query(models.Person).filter(models.Person.id == person_id).first()
    updateperson.id = person.id,
    updateperson.name = person.name,
    updateperson.email = person.email,
    updateperson.phone = person.phone

    db.commit()
    return updateperson



@app.delete('/delete-person/{person_id}', response_model = Person)
def delete_person(person_id:int):
    deleteperson = db.query(models.Person).filter(models.Person.id == person_id).first()

    if deleteperson is None:
        raise HTTPException(status_code = status.HTTP_400_BAD_REQUEST, detail = "Person with this id is not found")
    
    db.delete(deleteperson)
    db.commit()
    return deleteperson







