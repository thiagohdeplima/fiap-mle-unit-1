from flask_restx import Resource

from flask_jwt_extended import jwt_required

from rest.imports import namespace

import core.imports

import rest.models
import rest.params
import rest.imports.models as models

params = rest.params.generic.copy()
params.add_argument('category', type=str)

@namespace.route('')
class Import(Resource):
  @jwt_required()
  @namespace.doc(security='Bearer')
  @namespace.expect(params)
  @namespace.marshal_list_with(models.imports)
  def get(self):
    '''Lista todas as importações por país'''

    return core.imports.get_imports()
