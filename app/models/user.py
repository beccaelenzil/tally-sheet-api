from app import db
from app.models.sheet import Sheet

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String)
    sheets = db.relationship("Sheet")

    def to_dict(self):
        return {
                "id": self.id,
                "username": self.username,
                "sheets": Sheet.create_list_of_sheets(self.sheets)
            }