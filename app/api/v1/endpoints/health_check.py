from typing import Any

from fastapi import APIRouter
from fastapi import Depends
from sqlalchemy.orm import Session
from starlette.requests import Request

from app.api import dependencies
from app.schemas.v1.health_check import HealthCheck

router = APIRouter()


@router.get("/", response_model=HealthCheck, tags=["health check"])
def health_check(
    *, request: Request, session: Session = Depends(dependencies.get_db)
) -> Any:
    session.execute("SELECT 1")
    return HealthCheck(message="OK")
