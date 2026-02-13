from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from db import get_db,DATABASE_URL
from sqlalchemy import create_engine
from models import Base
import os
app = FastAPI()

#cors
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Create database tables if they don't exist
engine = create_engine(DATABASE_URL)

@app.get("/")
def read_root():
    return {"Hello": "World"}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000, reload=True)