from flask_restx import Namespace

namespace = Namespace('Products', path='/v1/products', description='Expõe dados de produtos produzidos')
