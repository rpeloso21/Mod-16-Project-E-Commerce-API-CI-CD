from marshmallow import fields
from schema import ma

class CustomerAccountSchema(ma.Schema):
    id = fields.Integer(required = False)
    username = fields.String(required = True)
    password = fields.String(required = True)
    customer_id = fields.Integer(required = True)
    role = fields.String(required = True)

    class Meta:
        fields = ("id", "username", "password", "customer_id", "role")


customer_account_schema = CustomerAccountSchema()
customer_accounts_schema = CustomerAccountSchema(many=True)