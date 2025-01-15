from datetime import datetime

from flask_restx import Resource, reqparse, inputs

from rest.products import namespace

import rest.models
import rest.params
import rest.products.models as models

@namespace.route('')
class Products(Resource):
  @namespace.expect(rest.params.generic)
  @namespace.marshal_list_with(models.product)
  def get(self):
    '''Lista todos os produtos produzidos'''

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

