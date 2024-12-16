from retry import retry

import app.logger_util as log
import sys

from fastapi import Depends
from fastapi.encoders import jsonable_encoder

from app import repo
from app.models.usecase_exception import UseCaseException
from app.routers.utils.db import get_db
from app.schema.orders import CreateOrderModel, CreateOrderResponseModel
from sqlalchemy.orm import Session
from app import stock_exchange


def createOrders(model: CreateOrderModel, db: Session = Depends(get_db)):
    if model is None:
        return None

    global responseModel
    try:
        orderDB = repo.orders.create(db_session=db, obj_in=model)
        ## encode and send response
        encodedJson = jsonable_encoder(orderDB)
        log.logger.info('Value returned after saving to the db: %s', encodedJson)
        responseModel = CreateOrderResponseModel(**encodedJson)

        ## try connecting to exchange
        retryExchangeCall(responseModel)

        repo.orders.updateOrderPlacedInExchangeData(db_session=db, orderPlaced=True, obj_id=orderDB.id)
        return responseModel

    except ValueError as e:
        log.logger.error("Order cannot be empty/null")
        raise UseCaseException("Order cannot be empty/null", e)

    except:
        e = sys.exc_info()[0]
        log.logger.error("Unable to place order to the db due to error %s", e)
        raise UseCaseException("Unable to place order to the db due to error", e)


@retry(stock_exchange.OrderPlacementError, delay=1, backoff=2, max_delay=4)
def retryExchangeCall(responseModel: CreateOrderResponseModel):
    stock_exchange.place_order(responseModel)