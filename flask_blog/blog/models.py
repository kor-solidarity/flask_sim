from flask_blog import db
from datetime import datetime


class Article(db.Model):
    gul_id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.VARCHAR(80))
    # author - 나중에 추가
    ip = db.Column(db.VARCHAR(40))
    # 조회
    views = db.Column(db.Integer)
    # 답글달리고있는 원글번호.
    ori_id = db.Column(db.Integer)
    step = db.Column(db.Integer)
    depth = db.Column(db.Integer)
    # 본문
    text = db.Column(db.TEXT)
    time = db.Column(db.TIMESTAMP)
    deleted = db.Column(db.Boolean)
    edit_time = db.Column(db.TIMESTAMP, nullable=True)

    def __init__(self, title, ip, ori_id, text):
        self.title = title
        self.ip = ip
        self.ori_id = ori_id
        self.step = 0
        self.depth = 0
        self.text = text
        self.time = datetime.utcnow()
        self.deleted = 0
