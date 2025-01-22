from datetime import datetime

from flask_restx import Resource, reqparse, inputs

import core.sellings

from rest.sellings import namespace

import rest.models
import rest.params
import rest.sellings.models as models

@namespace.route('')
class Sellings(Resource):
  @namespace.doc(security='Bearer')
  @namespace.expect(rest.params.generic)
  @namespace.marshal_list_with(models.selling)
  def get(self):
    '''Lista todos os dados de comercialização'''

    return core.sellings.get_sellings()
