from sanic.app import Sanic
from sanic.request import Request
from sanic.response import json
from router import bp
from controllers.user import bp_user

app = Sanic()


@app.middleware('request')
async def print_req_info(request):
    assert isinstance(request, Request)
    print(request.host)

app.blueprint(bp)
app.blueprint(bp_user)


@app.middleware('response')
async def formatter_response(request, response):
    return json(response)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)
