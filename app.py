from flask import Flask
from flask_restx import Api

from rest import authorizations

import rest.exports.routes
import rest.products.routes
import rest.process.routes

app = Flask(__name__)
api = Api(app,
  version='1.0',
  title='EMBRAPA Data API',
  description='API para acesso à dados públicos ingeridos da EMBRAPA',
  authorizations=authorizations,
)

api.add_namespace(rest.exports.routes.namespace)
api.add_namespace(rest.products.routes.namespace)
api.add_namespace(rest.process.routes.namespace)

app.config.RESTX_MASK_HEADER = False
app.config.RESTPLUS_MASK_SWAGGER = False
app.config.SWAGGER_UI_DOC_EXPANSION = 'list'

if __name__ == '__main__':
  app.run(debug=True, port=8080)
