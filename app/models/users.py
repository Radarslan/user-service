from sqlalchemy import VARCHAR
from sqlalchemy import Boolean
from sqlalchemy import CheckConstraint
from sqlalchemy import Column
from sqlalchemy import Index
from sqlalchemy import Integer
from sqlalchemy.orm import relationship

from app.core.settings import data_validation
from app.db.base_class import Base


class Users(Base):
    # columns
    id = Column(
        Integer,
        autoincrement=True,
        nullable=False,
        primary_key=True,
        unique=True,
    )
    first_name = Column(
        VARCHAR(data_validation.first_name_max_length), nullable=False
    )
    last_name = Column(
        VARCHAR(data_validation.last_name_max_length), nullable=False
    )
    is_active = Column(Boolean, default=True, nullable=False)

    # relationships
    emails = relationship(
        "Emails",
        back_populates="user",
        cascade="all, delete-orphan",
    )
    phone_numbers = relationship(
        "PhoneNumbers",
        back_populates="user",
        cascade="all, delete-orphan",
    )

    # constraints
    CheckConstraint(
        f"length(first_name) >= {data_validation.names_min_length}"
    )
    CheckConstraint(f"length(last_name) >= {data_validation.names_min_length}")


# indexes
"""
We assume user creation will be occurring to the significantly less
margin than read. Therefore, indexes for names are added.
"""
Index(
    f"{Users.__tablename__}_first_name",
    Users.first_name,
    postgresql_using="btree",
)
Index(
    f"{Users.__tablename__}_last_name",
    Users.last_name,
    postgresql_using="btree",
)
Index(
    f"{Users.__tablename__}_first_name_last_name",
    Users.first_name,
    Users.last_name,
    postgresql_using="btree",
)
