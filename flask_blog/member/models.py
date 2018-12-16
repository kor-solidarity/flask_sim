from flask_blog import db


class Member(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    # username