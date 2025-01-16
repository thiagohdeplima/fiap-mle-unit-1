from flask_restx import fields, Model

import rest.models

from rest.sellings import namespace

selling = Model('Selling', {
  'id': fields.Integer(required=True, example=6),
  'type': fields.String(required=True, example='Vinho de Mesa'),
  'control': fields.String(required=True, example='vv_Tinto'),
  'name': fields.String(required=True, example='Tinto'),
  'quantities': fields.List(fields.Nested(rest.models.quantity), required=True),

})

namespace.models[selling.name] = selling
