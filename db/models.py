from sqlalchemy import Column, Integer, String, Boolean, Text, Float
from db.database import Base


class Ad(Base):
    __tablename__ = 'ads'
    id = Column(Integer, primary_key=True)
    settlement = Column(String(50))
    under_construction = Column(Boolean)
    description = Column(Text)
    price = Column(Integer)
    oblast_district = Column(String(50))
    living_area = Column(Float)
    has_balcony = Column(Boolean)
    address = Column(String(255))
    construction_year = Column(Integer)
    rooms_number = Column(Integer)
    premise_area = Column(Float)
    active = Column(Boolean)

    def __init__(
                self,
                id,
                settlement=None,
                under_construction=None,
                description=None,
                price=0,
                oblast_district=None,
                living_area=0,
                has_balcony=False,
                address=None,
                construction_year=0,
                rooms_number=0,
                premise_area=0,
                active=False):
        self.id = id
        self.settlement = settlement
        self.under_construction = under_construction
        self.description = description
        self.price = price
        self.oblast_district = oblast_district
        self.living_area = living_area
        self.has_balcony = has_balcony
        self.address = address
        self.construction_year = construction_year
        self.rooms_number = rooms_number
        self.premise_area = premise_area
        self.active = True

    def __repr__(self):
        return '<Ad %r (%r)>' % (self.id, self.settlement)
