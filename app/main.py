from fastapi import FastAPI

from app.database import Base, engine
from app.routes.movements import router as movements_router
from app.routes.products import router as products_router

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Sistema de Estoque",
    version="1.0.0",
    description="API REST para controle de produtos e movimentações de estoque.",
)

app.include_router(products_router)
app.include_router(movements_router)


@app.get("/", tags=["Health"])
def root() -> dict[str, str]:
    return {"message": "Sistema de Estoque online"}


@app.get("/health", tags=["Health"])
def health_check() -> dict[str, str]:
    return {"status": "ok"}
