from ext import db, app
from models import History, Review, User

with app.app_context():
    db.drop_all()
    db.create_all()

    admin = User(username="iliamagaribiwia", password="iliahooperia", role="admin")
    admin.create()