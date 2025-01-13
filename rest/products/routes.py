from datetime import datetime

from flask_restx import Resource, reqparse, inputs

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

productByIdParams = reqparse.RequestParser()
productByIdParams.add_argument('year_to', type=inputs.int_range(1970, datetime.now().year), required=False, help='Busca somente quantidades a partir deste ano')
productByIdParams.add_argument('year_from', type=inputs.int_range(1970, datetime.now().year), required=False, help='Busca somente quantidades atee deste ano')

@namespace.route('/<int:id>/quantities')
class ProductById(Resource):
  @namespace.expect(productByIdParams)
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
