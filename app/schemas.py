from datetime import datetime

from pydantic import BaseModel, ConfigDict, Field


class ProductBase(BaseModel):
    name: str = Field(min_length=1, max_length=120)
    sku: str = Field(min_length=1, max_length=50)
    category: str | None = Field(default=None, max_length=80)
    price: float = Field(ge=0)
    minimum_stock: int = Field(default=0, ge=0)


class ProductCreate(ProductBase):
    quantity: int = Field(default=0, ge=0)


class ProductUpdate(BaseModel):
    name: str | None = Field(default=None, min_length=1, max_length=120)
    sku: str | None = Field(default=None, min_length=1, max_length=50)
    category: str | None = Field(default=None, max_length=80)
    price: float | None = Field(default=None, ge=0)
    minimum_stock: int | None = Field(default=None, ge=0)


class ProductResponse(ProductBase):
    model_config = ConfigDict(from_attributes=True)

    id: int
    quantity: int
    created_at: datetime


class MovementCreate(BaseModel):
    movement_type: str = Field(pattern="^(entry|exit)$")
    quantity: int = Field(gt=0)


class MovementResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    product_id: int
    movement_type: str
    quantity: int
    created_at: datetime
