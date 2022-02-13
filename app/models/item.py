from app import db

class Item(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    item_name = db.Column(db.String)
    sheet_id = db.Column(db.Integer, db.ForeignKey('sheet.id'))

    def to_dict(self):
        return {
            "id": self.id,
            "item_name": self.item_name,
            "sheetr_id": self.sheet_id
        }

    @classmethod
    def create_list_of_items(items):
        items_list = []
        for item in items:
            items_list.append(item.to_dict)
        return items_list