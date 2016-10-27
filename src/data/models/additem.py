from datetime import datetime, timedelta
from sqlalchemy.orm import relationship
from sqlalchemy.schema import Column, ForeignKey
from sqlalchemy.types import Boolean, Integer, String, DateTime

from ..database import db
from ..mixins import CRUDModel


class AddItem(CRUDModel):
    __tablename__ = 'item'
    __table_args__ = {'sqlite_autoincrement': True}
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False, index=True)
    amount = Column(Integer, nullable=False, index=False)
    price = Column(Integer, nullable=False, index=False)
    insert_date = Column(DateTime)

    # Use custom constructor
    # pylint: disable=W0231
    def __init__(self, **kwargs):
        self.insert_date = datetime.utcnow()
        for k, v in kwargs.iteritems():
            setattr(self, k, v)

    @staticmethod
    def find_by_name(item_name):
        return db.session.query(AddItem).filter_by(name=item_name).all()

