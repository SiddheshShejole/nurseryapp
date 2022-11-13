from app import db


# All Tables in database

class Product(db.Model):
    product_id = db.Column(db.Integer(), primary_key=True)
    category = db.Column(db.String(20), unique=False, nullable=False)
    subcategory = db.Column(db.String(20), unique=False, nullable=False)
    productname = db.Column(db.String(20), unique=False, nullable=False)
    rate = db.Column(db.Integer(), unique=False, nullable=False)
    image = db.Column(db.String(20), unique=False, nullable=False)


class Customer(db.Model):
    mobile_number = db.Column(db.Integer(), primary_key=True)
    password = db.Column(db.String(20), unique=False, nullable=False)
    cust_name = db.Column(db.String(20), unique=False, nullable=False)


class OrderProduct(db.Model):
    order_id = db.Column(db.Integer(), primary_key=True)
    order_date = db.Column(db.DateTime, unique=False, nullable=False)
    mobile_number = db.Column(db.Integer(), unique=False, nullable=False)
    address = db.Column(db.String(100), unique=False, nullable=False)
    total_amount = db.Column(db.Integer(), unique=False, nullable=False)


class OrderDetails(db.Model):
    order_id = db.Column(db.Integer(), primary_key=True)
    product_id = db.Column(db.Integer(), primary_key=True)
    quantity = db.Column(db.Integer(), unique=False, nullable=False)
    rate = db.Column(db.Integer(), unique=False, nullable=False)
    amount = db.Column(db.Integer(), unique=False, nullable=False)


class Admin(db.Model):
    admin_id = db.Column(db.Integer(), primary_key=True)
    password = db.Column(db.String(20), unique=False, nullable=False)
