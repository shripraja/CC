from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Database configuration
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///products.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# Product Model
class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    Product_Name = db.Column(db.String(100), nullable=False)
    Quantity = db.Column(db.Integer, nullable=False)
    Expiry_date = db.Column(db.String(20), nullable=False)

# Create Database
with app.app_context():
    db.create_all()

# -----------------------
# CREATE Product
# -----------------------
@app.route('/products', methods=['POST'])
def create_product():
    data = request.get_json()

    new_product = Product(
        Product_Name=data['Product_Name'],
        Quantity=data['Quantity'],
        Expiry_date=data['Expiry_date']
    )

    db.session.add(new_product)
    db.session.commit()

    return jsonify({"message": "Product added successfully"})


# -----------------------
# READ All Products
# -----------------------
@app.route('/products', methods=['GET'])
def get_products():
    products = Product.query.all()

    output = []

    for p in products:
        product_data = {
            "id": p.id,
            "Product_Name": p.Product_Name,
            "Quantity": p.Quantity,
            "Expiry_date": p.Expiry_date
        }
        output.append(product_data)

    return jsonify(output)


# -----------------------
# UPDATE Product
# -----------------------
@app.route('/products/<int:id>', methods=['PUT'])
def update_product(id):
    product = Product.query.get(id)

    data = request.get_json()

    product.Product_Name = data['Product_Name']
    product.Quantity = data['Quantity']
    product.Expiry_date = data['Expiry_date']

    db.session.commit()

    return jsonify({"message": "Product updated successfully"})


# -----------------------
# DELETE Product
# -----------------------
@app.route('/products/<int:id>', methods=['DELETE'])
def delete_product(id):
    product = Product.query.get(id)

    db.session.delete(product)
    db.session.commit()

    return jsonify({"message": "Product deleted successfully"})


if __name__ == '__main__':
    app.run(debug=True)
