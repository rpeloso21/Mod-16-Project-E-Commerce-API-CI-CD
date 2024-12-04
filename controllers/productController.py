from flask import request, jsonify
from models.schemas.productSchema import product_schema, products_schema
from marshmallow import ValidationError
from services import productService
from caching import cache
from utils.util import role_required, token_required


@token_required
@role_required('admin')
def save():
    try:
        product_data = product_schema.load(request.json)
    except ValidationError as err:
        return jsonify(err.messages), 400
    
    product_save = productService.save(product_data)
    if product_save is not None:
        return product_schema.jsonify(product_save), 201
    else:
        return jsonify({"message": "Fallback method error activated","body":product_data}), 400


@cache.cached(timeout=60)
@token_required
@role_required('admin')
def find_all():
    products = productService.find_all()
    return products_schema.jsonify(products), 200


@token_required
@role_required('admin')
def update_product(id):
    product = productService.update_product(id)

    return product_schema.jsonify(product)


@token_required
@role_required('admin')
def delete_product(id):
    product = productService.delete_product(id)
    return product_schema.jsonify(product)

def find_all_pagination():
    page = request.args.get('page', 1, type=int)
    per_page = request.args.get('per_page', 10, type=int)
    return products_schema.jsonify(productService.find_all_pagination(page=page, per_page=per_page)), 200
