from flask import Flask, request
from flask_restful import Api

from resources.player import Players, Player

app = Flask(__name__)

@app.route('/players', methods=['GET'])
def get(self):
    return {'Players': players}

api = Api(app)

api.add_resource(Players, '/players')
api.add_resource(Player, '/players/<string:player_id>')

if __name__ == '__main__':
  app.run(debug=True)