from flask import Blueprint
from controllers.customerController import save, find_all, update_customer, delete_customer


customer_blueprint = Blueprint('customer_bp', __name__)

@customer_blueprint.route('/', methods=['POST'])
def test():
    return "New test for customers post route"
customer_blueprint.route('/', methods=['GET'])(find_all)
customer_blueprint.route('/<int:id>', methods=['PUT'])(update_customer)
customer_blueprint.route('/<int:id>', methods=['DELETE'])(delete_customer)