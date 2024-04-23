from fastapi import FastAPI, Path


app = FastAPI() # object of FastAPI class


classes = {
    1 :{
        "name": "Data Science",
        "teacher": "Mr. A"
    },
    2:{
        "name": "Machine Learning",
        "teacher": "Mr. B"
    },
    3:{
        "name": "Maths",
        "teacher": "Mr. C"
    }
}



#creating endpoint
@app.get("/")
def index():
    return {"data": "data goes here"}

@app.get("/get-class/{class_id}")
def get_class(class_id: int = Path(..., description="The ID of the class you want to view", gt=0, lt=3)):
    return classes[class_id]

@app.get("/get-by-name")
def get_class(name: str ):
    for class_id in classes:
        if classes[class_id]["name"] == name:
            return classes[class_id]
    return {"Data": "Not Found"}

@app.get("/get-by-name/{name}")
def get_class(name: str=Path(...,description="enter class name") ):
    for class_id in classes:
        if classes[class_id]["name"] == name:
            return classes[class_id]
    return {"Data": "Not Found"}