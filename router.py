from sanic import Blueprint
from sanic.router import Router

router = Router()

bp = Blueprint('bp', url_prefix='/bp')
