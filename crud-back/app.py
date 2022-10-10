from flask import Flask, request
from flask_restful import Api
from flask_pymongo import PyMongo

from resources.player import Players, Player

app = Flask(__name__)
app.config['MONGO_URI']='mongodb://localhost/pythonmongodb'

mongo = PyMongo(app)

#@app.route('/players', methods=['GET'])
#def get(self):
#    return {'Players': players}

@app.route('/player', methods=['POST'])
def post():
  name = request.json['name']
  position = request.json['position']
  team = request.json['team']
  shirt = request.json['shirt']
  height = request.json['height']
  weight = request.json['weight']
  gols = request.json['gols']
  stars = request.json['stars']

  if name and position and team and shirt and height and weight and gols and stars: 
    mongo.db.player.insert(
      {
      'name': name,
      'postion': position,
      'team': team,
      'shirt': shirt,
      'height': height,
      'weight': weight,
      'gols': gols,
      'stars': stars
      }
    )
  else:
    {'message': 'Error, 404'}
    
# --------------------------->

# api = Api(app)

#api.add_resource(Players, '/players')
#api.add_resource(Player, '/players/<string:player_id>')

if __name__ == '__main__':
  app.run(debug=True)