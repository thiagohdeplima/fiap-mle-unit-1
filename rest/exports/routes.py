from flask_restx import Resource

from rest.exports import namespace
import rest.exports.models as models

@namespace.route('')
class Export(Resource):
  @namespace.marshal_list_with(models.exports)
  def get(self):
    '''Lista todas as exportações por país'''

    return [
      {
        'id': 6,
        'country': 'Portugal',
        'country_code': 'PT'
      }
    ]
