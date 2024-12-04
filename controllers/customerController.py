from flask import request, jsonify
from models.schemas.customerSchema import customer_schema, customers_schema
from services import customerService
from marshmallow import ValidationError
from models.customer import Customer
from caching import cache
from utils.util import token_required, role_required
from sqlalchemy.orm import Session
from database import db


@token_required
@role_required('admin')
def save():
    try:
        customer_data = customer_schema.load(request.json)
    except ValidationError as err:
        return jsonify(err.messages), 400
    
    customer_save = customerService.save(customer_data)
    if customer_save is not None:
        return customer_schema.jsonify(customer_save), 201
    else:
        return jsonify({"message": "Fallback method error activated","body":customer_data}), 400


@cache.cached(timeout=60)
@token_required
@role_required('admin')
def find_all():
    customers = customerService.find_all()
    return customers_schema.jsonify(customers), 200


@token_required
@role_required('admin')
def update_customer(id):
    customer = customerService.update_customer(id)

    return customer_schema.jsonify(customer)



@token_required
@role_required('admin')
def delete_customer(id):
    customer = customerService.delete_customer(id)
    return customer_schema.jsonify(customer)