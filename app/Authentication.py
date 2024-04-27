from fastapi import FastAPI

app = FastAPI()

@app.get("/healdcheck")
async def healthcheck() -> dict[str, str]
    return {"status":"ok"}