from typing import Any
from typing import Callable

from fastapi import HTTPException
from sqlalchemy.exc import IntegrityError


def unique_violation(func: Callable) -> Callable:
    def wrapper(*args, **kwargs) -> Any:
        try:
            result = func(*args, **kwargs)
        except IntegrityError as e:
            # if email or phone already exists
            # psycopg2.errors.UniqueViolation
            if e.orig.pgcode == "23505":
                detail = e.orig.pgerror[e.orig.pgerror.find("Key ") + 4 : -2]
                raise HTTPException(status_code=400, detail=detail)
        return result

    return wrapper
