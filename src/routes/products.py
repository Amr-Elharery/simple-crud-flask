from flask import Blueprint, jsonify, request
from ..extensions.extensions import db
from ..models.Product import Product
from ..schemas.Product import ProductSchema
from sqlalchemy.exc import SQLAlchemyError

product_bp = Blueprint("products", __name__, url_prefix="/api/products")
product_schema = ProductSchema()
products_schema = ProductSchema(many=True)

def handleExceptions():
  return jsonify({"message": "Unknown Error Occurred"})

@product_bp.route("/", methods=["POST"])
def create_product():
  json_data = request.get_json()
  errors = product_schema.validate(json_data)
  if errors:
    return jsonify({"errors": errors}), 400

  # No Errors, Store
  try:
    product = Product(
      name=json_data["name"],
      description=json_data["description"],
      price=json_data["price"]
    )
    db.session.add(product)
    db.session.commit()
    return jsonify({"message": "created successfully", "product": product_schema.dump(product)}), 201
  except SQLAlchemyError as e:
    db.session.rollback()
    print(e)
    return handleExceptions(), 500

@product_bp.route("/", methods=["GET"])
def get_products():
  try:
    q = Product.query.all()
    products = [p.to_dict() for p in q]
    return jsonify({
      "products": products,
      "total": len(products)
    }), 200
  except Exception as e:
    print(e)
    return handleExceptions(), 500

@product_bp.route("/<int:id>", methods=["GET"])
def get_product(id):
  try:
    q = Product.query.get(id)
    if not q:
      return jsonify({"message": "Invalid ID."})
    return jsonify(product_schema.dump(q)), 200
  except Exception as e:
    print(e)
    return handleExceptions(), 500

@product_bp.route("/<int:id>", methods=["PUT", "PATCH"])
def update_product(id):
  try:
    q = Product.query.get(id)
    if not q:
      return jsonify({"message": "Invalid ID."})
  except Exception as e:
    print(e)
    return handleExceptions(), 500

  json_data = request.get_json() or {}
  errors = product_schema.validate(json_data, partial=True)
  if errors:
    return jsonify({"errors": errors}), 400

  # No errors
  try:
    q.name = json_data.get("name", q.name)
    q.description = json_data.get("description", q.description)
    q.price = json_data.get("price", q.price)
    db.session.commit()
    return jsonify({"message": "updated successfully", "product": product_schema.dump(q)}), 200
  except SQLAlchemyError as e:
    db.session.rollback()
    print(e)
    return handleExceptions(), 500

@product_bp.route("/<int:id>", methods=["DELETE"])
def delete_product(id):
  try:
    q = Product.query.get(id)
    if not q:
      return jsonify({"message": "Invalid ID."})
    db.session.delete(q)
    db.session.commit()
    return jsonify({"message": "deleted successfully"}), 200
  except Exception as e:
    print(e)
    return handleExceptions(), 500