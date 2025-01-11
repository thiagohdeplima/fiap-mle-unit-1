from flask_restx import Resource

from rest import namespace
from rest.models import product

@namespace.route('/products')
class Products(Resource):
  @namespace.marshal_with(product)
  def get(self):
    return 'Products'

