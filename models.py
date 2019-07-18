from app import db


class Ad(db.Model):
    id = db.Column(db.Integer, primary_key=True, index=True)
    settlement = db.Column(db.String(50))
    under_construction = db.Column(db.Boolean)
    description = db.Column(db.Text)
    price = db.Column(db.Integer, index=True)
    oblast_district = db.Column(db.String(50), index=True)
    living_area = db.Column(db.Float)
    has_balcony = db.Column(db.Boolean)
    address = db.Column(db.String(255))
    construction_year = db.Column(db.Integer, index=True)
    rooms_number = db.Column(db.Integer)
    premise_area = db.Column(db.Float)
    active = db.Column(db.Boolean, index=True)

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
                active=True):
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
        self.active = active

    def __repr__(self):
        #return '<Ad %r (%r)>' % (self.id, self.settlement)
        return '%r' % (self.id)
