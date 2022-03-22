from sqlalchemy import VARCHAR
from sqlalchemy import CheckConstraint
from sqlalchemy import Column
from sqlalchemy import ForeignKey
from sqlalchemy import Integer
from sqlalchemy.orm import relationship

from app.core.settings import data_validation
from app.db.base_class import Base


class Emails(Base):
    # columns
    id = Column(
        Integer,
        autoincrement=True,
        nullable=False,
        primary_key=True,
        unique=True,
    )
    mail = Column(
        VARCHAR(data_validation.email_number_max_length),
        nullable=False,
        unique=True,
    )
    user_id = Column(Integer, ForeignKey("users.id"))

    # relationships
    user = relationship("Users", back_populates="emails")

    # constraints
    CheckConstraint(
        f"length(mail) >= {data_validation.email_number_min_length}"
    )
