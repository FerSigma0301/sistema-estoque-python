from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy import select
from sqlalchemy.orm import Session

from app.database import get_db
from app.models import Product, StockMovement
from app.schemas import MovementCreate, MovementResponse

router = APIRouter(prefix="/products", tags=["Stock"])


@router.post("/{product_id}/movements", response_model=MovementResponse, status_code=status.HTTP_201_CREATED)
def create_movement(
    product_id: int,
    movement_data: MovementCreate,
    db: Session = Depends(get_db),
) -> StockMovement:
    product = db.get(Product, product_id)
    if product is None:
        raise HTTPException(status_code=404, detail="Produto não encontrado")

    if movement_data.movement_type == "exit" and product.quantity < movement_data.quantity:
        raise HTTPException(status_code=400, detail="Estoque insuficiente")

    if movement_data.movement_type == "entry":
        product.quantity += movement_data.quantity
    else:
        product.quantity -= movement_data.quantity

    movement = StockMovement(product_id=product_id, **movement_data.model_dump())
    db.add(movement)
    db.commit()
    db.refresh(movement)
    return movement


@router.get("/{product_id}/movements", response_model=list[MovementResponse])
def list_movements(product_id: int, db: Session = Depends(get_db)) -> list[StockMovement]:
    if db.get(Product, product_id) is None:
        raise HTTPException(status_code=404, detail="Produto não encontrado")
    return list(
        db.scalars(
            select(StockMovement)
            .where(StockMovement.product_id == product_id)
            .order_by(StockMovement.id)
        ).all()
    )
