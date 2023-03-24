from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from routers import products
app = FastAPI()

app.include_router(products.router)

@app.get("/")
async def main():
    return RedirectResponse("/docs")