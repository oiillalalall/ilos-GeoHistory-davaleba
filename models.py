from ext import db

class History(db.Model):
    __tablename__ = 'history'
    id = db.Column(db.Integer(), primary_key=True)
    history_title = db.Column(db.String(), nullable=False)
    description = db.Column(db.String(), nullable=False)
    image = db.Column(db.String(), default='/static/images/add_image.png')