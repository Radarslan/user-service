from sqlalchemy import VARCHAR
from sqlalchemy import CheckConstraint
from sqlalchemy import Column
from sqlalchemy import ForeignKey
from sqlalchemy import Integer
from sqlalchemy.orm import relationship

from app.core.settings import data_validation
from app.db.base_class import Base


class PhoneNumbers(Base):
    # columns
    id = Column(
        Integer,
        autoincrement=True,
        nullable=False,
        primary_key=True,
        unique=True,
    )
    number = Column(
        VARCHAR(data_validation.phone_number_max_length),
        nullable=False,
        unique=True,
    )
    user_id = Column(Integer, ForeignKey("users.id"))

    # relationships
    user = relationship("Users", back_populates="phone_numbers")

    # constraints
    CheckConstraint(
        f"length(number) >= {data_validation.phone_number_min_length}"
    )
