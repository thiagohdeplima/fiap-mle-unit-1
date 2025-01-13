from flask_restx import fields, Model

from rest.exports import namespace

exports = Model('Export', {
  'id': fields.Integer(required=True, example=6),
  'country': fields.String(required=True, example='Portugal'),
  'country_code': fields.String(required=True, example='PT', description='ISO 3166-1 alpha-2 code'),
})

namespace.models[exports.name] = exports
