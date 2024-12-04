from flask import request
from sqlalchemy.orm import Session
from database import db
from models.customer import Customer
from models.customerAccount import CustomerAccount
from circuitbreaker import circuit
from sqlalchemy import select
from utils.util import encode_token


def save(account_data):

    with Session(db.engine) as session:
        with session.begin():
            new_account = CustomerAccount(username=account_data['username'], password=account_data['password'], customer_id=account_data['customer_id'], role=account_data['role'])
            session.add(new_account)
            session.commit()
        session.refresh(new_account)
        return new_account


def find_all():
    query = select(CustomerAccount).join(Customer).where(Customer.id == CustomerAccount.customer_id)
    customer_accounts = db.session.execute(query).scalars().all()
    return customer_accounts


def update_customer_account(id):
    with Session(db.engine) as session:

        customer_account_data = request.get_json()
        customer_account = session.get(CustomerAccount, id)
        
        customer_account.username = customer_account_data["username"]
        customer_account.password = customer_account_data["password"]
        customer_account.customer_id = customer_account_data["customer_id"]

        session.commit()
        session.refresh(customer_account)

    return customer_account


def delete_customer_account(id):
    with Session(db.engine) as session:

        customer_account = session.get(CustomerAccount, id)
        session.delete(customer_account)
        session.commit()

    return customer_account



def login_customer(username, password): 
    user = (db.session.execute(db.select(CustomerAccount).where(CustomerAccount.username == username, CustomerAccount.password == password)).scalar_one_or_none())
    role = user.role
    if user:
        auth_token = encode_token(user.id, role)
        resp = {
            'status': 'success',
            'message': 'successfully logged in',
            'auth_token': auth_token
        }
        return resp
    else:
        return None
    