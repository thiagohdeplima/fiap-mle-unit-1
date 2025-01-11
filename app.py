from flask import Flask
from flask_restx import Api

from rest.namespaces import namespace

app = Flask(__name__)
api = Api(app, version='1.0', title='EMBRAPA Data API')

api.add_namespace(namespace)

if __name__ == '__main__':
  app.run(debug=True, port=8080)
