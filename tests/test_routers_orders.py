from app.main import app
from app.schema import orders

from fastapi import FastAPI
from sqlalchemy.orm import Session
from fastapi.testclient import TestClient
from fastapi.encoders import jsonable_encoder

from app.schema.orders import CreateOrderModel, CreateOrderResponseModel

client = TestClient(app)

def test_order_create(app: FastAPI,
    db_session: Session,
    client: TestClient):
    orderSchema = CreateOrderModel(
        type="market",
        side="buy",
        instrument="abc",
        limit_price="13",
        quantity=1
    )
    req_data = jsonable_encoder(orderSchema)
    response = client.post(
        "/orders",
        json=req_data,
    )
    data = response.json()
    print(data)
    assert response.status_code == 200
    assert CreateOrderResponseModel(**data)