from flask_restx import Resource

from rest.products import namespace
import rest.products.models as models

@namespace.route('/')
class Products(Resource):
  @namespace.marshal_list_with(models.product)
  def get(self):
    '''Lista todos os produtos produzidos'''

    return [
      {
        'id': 6,
        'control': 'vv_Tinto',
        'name': 'Tinto',
        'type': 'Vinho de Mesa'
      }
    ]

@namespace.route('/<int:id>/quantities')
class ProductById(Resource):
  @namespace.marshal_list_with(models.product_quantity)
  def get(self, id):
    '''Dado um ID de produto, retorna a quantidade produzida por ano'''

    return {
      'id': id,
      'control': 'vv_Tinto',
      'name': 'Tinto',
      'type': 'Vinho de Mesa',
      'quantities': {
        'quantity': 100,
        'year': 2023
      }
    }
