from flask import Flask, request
from flask_restful import Api
from flask_cors import CORS

from resources.player import Players, Player

app = Flask(__name__)
api = Api(app)

cors = CORS(app)

api.add_resource(Players, '/players')
api.add_resource(Player, '/players/<string:player_id>')

if __name__ == '__main__':
  app.run(debug=True)