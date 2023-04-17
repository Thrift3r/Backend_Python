from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from routers import products
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()

# Configuración de CORS
origins = [
    "http://localhost",
    "http://localhost:3000",
]

app.include_router(products.router)


app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def main():
    return RedirectResponse("/docs")