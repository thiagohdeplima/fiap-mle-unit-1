from flask_restx import fields, Model

import rest.models
from rest.imports import namespace

imports = Model('Import', {
  'id': fields.Integer(required=True, example=6),
  'country': fields.String(required=True, example='Portugal'),
  'country_code': fields.String(required=True, example='PT', description='ISO 3166-1 alpha-2 code'),
  'category': fields.String(required=True, example='Vinhos de Mesa'),
  'quantities': fields.List(fields.Nested(rest.models.quantity), required=True),
})

namespace.models[imports.name] = imports
