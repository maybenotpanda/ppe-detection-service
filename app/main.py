from fastapi import FastAPI, Request, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse
from fastapi.staticfiles import StaticFiles
import os

from app.config.database import Base, engine
from app.routes import routes

Base.metadata.create_all(bind=engine)

app = FastAPI(title="PPE Detection Service")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.middleware("http")
async def log_requests(request: Request, call_next):
    print(f"[REQUEST] {request.method} {request.url}")
    response = await call_next(request)
    print(f"[RESPONSE] {response.status_code}")
    return response

@app.exception_handler(HTTPException)
async def http_exception_handler(request, exc):
    return JSONResponse(
        status_code=exc.status_code,
        content={"success": False, "message": exc.detail},
    )

@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request, exc):
    return JSONResponse(
        status_code=422,
        content={
            "success": False,
            "message": "Invalid input",
            "errors": exc.errors(),
        },
    )

@app.exception_handler(Exception)
async def global_exception_handler(request, exc: Exception):
    return JSONResponse(
        status_code=500,
        content={
            "success": False,
            "message": "Internal server error",
            "detail": str(exc),
        },
    )

RESULT_FOLDER = os.path.join(os.getcwd(), "results")
UPLOAD_FOLDER = os.path.join(os.getcwd(), "uploads")

os.makedirs(RESULT_FOLDER, exist_ok=True)
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

app.mount("/results", StaticFiles(directory=RESULT_FOLDER), name="results")
app.mount("/uploads", StaticFiles(directory=UPLOAD_FOLDER), name="uploads")

for route in routes:
    app.include_router(route)
