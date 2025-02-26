from fastapi import FastAPI  # type: ignore
from Routes.route import authRouter


app = FastAPI()


@app.get("/")
def read_root():
    return {"message": "server is running"}


app.include_router(authRouter, prefix="/reg", tags=["Routes"])
