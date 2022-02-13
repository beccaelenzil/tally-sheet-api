from app import db
from app.models.item import Item

class Sheet(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    sheet_name = db.Column(db.String)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def to_dict(self):
        return {
            "id": self.id,
            "sheet_name": self.sheet_name,
            "user_id": self.user_id,
            "items": Item.create_list_of_items(self.items)
        }

    @classmethod
    def create_list_of_sheets(sheets):
        sheets_list = []
        for sheet in sheets:
            sheets_list.append(sheet.to_dict)
        return sheets_list