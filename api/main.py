from fastapi import FastAPI
from api.routes import router as source_router
from api.routes_target import router as target_router

app = FastAPI(title="ETL API")

# Inclui os endpoints que acessam o banco fonte (/data)
app.include_router(source_router)

# Inclui o endpoint que acessa o banco alvo (/signal)
app.include_router(target_router)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("api.main:app", host="0.0.0.0", port=8000, reload=True)
