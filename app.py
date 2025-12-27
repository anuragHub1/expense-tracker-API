from fastapi import FastAPI

app=FastAPI(title="Expense tracker API")

@app.get("/")
def welcome():
    return {"message":"welcome"}