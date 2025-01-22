from flask_restx import Resource

from flask_jwt_extended import jwt_required

import core.product

from rest.products import namespace

import rest.models
import rest.params
import rest.products.models as models


@namespace.route('')
class Products(Resource):
  @jwt_required()
  @namespace.doc(security='Bearer')
  @namespace.expect(rest.params.generic)
  @namespace.marshal_list_with(models.product)
  def get(self):
    '''Lista todos os produtos produzidos'''

    return core.product.get_products()

