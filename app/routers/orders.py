from http.client import HTTPException

import app.logger_util as log

from fastapi import APIRouter, Depends

import app.usecase.orders
from app.routers.utils.db import get_db
from app.schema.orders import CreateOrderModel, CreateOrderResponseModel
from sqlalchemy.orm import Session
from app.models import usecase_exception

router = APIRouter()

@router.post("/orders", response_model=CreateOrderResponseModel, name="order:create", status_code=201, response_model_by_alias=True)
async def create_order(model: CreateOrderModel, db: Session = Depends(get_db)):
    try:
        return app.usecase.orders.createOrders(model=model, db=db)
    except usecase_exception:
        raise HTTPException(status_code=500, message="Internal server error while placing the order")
