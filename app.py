from flask import Flask,request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
import os


app=Flask(__name__)


basedir = os.path.abspath(os.path.dirname(__file__))

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' +os.path.join(basedir,'db.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False

db=SQLAlchemy(app)

ma = Marshmallow(app)

class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True)
    qty = db.Column(db.Integer)

    def __init__ (self, name, qty):
        self.name=name
        self.qty=qty

      

class ProductSchema(ma.Schema):
    class Meta:
        fields=('id','name', 'qty')

product_schema = ProductSchema()
products_schema = ProductSchema(many=True)

@app.route('/product', methods=['POST'])
def add_product():
    name = request.json['name']
    qty = request.json['qty']
    new_product = Product(name,qty)
    db.session.add(new_product)
    db.session.commit()
    return product_schema.jsonify(new_product)
 
@app.route('/product>', methods=['GET'])
def get_products():
    all_products = Product.query.all()
    result= product_schema.dump(all_products)
    return jsonify(result.data)

@app.route('/product/<id>', methods=['PUT'])
def update_product():
    product=Product.query.get(id)
    name = request.json['name']
    qty = request.json['qty']
    product.qty=qty
    
    db.session.commit()
    return product_schema.jsonify(product)

@app.route('/product/<id>', methods=['DELETE'])
def delete_product(id):
    product = Product.query.get(id)
    db.session.delete(product)
    db.session.commit()
    return product_schema.jsonify(product)
    
#runs server
if __name__ == '__main__': 
    app.run(debug = True)
    