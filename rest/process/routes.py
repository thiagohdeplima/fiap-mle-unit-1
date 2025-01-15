from flask_restx import Resource, reqparse, inputs

from rest.process import namespace

import rest.models
import rest.params
import rest.process.models as models

params = rest.params.generic.copy()
params.add_argument('category', type=str)

@namespace.route('')
class Process(Resource):
  @namespace.expect(params)
  @namespace.marshal_list_with(models.process)
  def get(self):
    '''Uvas viníferas processadas'''

    return [
      {
        'id': 6,
        'control': 'ti_Alicante',
        'name': 'Alicante Bouschet',
        'type': 'Tintas',
        'quantities': [
          {
            'unit': 'kg',
            'quantity': 4108858,
            'year': 2023
          }
        ]
      }
    ]
