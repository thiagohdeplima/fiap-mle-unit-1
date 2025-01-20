from datetime import datetime

from flask_restx import Resource, reqparse, inputs

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

    return [
      {
        'id': 6,
        'control': 'vv_Tinto',
        'name': 'Tinto',
        'type': 'Vinho de Mesa',
        'quantities': [
          {
            'unit': 'kg',
            'quantity': 100,
            'year': 2020
          }
        ]
      }
    ]

