from fastapi import APIRouter

from .routers import orders

router = APIRouter()
router.include_router(orders.router)