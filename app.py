from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"email": "23f1001792@ds.study.iitm.ac.in", "message": "Hello from Codespaces!"}
