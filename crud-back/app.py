from flask import Flask
from flask_restful import Api

from resources.player import Players, Player

app = Flask(__name__)
api = Api(app)

api.add_resource(Players, '/players')
api.add_resource(Player, '/players/<string:player_id>')

if __name__ == '__main__':
  app.run(debug=True)
#@app.route('/home', methods=['GET'])
#def index():
#  return (pass)

#if __name__ == '__main__': 
#  app.run(host='127.0.0.1', port=5000, debug=True)
