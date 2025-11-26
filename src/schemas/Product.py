from marshmallow import Schema, fields, ValidationError

def must_be_positive(value):
  if value <= 0:
    raise ValidationError("Value must be positive.")

def must_not_be_empty(value):
  if not value or value.strip() == "":
    raise ValidationError("Value must not be empty.")

class ProductSchema(Schema):
  id = fields.Int(dump_only=True)
  name = fields.Str(required=True, validate=must_not_be_empty)
  description = fields.Str(required=True, validate=must_not_be_empty)
  price = fields.Float(required=True, validate=must_be_positive)
  created_at = fields.DateTime(dump_only=True)
  updated_at = fields.DateTime(dump_only=True)
