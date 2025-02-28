from fastapi import FastAPI  # type: ignore
from .routes import authRouter
# from .errors import app

from fastapi import FastAPI # type: ignore
from fastapi.responses import JSONResponse # type: ignore
from fastapi.exceptions import RequestValidationError # type: ignore
from fastapi import Request # type: ignore


app = FastAPI()


@app.get("/")
def read_root():
    return {"message": "server is running"}


@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request: Request, exc: RequestValidationError):
    errors = []
    for error in exc.errors():
        errors.append({
            "field": ".".join(map(str, error["loc"])),  # Converts tuple path to a string
            "message": error["msg"]
        })
    
    return JSONResponse(
        status_code=400,
        content={
            "status": "error",
            "message": "Validation failed",
            "errors": errors
        }
    )



app.include_router(authRouter, prefix="/reg", tags=["Routes"])
