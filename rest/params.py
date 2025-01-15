from datetime import datetime

from flask_restx import reqparse, inputs

generic = reqparse.RequestParser()

generic.add_argument('year_to', type=inputs.int_range(1970, datetime.now().year), required=False, help='Busca somente quantidades a partir deste ano')
generic.add_argument('year_from', type=inputs.int_range(1970, datetime.now().year), required=False, help='Busca somente quantidades atee deste ano')
