from flask_restx import Resource

from rest.products import namespace
import rest.products.models as models

@namespace.route('/')
class Products(Resource):
  @namespace.marshal_list_with(models.product)
  def get(self):
    '''List all products'''

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
    '''Return all quantities of a product by year'''

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
