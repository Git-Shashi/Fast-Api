from fastapi import FastAPI ,Path,HTTPException
import json

app = FastAPI()

def load_data():
    # Placeholder for data loading logic
    with open("patients.json", "r") as file:
        data = json.load(file)
    return data

@app.get("/")
def hello():
    return {"message": "Patients Management System"}

@app.get("/about")
def about():
    return {"message": "Fully functional patients management system built with FastAPI."}

@app.get("/view")
def view():
    return load_data()


@app.get("/view/{patientId}")
def view_patient(patientId: str=Path(..., description="The ID of the patient to retrieve")):
    data = load_data()
  
    if(patientId in data):
        return data[patientId]
    else:
        raise HTTPException(status_code=404, detail="Patient not found")