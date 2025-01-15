from flask_restx import fields, Model

from rest.products import namespace

quantity = Model('Quantity', {
  'unit': fields.String(required=True, example='kg', enum=['kg', 'l', 'usd'], description='Unit of the quantity'),
  'quantity': fields.Integer(required=True, example=100),
  'year': fields.Integer(required=True, example=2020),
})

namespace.models[quantity.name] = quantity
