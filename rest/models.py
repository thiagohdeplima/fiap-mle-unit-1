from flask_restx import fields, Model

from rest import namespace

product = Model('Product', {
    'id': fields.Integer(required=True, example=6),
    'control': fields.String(required=True, example='vv_Tinto'),
    'name': fields.String(required=True, example='Tinto'),
})

namespace.models[product.name] = product
