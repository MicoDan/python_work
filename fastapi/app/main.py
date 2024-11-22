import uvicorn
from fastapi import FastAPI
app = FastAPI()
from server.routes.student import router as student_router




app.include_router(student_router, prefix="/students", tags=["Students"])

@app.get("/")
def read_root():
    return {"message": "Hello, FastAPI!"}

if __name__ == "__main__":
    uvicorn.run("server.app:app", host="0.0.0.0", port=8000, reload=True)