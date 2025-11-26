# Flask CRUD API

A simple REST API built with Flask for managing products with full CRUD operations.

## 🏗️ Architecture

```
crud-app/
├── src/
│   ├── __init__.py           # App factory (create_app)
│   ├── config/
│   │   └── config.py         # Database & app configuration
│   ├── extensions/
│   │   └── extensions.py     # Flask extensions (SQLAlchemy, Migrate)
│   ├── models/
│   │   └── Product.py        # Product database model
│   ├── schemas/
│   │   └── Product.py        # Marshmallow validation schemas
│   └── routes/
│       └── products.py       # Product API endpoints
├── run.py                    # Application entry point
├── requirements.txt          # Python dependencies
└── .env                      # Environment variables
```

## 🚀 Setup

### 1. Clone the repository

```bash
git clone https://github.com/Amr-Elharery/simple-crud-flask.git
cd simple-crud-flask
```

### 2. Create virtual environment

```cmd
python -m venv .venv
.venv\Scripts\activate
```

### 3. Install dependencies

```cmd
pip install -r requirements.txt
```

### 4. Configure database

Create a `.env` file in the root directory:

```env
SECRET_KEY=your-secret-key-here
DB_USER=root
DB_PASSWORD=
DB_HOST=localhost
DB_NAME=flask_crud_2
```

### 5. Initialize database

```cmd
flask db init
flask db migrate -m "Initial migration"
flask db upgrade
```

### 6. Run the application

```cmd
python run.py
```

The API will be available at `http://localhost:5000`

## 📡 API Endpoints

### Health Check

```http
GET /health
```

Returns: `{"status": "healthy"}`

### Products

#### Create Product

```http
POST /api/products/
Content-Type: application/json

{
  "name": "Product Name",
  "description": "Product Description",
  "price": 99.99
}
```

#### Get All Products

```http
GET /api/products/
```

Returns: List of all products with total count

#### Get Single Product

```http
GET /api/products/{id}
```

#### Update Product

```http
PUT /api/products/{id}
PATCH /api/products/{id}
Content-Type: application/json

{
  "name": "Updated Name",
  "price": 149.99
}
```

Note: All fields are optional for updates

## 🗄️ Database Schema

### Product Model

| Field       | Type        | Description                    |
| ----------- | ----------- | ------------------------------ |
| id          | Integer     | Primary key (auto-increment)   |
| name        | String(100) | Product name (required)        |
| description | Text        | Product description (required) |
| price       | Float       | Product price (required, > 0)  |
| created_at  | DateTime    | Auto-generated timestamp       |
| updated_at  | DateTime    | Auto-updated timestamp         |

## 🛠️ Tech Stack

- **Flask** - Web framework
- **SQLAlchemy** - ORM for database operations
- **Flask-Migrate** - Database migrations (Alembic)
- **Marshmallow** - Data validation and serialization
- **MySQL** - Database (via mysql-connector-python)
- **python-dotenv** - Environment variable management

## 📝 Key Features

- ✅ RESTful API design
- ✅ Input validation with Marshmallow
- ✅ Database migrations support
- ✅ Error handling and rollback
- ✅ Partial updates (PATCH)
- ✅ Environment-based configuration
- ✅ Factory pattern for app creation

## 🧪 Testing the API

Using curl:

```cmd
REM Create product
curl -X POST http://localhost:5000/api/products/ ^
  -H "Content-Type: application/json" ^
  -d "{\"name\":\"Laptop\",\"description\":\"Gaming laptop\",\"price\":1299.99}"

REM Get all products
curl http://localhost:5000/api/products/

REM Get product by ID
curl http://localhost:5000/api/products/1

REM Update product
curl -X PUT http://localhost:5000/api/products/1 ^
  -H "Content-Type: application/json" ^
  -d "{\"price\":1199.99}"
```

Or use tools like [Postman](https://www.postman.com/) or [Thunder Client](https://www.thunderclient.com/).

## 📄 License

This project is for educational purposes.
