from fastapi import FastAPI
from app.config.database import Base, engine
from app.routes import routes

Base.metadata.create_all(bind=engine)

app = FastAPI(title="PPE Detection Service")

for route in routes:
    app.include_router(route)
