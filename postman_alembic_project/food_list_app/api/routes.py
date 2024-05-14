from flask import *
from api.models import Food, User
from api.db import SessionLocal

app = Flask(__name__)

#creation of the blueprint is here! 
# this file is equivalent to "pages.py" in the flask board tutorial. 
# but now, each route isnt just a page. its a function that returns data.

v1_bp = Blueprint('api_v1', __name__)

# to access DB, each route needs to know about psycopg2's engine and SessionLocal
# for all routes, we dependency injection.

# Dependency injection for session in all routes
def get_db():
    db = SessionLocal()
    return db


# Default route
@v1_bp.route('/', methods=['GET'])
def hello_v1():
    return jsonify({"success": True, "message": "Hello from API v1"}), 201

# Display all users
@v1_bp.route("/users/index", methods=['GET'])
def get_all_users():
    db = get_db()
    users = db.query(User).all()
    users_list = [user.__dict__ for user in users]
    db.close()
    return jsonify(users_list)


# Display all restaurants
@v1_bp.route("/indofood/index", methods=['GET'])
def get_all_restaurants():
    db = get_db()
    restaurants = db.query(Food).all()
    restaurants_list = [restaurant.to_dict() for restaurant in restaurants]
    db.close()
    return jsonify(restaurants_list)


# Show a specific user
@v1_bp.route("/users/show/<int:user_id>", methods=['GET'])
def get_user(user_id):
    db = get_db()
    user = db.query(User).filter_by(id=user_id).first()
    if not user:
        return jsonify({"message": "User not found"}), 404
    user_data = user.__dict__
    db.close()
    return jsonify(user_data)


# Show a specific restaurant
@v1_bp.route("/indofood/show/<int:restaurant_id>", methods=['GET'])
def get_restaurant(restaurant_id):
    db = get_db()
    restaurant = db.query(Food).filter_by(id=restaurant_id).first()
    if not restaurant:
        return jsonify({"message": "Restaurant not found"}), 404
    restaurant_data = restaurant.__dict__
    db.close()
    return jsonify(restaurant_data)


# Create a new user (with basic input validation)
@v1_bp.route("/users/create", methods=['POST'])
def create_user():
    # Get data from request.json
    data = request.get_json()

    # Basic validation (replace with more robust checks)
    if not data or not data.get('name') or not data.get('address'):
        return jsonify({"message": "Missing required fields"}), 400

    # Create user object and add to database
    db = get_db()
    user = User(name=data['name'], address=data['address'])  # Assuming other fields from request
    db.add(user)
    db.commit()
    db.close()
    return jsonify({"message": "User created successfully"}), 201


# Create a new restaurant (with basic input validation)
@v1_bp.route("/indofood/create", methods=['POST'])
def create_restaurant():
    # Get data from request.json
    data = request.get_json()

    # Basic validation (replace with more robust checks)
    if not data or not data.get('name') or not data.get('cuisine'):
        return jsonify({"message": "Missing required fields"}), 400

    # Create restaurant object and add to database
    db = get_db()
    restaurant = Food(name=data['name'], cuisine=data['cuisine'])  # Assuming other fields from request
    db.add(restaurant)
    db.commit()
    db.close()
    return jsonify({"message": "Restaurant created successfully"}), 201
