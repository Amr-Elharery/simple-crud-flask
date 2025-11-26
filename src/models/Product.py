from ..extensions.extensions import db
from datetime import datetime

class Product(db.Model):
  __tablename__ = 'products'
  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(100), nullable=False)
  description = db.Column(db.Text, nullable=False)
  price = db.Column(db.Float, nullable=False, default=0.0)
  created_at = db.Column(db.DateTime, default=datetime.utcnow)
  updated_at = db.Column(db.DateTime, onupdate=datetime.utcnow)
  
  def to_dict(self):
    return {
      "id": self.id,
      "name": self.name,
      "description": self.description,
      "price": self.price,
      "created_at": self.created_at,
      "updated_at": self.updated_at
    }