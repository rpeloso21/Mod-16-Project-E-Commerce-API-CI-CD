from models.schemas.customerAccountSchema import customer_accounts_schema, customer_account_schema
from services import customerAccountService
from flask import jsonify, request
from utils.util import token_required, role_required
from marshmallow import ValidationError
from caching import cache


@token_required
@role_required('admin')
def save():
    try:
        account_data = customer_account_schema.load(request.json)
    except ValidationError as err:
        return jsonify(err.messages), 400
    
    account_save = customerAccountService.save(account_data)
    if account_save is not None:
        return customer_account_schema.jsonify(account_save), 201
    else:
        return jsonify({"message": "Fallback method error activated","body":account_data}), 400


@cache.cached(timeout=60)
@token_required
@role_required('admin')
def find_all():
    customer_account = customerAccountService.find_all()
    return customer_accounts_schema.jsonify(customer_account), 200


@token_required
@role_required('admin')
def update_customer_account(id):
    customer_account = customerAccountService.update_customer_account(id)

    return customer_account_schema.jsonify(customer_account)


@token_required
@role_required('admin')
def delete_customer_account(id):
    customer_account = customerAccountService.delete_customer_account(id)
    return customer_account_schema.jsonify(customer_account)


def login():
    customer = request.json
    user = customerAccountService.login_customer(customer['username'], customer['password'])
    if user:
        return jsonify(user), 200

    else:
        resp = {
            'status': 'error',
            'message': 'user does not exist'
        }
        return jsonify(resp), 404