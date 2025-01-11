from flask_restx import fields, Model

from rest import namespace

product_quantity = Model('ProductQuantity', {
  'quantity': fields.Integer(required=True, example=100),
  'year': fields.Integer(required=True, example=2020),
})

product = Model('Product', {
  'id': fields.Integer(required=True, example=6),
  'type': fields.String(required=True, example='Vinho de Mesa'),
  'control': fields.String(required=True, example='vv_Tinto'),
  'name': fields.String(required=True, example='Tinto'),

  'quantities': fields.List(
    fields.Nested(product_quantity)
  )
})

namespace.models[product.name] = product
namespace.models[product_quantity.name] = product_quantity
