from app import db
from app.models.sheet import Sheet

class Member(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String)
    sheets = db.relationship("Sheet")

    def to_dict(self):
        return {
                "id": self.id,
                "username": self.username,
                "sheets": Sheet.create_list_of_sheets(self.sheets)
            }

    @staticmethod
    def create_list_of_members(members):
        members_list = []
        for member in members:
            members_list.append(member.to_dict())
        return members_list