# flask-backend/app/models.py

from . import db

class Dam(db.Model):
    __tablename__ = 'dams'
    dam_id = db.Column(db.String(20), primary_key=True)
    dam_name = db.Column(db.String(255), nullable=False)
    full_volume = db.Column(db.Integer)
    latitude = db.Column(db.Numeric(10, 6))
    longitude = db.Column(db.Numeric(10, 6))

    def __repr__(self):
        return f'<Dam {self.dam_name}>'

class DamResource(db.Model):
    __tablename__ = 'dam_resources'
    resource_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    dam_id = db.Column(db.String(20), db.ForeignKey('dams.dam_id'), nullable=False)
    date = db.Column(db.Date, nullable=False)
    storage_volume = db.Column(db.Numeric(10, 3))
    percentage_full = db.Column(db.Numeric(6, 2))
    storage_inflow = db.Column(db.Numeric(10, 3))
    storage_release = db.Column(db.Numeric(10, 3))

    dam = db.relationship('Dam', backref=db.backref('resources', lazy=True))

    def __repr__(self):
        return f'<DamResource {self.resource_id}>'

class LatestData(db.Model):
    __tablename__ = 'latest_data'
    dam_id = db.Column(db.String(20), db.ForeignKey('dams.dam_id'), primary_key=True)
    dam_name = db.Column(db.String(255), nullable=False)
    date = db.Column(db.Date, nullable=False)
    storage_volume = db.Column(db.Numeric(10, 3))
    percentage_full = db.Column(db.Numeric(6, 2))
    storage_inflow = db.Column(db.Numeric(10, 3))
    storage_release = db.Column(db.Numeric(10, 3))

    dam = db.relationship('Dam', backref=db.backref('latest', uselist=False))

    def __repr__(self):
        return f'<LatestData {self.dam_id}>'
