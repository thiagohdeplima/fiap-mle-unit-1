from flask_restx import Resource, reqparse, inputs

from rest.exports import namespace

import core.export

import rest.models
import rest.params
import rest.exports.models as models

params = rest.params.generic.copy()
params.add_argument('category', type=str)

@namespace.route('')
class Export(Resource):
  @namespace.doc(security='Bearer')
  @namespace.expect(params)
  @namespace.marshal_list_with(models.exports)
  def get(self):
    '''Lista todas as exportações por país'''

    return core.export.get_exports()
