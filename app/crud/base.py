from typing import Any
from typing import Dict
from typing import Generic
from typing import List
from typing import Optional
from typing import Type
from typing import TypeVar
from typing import Union

from fastapi.encoders import jsonable_encoder
from fastapi.params import Query
from pydantic import BaseModel
from sqlalchemy.orm import Session
from sqlalchemy.sql.expression import and_

from app.core.settings import data_validation
from app.core.utils.exceptions.unique_violation import unique_violation
from app.db.base_class import Base

ModelType = TypeVar("ModelType", bound=Base)
CreateSchemaType = TypeVar("CreateSchemaType", bound=BaseModel)
QuerySchemaType = TypeVar("QuerySchemaType", bound=Query)
UpdateSchemaType = TypeVar("UpdateSchemaType", bound=BaseModel)


def exclude_unset(obj_data: dict):
    return {key: value for key, value in obj_data.items() if value is not None}


class CRUDBase(
    Generic[ModelType, CreateSchemaType, QuerySchemaType, UpdateSchemaType]
):
    def __init__(self, model: Type[ModelType]):
        """
        CRUD object with default methods to Create, Read, Update, Delete (CRUD).

        **Parameters**

        * `model`: A SQLAlchemy model class
        * `schema`: A Pydantic model (schema) class
        """
        self.model = model

    @unique_violation
    def create(
        self, db: Session, *, obj_in: Union[CreateSchemaType, Dict[str, Any]]
    ) -> ModelType:
        if isinstance(obj_in, dict):
            obj_in_data = obj_in
        else:
            obj_in_data = jsonable_encoder(obj_in)
        db_obj = self.model(**obj_in_data)

        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj

    def find_many(
        self,
        db: Session,
        query: QuerySchemaType,
        skip: int = 0,
        limit: int = data_validation.page_size,
    ) -> List[ModelType]:
        filters = []
        for parameter in query.__slots__:
            if isinstance(getattr(query, parameter), str):
                filters.append(
                    getattr(self.model, parameter).like(
                        f"%{getattr(query, parameter)}%"
                    )
                )
            elif isinstance(getattr(query, parameter), bool):
                filters.append(
                    getattr(self.model, parameter) == getattr(query, parameter)
                )
        return (
            db.query(self.model)
            .filter(and_(*filters))
            .order_by(self.model.id)
            .offset(skip)
            .limit(limit)
            .all()
        )

    def read_many(
        self,
        db: Session,
        *,
        skip: int = 0,
        limit: int = data_validation.page_size,
    ) -> List[ModelType]:
        db_objs = (
            db.query(self.model)
            .order_by(self.model.id)
            .offset(skip)
            .limit(limit)
            .all()
        )
        return db_objs

    def read(self, db: Session, entity_id: Any) -> Optional[ModelType]:
        return db.query(self.model).get(entity_id)

    @unique_violation
    def update(
        self,
        db: Session,
        *,
        db_obj: ModelType,
        obj_in: Union[UpdateSchemaType, Dict[str, Any]],
    ) -> ModelType:
        if isinstance(obj_in, dict):
            update_data = exclude_unset(obj_in)
        else:
            update_data = jsonable_encoder(obj_in, exclude_unset=True)

        for field in db_obj.__dict__:
            if field in update_data:
                setattr(db_obj, field, update_data[field])
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj

    def delete(self, db: Session, *, db_obj: ModelType) -> Optional[ModelType]:
        db.delete(db_obj)
        db.commit()
        return db_obj
