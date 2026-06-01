from ext import db, app
from models import History, Review

with app.app_context():
    db.drop_all()
    db.create_all()