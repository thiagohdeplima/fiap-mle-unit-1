from flask import Flask
from flask_restx import Api

import rest.exports.routes
import rest.products.routes

app = Flask(__name__)
api = Api(app,
  version='1.0',
  title='EMBRAPA Data API',
  description='API para acesso à dados públicos ingeridos da EMBRAPA',
)

api.add_namespace(rest.exports.routes.namespace)
api.add_namespace(rest.products.routes.namespace)

app.config.RESTX_MASK_HEADER = False
app.config.RESTPLUS_MASK_SWAGGER = False
app.config.SWAGGER_UI_DOC_EXPANSION = 'list'

if __name__ == '__main__':
  app.run(debug=True, port=8080)
