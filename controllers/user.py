from sanic.views import HTTPMethodView
from sanic import Blueprint

bp_user = Blueprint('user', url_prefix='/user')


class User(HTTPMethodView):

    async def get(self, request, uid):
        if uid:
            return uid
        return request.raw_args

    async def post(self, request):
        return request.json

    async def put(self, request):
        return request.json

bp_user.add_route(User.as_view(), '/<uid>')
