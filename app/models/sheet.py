from app import db
from app.models.item import Item

class Sheet(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    sheet_name = db.Column(db.String)
    member_id = db.Column(db.Integer, db.ForeignKey('member.id'))
    items = db.relationship("Item")

    def to_dict(self):
        return {
            "sheet_name": self.sheet_name,
            "id": self.id,
            "member_id": self.member_id,
            "items": Item.create_list_of_items(self.items)
        }

    @staticmethod
    def create_list_of_sheets(sheets):
        sheets_list = []
        for sheet in sheets:
            sheets_list.append(sheet.to_dict())
            print(sheets_list)
        return sheets_list