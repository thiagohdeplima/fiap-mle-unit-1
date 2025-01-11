from flask_restx import Resource

from rest import namespace

import rest.models as models

@namespace.route('/products')
class Products(Resource):
  @namespace.marshal_list_with(models.product)
  def get(self):
    '''List all products'''

    return [
      {
        'id': 6,
        'control': 'vv_Tinto',
        'name': 'Tinto',
        'quantities': {
            'quantity': 100,
            'year': 2023
          }
      }
    ]
