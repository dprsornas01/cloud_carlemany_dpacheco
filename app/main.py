from fastapi import FastAPI

app = FastAPI()

@app.get("/healthcheck")
async def healthcheck() -> dict[str, str]:
    return {"status": "ok"}

@app.post("/test/{id}")
async def test(id: int) -> dict[str, str]:
        return {"test": id}