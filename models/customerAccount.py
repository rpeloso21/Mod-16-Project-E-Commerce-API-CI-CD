from database import db, Base
from sqlalchemy.orm import Mapped, mapped_column
from typing import List



class CustomerAccount(Base):
    __tablename__ = 'customerAccount'
    id: Mapped[int] = mapped_column(primary_key = True)
    username: Mapped[str] = mapped_column(db.String(255), nullable = False)
    password: Mapped[str] = mapped_column(db.String(255), nullable = False)
    customer_id: Mapped[int] = mapped_column(db.ForeignKey('customers.id'))
    # customer: Mapped['Customer'] = db.relationship(back_populates='customer_account', lazy='noload')
    role: Mapped[str] = mapped_column(db.String(255), nullable = False)