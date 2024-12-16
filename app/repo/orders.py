import logging as log

from app.db.session import Session
from app.schema.orders import CreateOrderModel
from app.models.orders import CreateOrderDB

logger = log.getLogger('repo')
logger.setLevel(log.INFO)
logger.addHandler(log.StreamHandler())

def create(db_session: Session, *, obj_in: CreateOrderModel) -> CreateOrderDB:
    log.info("creating order in the database")
    orderDBDetails = CreateOrderDB(
        side = obj_in.side.value,
        instrument =  obj_in.instrument,
        type = obj_in.type_.value,
        price = obj_in.limit_price,
        quantity = obj_in.quantity
    )

    db_session.add(orderDBDetails)
    db_session.commit()
    db_session.refresh(orderDBDetails)
    log.info("order created in the database")
    return orderDBDetails

def updateOrderPlacedInExchangeData(db_session: Session, *, obj_id: int, orderPlaced: bool) -> CreateOrderDB:
    log.info("creating order_placed_data in exchange in the database for order id %s", obj_id)
    data = db_session.query(CreateOrderDB).filter(CreateOrderDB.id == obj_id).first()

    if not data:
        raise Exception("unable to find the Order places details for order id : %s", obj_id)

    data.orderPlaced = orderPlaced
    db_session.commit()
    db_session.refresh(data)

    log.info("order updated in the database")
    return data
