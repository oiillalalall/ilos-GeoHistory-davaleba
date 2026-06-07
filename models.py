from ext import db, login_manager
from flask_login import UserMixin

class BaseModel:
    def create(self):
        db.session.add(self)
        db.session.commit()

    @staticmethod
    def save():
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

class History(db.Model, BaseModel):
    __tablename__ = 'history'
    id = db.Column(db.Integer(), primary_key=True)
    history_title = db.Column(db.String(), nullable=False)
    description = db.Column(db.String(), nullable=False)
    image = db.Column(db.String(), server_default='add_image.png')


class Review(db.Model, BaseModel):
    __tablename__ = 'review'

    id = db.Column(db.Integer(), primary_key=True)
    text = db.Column(db.String(), nullable=False)
    history_id = db.Column(db.ForeignKey('history.id'))

#karoche ro miwers kods tviton miyvars ra :))))))))))))))))))))

class User(db.Model, BaseModel, UserMixin):
    __tablename__ = 'user'

    id = db.Column(db.Integer(), primary_key=True)
    username = db.Column(db.String())
    password = db.Column(db.String())
    role = db.Column(db.String(), default='guest')

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)
