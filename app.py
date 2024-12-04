from flask import Flask
from sqlalchemy import text
from database import db
from schema import ma
from limiter import limiter
from caching import cache
from flask_cors import CORS
from werkzeug.security import generate_password_hash

from models.customer import Customer
from models.employee import Employee
from models.order import Order
from models.product import Product
from models.production import Production
from models.user import User

from routes.customerBP import customer_blueprint
from routes.customerAccountBP import customer_account_blueprint
from routes.orderBP import order_blueprint
from routes.productBP import product_blueprint
from routes.employeeBP import employee_blueprint
from routes.productionBP import production_blueprint
from routes.userBP import user_blueprint
from flask_swagger_ui import get_swaggerui_blueprint

SWAGGER_URL = '/api/docs'
API_URL = '/static/swagger.yaml'

swagger_blueprint = get_swaggerui_blueprint(
    SWAGGER_URL,
    API_URL,
    config={
        'api_name': "E-Commerce API"
    }
)

app = Flask(__name__)


def create_app(config_name):

    app.config.from_object(f'config.{config_name}')
    db.init_app(app)
    ma.init_app(app)
    cache.init_app(app)
    limiter.init_app(app)
    CORS(app)


    return app

def blue_print_config(app):
    app.register_blueprint(customer_blueprint, url_prefix='/customers')
    app.register_blueprint(customer_account_blueprint, url_prefix='/accounts')
    app.register_blueprint(employee_blueprint, url_prefix='/employees')
    app.register_blueprint(production_blueprint, url_prefix='/productions')
    app.register_blueprint(product_blueprint, url_prefix='/products')    
    app.register_blueprint(order_blueprint, url_prefix='/orders')
    app.register_blueprint(user_blueprint, url_prefix='/users')
    app.register_blueprint(swagger_blueprint, url_prefix=SWAGGER_URL)



def configure_rate_limit():
    limiter.limit("100 per day")(customer_blueprint)
    limiter.limit("100 per day")(customer_account_blueprint)
    limiter.limit("100 per day")(employee_blueprint)
    limiter.limit("100 per day")(production_blueprint)
    limiter.limit("100 per day")(product_blueprint)
    limiter.limit("100 per day")(order_blueprint)
    limiter.limit("100 per day")(user_blueprint)
    
if __name__ == "__main__":
    app = create_app('DevelopmentConfig')

    blue_print_config(app)
    configure_rate_limit()

    with app.app_context():

        # db.drop_all()

        db.create_all()

    app.run(debug=True)
