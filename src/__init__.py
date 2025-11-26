from flask import Flask, jsonify
from .config.config import Config
from .extensions.extensions import db, migrate
from .routes.products import product_bp

def create_app():
  app = Flask(__name__)
  app.config.from_object(Config)

  db.init_app(app)
  migrate.init_app(app, db)

  app.register_blueprint(product_bp)

  @app.route("/")
  def hello():
    return jsonify({"message": "Hello, World!"})

  @app.route("/health")
  def health():
    return jsonify({"status": "healthy"})

  return app