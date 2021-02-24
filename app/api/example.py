# Import flask dependencies
from flask import Blueprint, request
from .validators import *
from ..common.Exceptions import ValidationException
import traceback
import json

from ..logic.Commands import *

# Define the blueprint: 'auth', set its url prefix: app.url/auth
example = Blueprint('example', __name__, url_prefix='/example/')

@example.route('/', methods=['GET'])
def example_func():
    try:
        return {'data':'example'}, 200
    except ValidationException as ex:
        return {"status":0, "message":ex.message }, 202
    except Exception as ex:
        traceback.print_exc()
        # There was an error adding the admin
        return {"status":0, "message":"Un error interno" }, 400