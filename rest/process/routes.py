from flask_restx import Resource, reqparse, inputs

from flask_jwt_extended import jwt_required

from rest.process import namespace

import core.process

import rest.models
import rest.params
import rest.process.models as models

params = rest.params.generic.copy()
params.add_argument('category', type=str)

@namespace.route('')
class Process(Resource):
  @jwt_required()
  @namespace.doc(security='Bearer')
  @namespace.expect(params)
  @namespace.marshal_list_with(models.process)
  def get(self):
    '''Uvas viníferas processadas'''

    return core.process.get_process()
