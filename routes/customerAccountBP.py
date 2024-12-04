from flask import Blueprint
from controllers.customerAccountConrtroller import find_all, update_customer_account, delete_customer_account, save, login

customer_account_blueprint = Blueprint('customer_account_bp', __name__)

customer_account_blueprint.route('/', methods=['POST'])(save)
customer_account_blueprint.route('/', methods=['GET'])(find_all)
customer_account_blueprint.route('/<int:id>', methods=['PUT'])(update_customer_account)
customer_account_blueprint.route('/<int:id>', methods=['DELETE'])(delete_customer_account)


customer_account_blueprint.route('/login', methods=['POST'])(login)