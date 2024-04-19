from fastapi import FastAPI


app = FastAPI() # object of FastAPI class

#creating endpoint
@app.get("/")
def index():
    return {"data": "data goes here"}